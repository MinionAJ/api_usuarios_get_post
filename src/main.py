from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src import models, database, schemas

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/usuarios")
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    novo_usuario = models.Usuario(**usuario.model_dump())
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

@app.get("/usuario")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(models.Usuario).all()