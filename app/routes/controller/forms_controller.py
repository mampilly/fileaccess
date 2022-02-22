# new additional imports

from email import header
from fastapi import status, APIRouter, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.routes.service.forms_service import read_csv

router = APIRouter()

templates = Jinja2Templates(directory="app/templates/")


@router.post("/example")
async def example(request: Request):
    form_data = await request.form()
    return form_data


@router.get('/')
def read_form():
    return 'hello world'


@router.get("/form")
def form_post(request: Request):
    result = "Type a number"
    return templates.TemplateResponse('form.html', context={'request': request, 'result': result})


@router.post("/form", response_class=RedirectResponse)
async def form_post(request: Request):
    form_data = await request.form()
    first_name = form_data.get("fname")
    second_name = form_data.get("lname")
    data_exist = read_csv(first_name, second_name)
    if data_exist:
        return RedirectResponse(
            '/found',
            status_code=status.HTTP_302_FOUND)

    else:
        return RedirectResponse(
            '/notfound',
            status_code=status.HTTP_302_FOUND)


@router.get("/found")
async def get_resp(request: Request):
    return templates.TemplateResponse('datafound.html', context={'request': request})


@router.get("/notfound")
async def get_resp(request: Request):
    return templates.TemplateResponse('noresult.html', context={'request': request})
