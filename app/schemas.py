from pydantic import BaseModel
from datetime import date

# Schema para la creación de una Radio
class RadioCreate(BaseModel):
    nombre: str

    class Config:
        from_attributes = True  # Configuración nueva

# Schema para la respuesta de los endpoints que devuelven datos de Radio
class Radio(BaseModel):
    id: int
    nombre: str

    class Config:
        from_attributes = True  # Configuración nueva

class ProgramaCreate(BaseModel):
    nombre: str
    nombre_conductor: str
    certificado_locucion: str
    url_banner: str
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class Programa(BaseModel):
    id_programa: int
    nombre: str
    nombre_conductor: str
    certificado_locucion: str
    url_banner: str

    class Config:
        from_attributes = True  # Configuración nueva

class ProgramacionCreate(BaseModel):
    nombre: str
    url_audio: str
    fecha_transmision: date
    fk_programa: int

    class Config:
        from_attributes = True  # Configuración nueva

class Programacion(BaseModel):
    id_programacion: int
    nombre: str
    url_audio: str
    fecha_transmision: date
    fk_programa: int

    class Config:
        from_attributes = True  # Configuración nueva

class ArtistaCreate(BaseModel):
    nombre: str
    informacion: str
    url_image: str
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class Artista(BaseModel):
    id_artista: int
    nombre: str
    informacion: str
    url_image: str
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class PublicidadCreate(BaseModel):
    nombre: str
    informacion: str
    url_image: str
    url_twitter: str = None
    url_instagram: str = None
    url_facebook: str = None
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

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
        from_attributes = True  # Configuración nueva

class ServicioSocialCreate(BaseModel):
    nombre: str
    informacion: str
    url_image: str
    tipo: str
    url_audio: str = None  # Opcional dependiendo del tipo
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class ServicioSocial(BaseModel):
    id_servicio: int
    nombre: str
    informacion: str
    url_image: str
    tipo: str
    url_audio: str = None
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class UsuarioCreate(BaseModel):
    nombre: str
    correo: str
    telefono: str
    password: str
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class Usuario(BaseModel):
    id_usuario: int
    nombre: str
    correo: str
    telefono: str
    fk_radio: int

    class Config:
        from_attributes = True  # Configuración nueva

class HiloMusicalCreate(BaseModel):
    nombre: str
    url_musical: str
    url_image: str
    fk_usuario: int

    class Config:
        from_attributes = True  # Configuración nueva

class HiloMusical(BaseModel):
    id_hilo: int
    nombre: str
    url_musical: str
    url_image: str
    fk_usuario: int

    class Config:
        from_attributes = True  # Configuración nueva