from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

router = APIRouter()
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), '../../../frontend'))

@router.get("/register", response_class=HTMLResponse)
async def get_register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})