from sqlmodel import SQLModel

class Client(SQLModel, table=True):
    n_: int
    nom: str
    adresse1: str
    adresse2: str
    cp: str
    ville: str