from typing import Optional
from sqlmodel import Field, SQLModel, select, Session, create_engine

class Facture(SQLModel, table = True):
    numero: str = Field(primary_key=True)
    client: int
    montantHT: float
    montantTTC: float

""" def createFactures():
    f1 = Facture(numero="2", client=1, montantHT=2.0, montantTTC=134.0)
    f2 = Facture(numero="12", client=3, montantHT=6.0, montantTTC=54.0)
    f3 = Facture(numero="6", client=3, montantHT=5.0, montantTTC=73.0)
    f4 = Facture(numero="4", client=1, montantHT=1.0, montantTTC=36.0)

    with Session(engine) as session : 
        session.add(f1)
        session.add(f2)
        session.add(f3)
        session.add(f4)
        session.commit()
        session.close()

def selectFactures():
    with Session(engine) as session:
        statement = select(Facture)
        results  = session.exec(statement)
        Facture = results.all()
        print(Facture)

def main():
    createFactures()
    selectFactures()

if __name__ == "__main__" :
    main()
 """