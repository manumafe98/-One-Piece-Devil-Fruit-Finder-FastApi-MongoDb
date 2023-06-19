import base64
import requests
from fastapi import Request, Form, APIRouter, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """
    Renders the home page.

    Parameters:
    - request (Request): The incoming HTTP request object.

    Returns:
    - TemplateResponse: The response containing the rendered "index.html" template.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/", response_class=HTMLResponse)
async def home_form(request: Request, search_element: str = Form(...)):
    """
    Handles the form submission on the home page.

    Parameters:
    - request (Request): The incoming HTTP request object.
    - search_element (str): The value submitted in the form.

    Returns:
    - TemplateResponse: The response containing the rendered "devil_fruit.html" template with the devil fruit data.

    Raises:
    - N/A
    """
    devil_fruit_searched = search_element.title()
    response = requests.get(f"http://api:8000/devil_fruits/{devil_fruit_searched}")
    if response.status_code == 200:
        devil_fruit = response.json()
        image_url = devil_fruit["devil_fruit_img"]
        image_response = requests.get(image_url, stream=True)
        if image_response.status_code == 200:
            image_content = image_response.content
            base64_image = base64.b64encode(image_content).decode("utf-8")
    return templates.TemplateResponse("devil_fruit.html", {"request": request, 
                                                           "devil_fruit": devil_fruit, 
                                                           "devil_fruit_img": base64_image})


@router.get("/add", response_class=HTMLResponse)
async def add(request: Request):
    """
    Renders the add page.

    Parameters:
    - request (Request): The incoming HTTP request object.

    Returns:
    - TemplateResponse: The response containing the rendered "add.html" template.
    """
    return templates.TemplateResponse("add.html", {"request": request})


@router.post("/add", response_class=HTMLResponse)
async def add_form(request: Request, devil_fruit_name: str = Form(...), devil_fruit_type: str = Form(...), 
                   devil_fruit_image: str = Form(...), current_user: str = Form(...)):
    """
    Handles the form submission on the add page.

    Parameters:
    - request (Request): The incoming HTTP request object.
    - devil_fruit_name (str): The name of the devil fruit submitted in the form.
    - devil_fruit_type (str): The type of the devil fruit submitted in the form.
    - devil_fruit_image (str): The URL of the image submitted in the form.
    - current_user (str): The name of the current user submitted in the form.

    Returns:
    - RedirectResponse: A redirect response to the home page.

    Raises:
    - N/A
    """
    devil_fruit_params = {
        "devil_fruit_name": devil_fruit_name.title(),
        "devil_fruit_type": devil_fruit_type.title(),
        "current_user": current_user.title(),
        "devil_fruit_img": devil_fruit_image
    }
    response = requests.post("http://api:8000/devil_fruits", json=devil_fruit_params)
    redirect_url = router.url_path_for("home")
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)


@router.get("/update", response_class=HTMLResponse)
async def update(request: Request):
    """
    Renders the update page.

    Parameters:
    - request (Request): The incoming HTTP request object.

    Returns:
    - TemplateResponse: The response containing the rendered "update.html" template.
    """
    return templates.TemplateResponse("update.html", {"request": request})


@router.post("/update", response_class=HTMLResponse)
async def update_form(request: Request, devil_fruit_to_update: str = Form(...), 
                      field_to_update: str = Form(...), updated_value: str = Form(...)):
    """
    Handles the form submission on the update page.

    Parameters:
    - request (Request): The incoming HTTP request object.
    - devil_fruit_to_update (str): The name of the devil fruit to update.
    - field_to_update (str): The field to update in the devil fruit.
    - updated_value (str): The updated value for the specified field.

    Returns:
    - RedirectResponse: A redirect response to the home page.

    Raises:
    - N/A
    """
    devil_fruit_name = devil_fruit_to_update.title()
    if field_to_update != "devil_fruit_img":
        updated_value.title()
    devil_fruit_params = {f"{field_to_update}": updated_value}
    print(devil_fruit_params)
    response = requests.patch(f"http://api:8000/devil_fruits/{devil_fruit_name}"
                              , json=devil_fruit_params)
    redirect_url = router.url_path_for("home")
    return RedirectResponse(redirect_url, status_code=status.HTTP_303_SEE_OTHER)
