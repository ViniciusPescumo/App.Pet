from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API DO APP PET")

@app.post("/pets/", response_model=schemas.PetResponse)
def criar_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    novo_pet = models.Pet(**pet.dict())
    db.add(novo_pet)
    db.commit()
    db.reflesh(novo_pet)
    return novo_pet

@app.get("/pets/")
def listar_pets(db: Session = Depends(get_db())):
    return db.query(models.Pet).all()

