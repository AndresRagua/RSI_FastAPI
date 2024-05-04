# radio.py: Rutas y controladores relacionados con las operaciones del modelo Radio.
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Radio as RadioModel
from app.schemas import RadioCreate, Radio  # Asumiendo que tienes un esquema para crear radios

router = APIRouter(
    prefix="/radio",
    tags=["Radios"]
)

@router.post('/agregar', response_model=Radio)
def crear_radio(radio: RadioCreate, db: Session = Depends(get_db)):
    new_radio = RadioModel(nombre=radio.nombre)
    db.add(new_radio)
    db.commit()
    db.refresh(new_radio)
    return new_radio

@router.get('/obtener', response_model=List[Radio])
def obtener_radios(db: Session = Depends(get_db)):
    radios = db.query(RadioModel).all()
    return radios

@router.get('/{radio_id}', response_model=Radio)
def obtener_radio_id(radio_id: int, db: Session = Depends(get_db)):
    radio = db.query(RadioModel).filter(RadioModel.id == radio_id).first()
    if radio is None:
        raise HTTPException(status_code=404, detail="Radio no encontrada")
    return radio

@router.put('/{radio_id}', response_model=Radio)
def actualizar_radio(radio_id: int, radio: RadioCreate, db: Session = Depends(get_db)):
    radio_db = db.query(RadioModel).filter(RadioModel.id == radio_id).first()
    if radio_db is None:
        raise HTTPException(status_code=404, detail="Radio no encontrada")
    radio_db.nombre = radio.nombre
    db.commit()
    db.refresh(radio_db)
    return radio_db

@router.delete('/{radio_id}', response_model=dict)
def eliminar_radio(radio_id: int, db: Session = Depends(get_db)):
    radio_db = db.query(RadioModel).filter(RadioModel.id == radio_id).first()
    if radio_db is None:
        raise HTTPException(status_code=404, detail="Radio no encontrada")
    db.delete(radio_db)
    db.commit()
    return {"mensaje": "Radio eliminada satisfactoriamente"}

# Asumimos que tienes un schema RadioCreate para crear radios y Radio para el output
