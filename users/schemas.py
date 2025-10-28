from ninja import Schema
from typing import Optional
from datetime import datetime

# Schema para retornar dados do usuário
class UserSchema(Schema):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    date_joined: datetime

# Schema para criar usuário
class UserCreateSchema(Schema):
    username: str
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None

# Schema para atualizar usuário
class UserUpdateSchema(Schema):
    username: Optional[str] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

# Schema para resposta de sucesso
class SuccessSchema(Schema):
    success: bool
    message: str
