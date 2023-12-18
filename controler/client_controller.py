from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlmodel import Field, Session, SQLModel, create_engine, select
from context.db_context import DBContext
from entities.client import Client

#setup.py pour installer un packagecustom

class ClientUpdate(SQLModel):
    nom: Optional[str] = None
    adresse1: Optional[str] = None
    adresse2: Optional[str] = None
    cp: Optional[str] = None
    ville: Optional[str] = None

app = FastAPI()
context = DBContext

@app.get("/client/{client_id}")
def get_client(client_id: int):
    with Session(context.engine) as session:
        client_get = session.get(Client, client_id)
        if not client_get:
            raise HTTPException(status_code=404, detail="Client not found")
        return client_get

@app.post("/client/{client_id}")
def create_client(client: Client):
    with Session(context.engine) as session:
        session.add(client)
        session.commit()
        session.refresh(client)
        return {"ok": True}

@app.put("/client/{client_id}")
def edit_client(client_id: int, client: ClientUpdate):
    with Session(context.engine) as session:
        db_client = session.get(Client, client_id)
        if not db_client:
            raise HTTPException(status_code=404, detail="Client not found")
        client_data = client.model_dump(exclude_unset=True)
        for key, value in client_data.items():
            setattr(db_client, key, value)
        session.add(db_client)
        session.commit()
        session.refresh(db_client)
        return {"ok": True}

@app.delete("/client/{client_id}")
def remove_client(client_id: int):
    with Session(context.engine) as session:
        client_db = session.get(Client, client_id)
        if not client_db:
            raise HTTPException(status_code=404, detail="Client not found")
        session.delete(client_db)
        session.commit()
        return {"ok": True}