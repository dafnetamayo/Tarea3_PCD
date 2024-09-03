from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from typing import List
import models
import database as bd

 
 
 
app = FastAPI()
 
models.Base.metadata.create_all(bind=bd.engine)
 
def get_db():
    try:
        db = bd.SessionLocal()
        yield db
    finally:
        db.close()
 
class UserCreate(BaseModel):
    user_name: str   
    user_email: str
    age: int
    recommendations: List[str] = []  
    zip_code: int
 
@app.get("/")
async def mostrar_usuarios(db:Session = Depends(get_db)):
    return db.query(models.Usuarios).all()
 
@app.post("/")
async def crear_usuario(user: UserCreate, db: Session =Depends(get_db)):
    correo_en_uso = db.query(models.Usuarios).filter(models.Usuarios.user_email == user.user_email).first()
    if correo_en_uso:
        raise HTTPException(status_code=400, detail="Ya existe este correo")
    
    #crear usuario
    user_model = models.Usuarios(
        user_name = user.user_name,
        user_email = user.user_email,
        age = user.age,
        zip_code = user.zip_code
    )

    user_model.set_recommendations(user.recommendations)

    db.add(user_model)
    db.commit()
    db.refresh(user_model)

    return{"Usuario creado" : user_model}

@app.put("/{user_id}")
async def actualizar_usuario(user_id:int, user:UserCreate, db:Session = Depends(get_db)):
    usuario = db.query(models.Usuarios).filter(models.Usuarios.user_id == user_id).first()
 
    if not usuario:
        raise HTTPException(status_code=404, detail="No existe el usuario")
    
    usuario.user_name = user.user_name
    usuario.user_email = user.user_email
    usuario.age = user.age
    usuario.set_recommendations(user.recommendations)
    usuario.zip_code = user.zip_code
 
    db.commit()
    db.refresh(usuario)
 
    return {"Se editó correctamente"}
    

@app.get("/{user_id}")
async def mostrar_datos_usuarios(user_id: int, db:Session = Depends(get_db)):
    return db.query(models.Usuarios).filter(models.Usuarios.user_id == user_id).first()

@app.delete("/{user_id}")
async def borrar_usuario(user_id:int, db:Session = Depends(get_db)):
    usuario = db.query(models.Usuarios).filter(models.Usuarios.user_id == user_id).first()

    if not usuario:
        raise HTTPException(status_code=404, detail= "No existe el usuario")
    
    db.commit()
    db.refresh(usuario)

    return{"Status" : "Se borró el usuario"}
 