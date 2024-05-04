# usuario.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Usuario as UsuarioModel
from app.schemas import UsuarioCreate, Usuario
from typing import List

router = APIRouter(
    prefix="/usuario",
    tags=["Usuarios"]
)

@router.post('/', response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    nuevo_usuario = UsuarioModel(**usuario.dict())
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get('/', response_model=List[Usuario])
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioModel).all()
    return usuarios

@router.get('/{usuario_id}', response_model=Usuario)
def obtener_usuario_por_id(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.put('/{usuario_id}', response_model=Usuario)
def actualizar_usuario(usuario_id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_db = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == usuario_id).first()
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    for key, value in usuario.dict().items():
        setattr(usuario_db, key, value)
    db.commit()
    db.refresh(usuario_db)
    return usuario_db

@router.delete('/{usuario_id}', response_model=dict)
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario_db = db.query(UsuarioModel).filter(UsuarioModel.id_usuario == usuario_id).first()
    if usuario_db is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    db.delete(usuario_db)
    db.commit()
    return {"mensaje": "Usuario eliminado satisfactoriamente"}
