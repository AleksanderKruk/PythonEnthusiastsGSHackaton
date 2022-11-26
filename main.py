from uvicorn import run
from fastapi import FastAPI, Form
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")


@app.get('/login')
async def get_login(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "id": id})


@app.post('/login')
async def post_login(email=Form(), password=Form()):
    #
    # body = await request.json()
    #
    # email, password = body['email'], body['password']

    if not email or not password:
        return "Missing field in login form"

    return f'Email: {email}/ password: {password}'


if __name__ == '__main__':
    run('main:app', port=8080, reload=True)
