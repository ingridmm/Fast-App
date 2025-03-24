import re
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    nome: str
    email: EmailStr
    cpf: str = Field(pattern=r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
    data_nascimento: str = Field(pattern=r'^\d{4}-\d{2}-\d{2}$')

#ideal p/ segurança:por não retornar a senha do usuário
class UserPublic(BaseModel):
    nome: str
    email: str

