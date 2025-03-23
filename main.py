from http import HTTPStatus

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm

from schemas import UserSchema, UserPublic
from auth import authenticate_user, create_access_token, get_current_user

app = FastAPI()

@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return {"error": "E-mail ou Senha incorretos"}

    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post('/users', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema, current_user: dict = Depends(get_current_user)):
    return {"message": "Usuário cadastrado com sucesso!", "user": user}

'''
@app.get('/users/', response_model=UserList)
def read_users():
    return {'user': UserList}
'''