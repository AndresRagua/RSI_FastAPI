# app/routers/home_router.py

from fastapi import APIRouter, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

router = APIRouter()

# Monta el directorio de archivos estáticos
router.mount("/static", StaticFiles(directory="static"), name="static")

# Monta el directorio de archivos estáticos
templates = Jinja2Templates(directory="templates")

@router.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})
