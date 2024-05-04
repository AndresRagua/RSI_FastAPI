from pydantic import BaseModel
from datetime import date

# Schema para la creación de una Radio
class RadioCreate(BaseModel):
    nombre: str

# Schema para la respuesta de los endpoints que devuelven datos de Radio
class Radio(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class ProgramaCreate(BaseModel):
    nombre: str
    nombre_conductor: str
    certificado_locucion: str
    url_banner: str
    fk_radio: int

class Programa(BaseModel):
    id_programa: int
    nombre: str
    nombre_conductor: str
    certificado_locucion: str
    url_banner: str

    class Config:
        orm_mode = True

class ProgramacionCreate(BaseModel):
    nombre: str
    url_audio: str
    fecha_transmision: date
    fk_programa: int

class Programacion(BaseModel):
    id_programacion: int
    nombre: str
    url_audio: str
    fecha_transmision: date
    fk_programa: int

    class Config:
        orm_mode = True

class ArtistaCreate(BaseModel):
    nombre: str
    informacion: str
    url_image: str
    fk_radio: int

class Artista(BaseModel):
    id_artista: int
    nombre: str
    informacion: str
    url_image: str
    fk_radio: int

    class Config:
        orm_mode = True

class PublicidadCreate(BaseModel):
    nombre: str
    informacion: str
    url_image: str
    url_twitter: str = None
    url_instagram: str = None
    url_facebook: str = None
    fk_radio: int

class Publicidad(BaseModel):
    id_publicidad: int
    nombre: str
    informacion: str
    url_image: str
    url_twitter: str
    url_instagram: str
    url_facebook: str
    fk_radio: int

    class Config:
        orm_mode = True

class ServicioSocialCreate(BaseModel):
    nombre: str
    informacion: str
    url_image: str
    tipo: str
    url_audio: str = None  # Opcional dependiendo del tipo
    fk_radio: int

class ServicioSocial(BaseModel):
    id_servicio: int
    nombre: str
    informacion: str
    url_image: str
    tipo: str
    url_audio: str = None
    fk_radio: int

    class Config:
        orm_mode = True

class UsuarioCreate(BaseModel):
    nombre: str
    correo: str
    telefono: str
    password: str
    fk_radio: int

class Usuario(BaseModel):
    id_usuario: int
    nombre: str
    correo: str
    telefono: str
    fk_radio: int

    class Config:
        orm_mode = True

class HiloMusicalCreate(BaseModel):
    nombre: str
    url_musical: str
    url_image: str
    fk_usuario: int

class HiloMusical(BaseModel):
    id_hilo: int
    nombre: str
    url_musical: str
    url_image: str
    fk_usuario: int

    class Config:
        orm_mode = True