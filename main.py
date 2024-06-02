from fastapi import FastAPI, HTTPException
import uvicorn
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import home, radio, programa, programacion, artista, publicidad, servicio, usuario, hilo
from app.db.database import Base, engine

def create_tables():
    Base.metadata.create_all(bind=engine)
create_tables()

app = FastAPI()

# Monta el directorio de archivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configura el directorio para las plantillas Jinja2
templates = Jinja2Templates(directory="templates")

app.include_router(radio.router)
app.include_router(programa.router)
app.include_router(programacion.router)
app.include_router(artista.router)
app.include_router(publicidad.router)
app.include_router(servicio.router)
app.include_router(usuario.router)
app.include_router(hilo.router)
app.include_router(home.router)



## Ejecutar la aplicacion con "python main.py"
if __name__ == "__main__":
    uvicorn.run("main:app",port=8000,reload=True)