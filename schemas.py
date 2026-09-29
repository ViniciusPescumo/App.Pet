from pydantic import BaseModel

class PetCreate(BaseModel):
    nome_pet:str
    especie:str
    raca:str
    bloco:str
    apartamento:str
    nome_tutor:str
    telefone_tutor:str

class PetResponse(PetCreate):
    id:int
    class config:
        from_atributes = True
