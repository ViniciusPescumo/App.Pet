from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
import models
import schemas
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="API DO APP PET")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#CRIAR PET
@app.post("/pets", response_model=schemas.PetResponse)
def criar_pet(pet: schemas.PetCreate, db: Session = Depends(get_db)):
    novo_pet = models.Pet(**pet.dict())
    db.add(novo_pet)
    db.commit()
    db.refresh(novo_pet)
    return novo_pet

#BUSCAR TODOS
@app.get("/pets")
def listar_pets(db: Session = Depends(get_db)):
    return db.query(models.Pet).all()

#BUSCAR POR AP
@app.get("/apartamento/{apartamento}")
def buscar_por_ap(apartamento: str, db: Session = Depends(get_db)):
    pets = db.query(models.Pet).filter(models.Pet.apartamento == apartamento).all()
    return pets

#ATUALIZAR PET
@app.put("/pets/{pet_id}")
def atualizar_pet(pet_id: int, dados_atualizados: schemas.PetCreate, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")

    for key, value in dados_atualizados.dict().items():
        setattr(pet, key, value)

    pet.nome = dados_atualizados.nome
    pet.apartamento = dados_atualizados.apartamento
    pet.tipo = dados_atualizados.tipo

    db.commit()
    db.refresh(pet)
    return pet

#DELETAR PET
@app.delete("/pets/{pet_id}")
def deletar_pet(pet_id: int, db: Session = Depends(get_db)):
    pet = db.query(models.Pet).filter(models.Pet.id == pet_id).first()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet não encontrado")
    db.delete(pet)
    db.commit()
    return {"msg": "Pet removido com sucesso"}