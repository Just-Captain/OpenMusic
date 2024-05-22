from fastapi import Request, APIRouter
from fastapi.templating import Jinja2Templates


router = APIRouter() 
templates = Jinja2Templates(directory='templates')

@router.get('/')
def get_main_page(request: Request):
    return templates.TemplateResponse(request=request, name='index.html')