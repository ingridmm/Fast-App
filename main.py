from http import HTTPStatus

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from schemas import UserSchema
from auth import authenticate_user, create_access_token, get_current_user
from database import SessionLocal, UserDB

app = FastAPI()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/login')
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        return {"error": "E-mail ou Senha incorretos"}

    access_token = create_access_token(data={"sub": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post('/users', status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    db_user = UserDB(
        nome=user.nome,
        email=user.email,
        cpf=user.cpf,
        data_nascimento=user.data_nascimento
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "Usuário cadastrado com sucesso!", "user": db_user}

@app.get('/users', status_code=HTTPStatus.OK)
def list_users(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    users = db.query(UserDB).all()
    return {"users": users}

