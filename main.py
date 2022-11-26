import datetime

from uvicorn import run
import sqlite3 as sql
from database import user_utility
from fastapi import FastAPI, Form
from fastapi.requests import Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from database.schema.submission import Submission

app = FastAPI()
conn = sql.connect('database/gs.db')

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="static")


@app.get('/')
async def root():
    return RedirectResponse('/login', status_code=303)


@app.get('/login')
async def get_login(request: Request):
    return templates.TemplateResponse('login.html', {'request': request, 'id': id})


@app.post('/login')
async def post_login(email=Form(), password=Form()):
    res = user_utility.login(email, password, conn)
    if res is None:
        RedirectResponse('/login', status_code=401)
    print(res)
    header = {'Set-Cookie': f'token={res}'}
    return RedirectResponse('/home', headers=header, status_code=303)


@app.get('/register')
async def get_register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request, "id": id})


@app.post('/register')
async def post_register(email=Form(), username=Form(), password=Form()):
    res = user_utility.register(username, email, password, conn)
    if not res:
        return RedirectResponse('/register', status_code=303)

    return RedirectResponse('/login', status_code=303)


@app.get('/home')
async def get_home(request: Request):
    token = request.cookies.get('token')
    print(f'From /home {token}')
    res = user_utility.validate_token(token, conn)
    print(res)
    q = 'SELECT * FROM challenges'
    challenges = conn.execute(q).fetchall()
    print(len(challenges))

    if res is None:
        return RedirectResponse('/login', status_code=303)

    return templates.TemplateResponse("home.html", {"request": request, "id": id, "content": challenges})

@app.get('/challenge/{id}')
async def get_challenge(id: str, request: Request):
    q = 'SELECT * FROM challenges WHERE id=?'
    challenge = conn.execute(q, (id,)).fetchone()

    if challenge is None:
        return RedirectResponse('/home', status_code=303)
    print(challenge)
    return templates.TemplateResponse("challenge.html", {"request": request, "id": id, "challenge": challenge})


@app.post('/challenge/{id}')
async def get_challenge(id: str, request: Request, submission=Form()):
    q = 'SELECT * FROM challenges WHERE id=?'
    challenge = conn.execute(q, (id,)).fetchone()

    if challenge is None:
        return RedirectResponse('/home', status_code=303)

    # update punktów na danym użytkowniku w DB
    ####
    token = request.cookies.get('token')
    res = list(user_utility.validate_token(token, conn))
    res[4] += 1
    q = 'UPDATE users SET points=? WHERE id=?'
    conn.execute(q, (res[4], res[0]))

    # wstawianie submisssion
    s = Submission(user_id=res[0], challenge_id=id, posting_iso=str(datetime.datetime.now()), text=submission)
    s.insert(conn)
    conn.commit()

    # wraca do home'a (z ewentualnym dodatkowym komunikatem
    return RedirectResponse('/home', status_code=303)

if __name__ == '__main__':
    try:
        run('main:app', port=8080, reload=True)
    except KeyboardInterrupt as r:
        conn.commit()
        raise r
