from http import HTTPStatus

from fastapi import FastAPI

from schemas import UserSchema, UserPublic

app = FastAPI()

@app.post('/users', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return {"message":"Usuário cadastrado com sucesso!", "user": user}