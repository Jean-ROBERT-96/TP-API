from fastapi import FastAPI, HTTPException
from typing import Optional
from sqlmodel import Field, SQLModel, select, Session, create_engine
from entities.facture import Facture
from context.db_context import DBContext

# ORM : SQLModel

app = FastAPI()
context = DBContext

class FactureUpdate(SQLModel):
    client: Optional[int] = None
    montantHT: Optional[float] = None
    montantTTC: Optional[float] = None

@app.get("/factures/{numero}")
def getFacture(numero: str):
    with Session(context.engine) as session:
        facture= session.get(Facture, numero)
    if not facture:
        raise HTTPException(status_code=404, detail="facture non trouvé")
    return facture

@app.post("/factures/{numero}")
def newFacture(Facture:Facture):
    with Session(context.engine) as session:
        session.add(Facture)
        session.commit()
        session.refresh(Facture)
    return {"ok":True}

@app.delete("/factures/{numero}")
def supprFacture(numero: str):
    with Session(context.engine) as session:
        factureDb = session.get(Facture, numero)
        if not factureDb:
            raise HTTPException(status_code=404, detail="Facture non trouvé")
        session.delete(factureDb)
        session.commit()
    return {"ok":True}

@app.put("/factures/{numero}")
def updateFacture(numero: str, facture:FactureUpdate):
    with Session(context.engine) as session:
        factureDb =session.get(Facture, numero)
        if not factureDb:
            raise HTTPException(status_code=404, detail="Facture non trouvé")
        dataFacture = facture.model_dump(exclude_unset=True)
        for key, value in dataFacture.items():
            setattr(factureDb, key, value)
        session.add(factureDb)
        session.commit()
        session.refresh()
        return {"ok":True}
    