# servicio_social.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import ServicioSocial as ServicioSocialModel
from app.schemas import ServicioSocialCreate, ServicioSocial
from typing import List

router = APIRouter(
    prefix="/servicio_social",
    tags=["Servicios Sociales"]
)

@router.post('/', response_model=ServicioSocial)
def crear_servicio_social(servicio: ServicioSocialCreate, db: Session = Depends(get_db)):
    nuevo_servicio = ServicioSocialModel(**servicio.dict())
    db.add(nuevo_servicio)
    db.commit()
    db.refresh(nuevo_servicio)
    return nuevo_servicio

@router.get('/', response_model=List[ServicioSocial])
def obtener_servicios_sociales(db: Session = Depends(get_db)):
    servicios = db.query(ServicioSocialModel).all()
    return servicios

@router.get('/{servicio_id}', response_model=ServicioSocial)
def obtener_servicio_social_por_id(servicio_id: int, db: Session = Depends(get_db)):
    servicio = db.query(ServicioSocialModel).filter(ServicioSocialModel.id_servicio == servicio_id).first()
    if servicio is None:
        raise HTTPException(status_code=404, detail="Servicio social no encontrado")
    return servicio

@router.put('/{servicio_id}', response_model=ServicioSocial)
def actualizar_servicio_social(servicio_id: int, servicio: ServicioSocialCreate, db: Session = Depends(get_db)):
    servicio_db = db.query(ServicioSocialModel).filter(ServicioSocialModel.id_servicio == servicio_id).first()
    if servicio_db is None:
        raise HTTPException(status_code=404, detail="Servicio social no encontrado")
    for key, value in servicio.dict().items():
        setattr(servicio_db, key, value)
    db.commit()
    db.refresh(servicio_db)
    return servicio_db

@router.delete('/{servicio_id}', response_model=dict)
def eliminar_servicio_social(servicio_id: int, db: Session = Depends(get_db)):
    servicio_db = db.query(ServicioSocialModel).filter(ServicioSocialModel.id_servicio == servicio_id).first()
    if servicio_db is None:
        raise HTTPException(status_code=404, detail="Servicio social no encontrado")
    db.delete(servicio_db)
    db.commit()
    return {"mensaje": "Servicio social eliminado satisfactoriamente"}
