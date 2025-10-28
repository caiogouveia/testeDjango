from ninja import NinjaAPI
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .schemas import (
    UserSchema, 
    UserCreateSchema, 
    UserUpdateSchema,
    SuccessSchema
)

api = NinjaAPI(
    title="Users API",
    version="1.0.0",
    description="API para gerenciamento de usuários"
)

# GET - Listar todos os usuários
@api.get("/users", response=list[UserSchema], tags=["Users"])
def list_users(request):
    """
    Lista todos os usuários cadastrados
    """
    users = User.objects.all()
    return users

# GET - Buscar usuário por ID
@api.get("/users/{user_id}", response=UserSchema, tags=["Users"])
def get_user(request, user_id: int):
    """
    Busca um usuário específico por ID
    """
    user = get_object_or_404(User, id=user_id)
    return user

# POST - Criar novo usuário
@api.post("/users", response=UserSchema, tags=["Users"])
def create_user(request, payload: UserCreateSchema):
    """
    Cria um novo usuário
    """
    user = User.objects.create_user(
        username=payload.username,
        email=payload.email,
        password=payload.password,
        first_name=payload.first_name or "",
        last_name=payload.last_name or ""
    )
    return user

# PUT - Atualizar usuário
@api.put("/users/{user_id}", response=UserSchema, tags=["Users"])
def update_user(request, user_id: int, payload: UserUpdateSchema):
    """
    Atualiza os dados de um usuário
    """
    user = get_object_or_404(User, id=user_id)
    
    if payload.username is not None:
        user.username = payload.username
    if payload.email is not None:
        user.email = payload.email
    if payload.first_name is not None:
        user.first_name = payload.first_name
    if payload.last_name is not None:
        user.last_name = payload.last_name
    
    user.save()
    return user

# PATCH - Atualizar parcialmente
@api.patch("/users/{user_id}", response=UserSchema, tags=["Users"])
def partial_update_user(request, user_id: int, payload: UserUpdateSchema):
    """
    Atualiza parcialmente os dados de um usuário
    """
    return update_user(request, user_id, payload)

# DELETE - Deletar usuário
@api.delete("/users/{user_id}", response=SuccessSchema, tags=["Users"])
def delete_user(request, user_id: int):
    """
    Remove um usuário do sistema
    """
    user = get_object_or_404(User, id=user_id)
    username = user.username
    user.delete()
    return {
        "success": True, 
        "message": f"Usuário '{username}' deletado com sucesso"
    }

# GET - Buscar usuário por username
@api.get("/users/username/{username}", response=UserSchema, tags=["Users"])
def get_user_by_username(request, username: str):
    """
    Busca um usuário pelo nome de usuário
    """
    user = get_object_or_404(User, username=username)
    return user

# GET - Health check
@api.get("/health", tags=["System"])
def health_check(request):
    """
    Verifica se a API está funcionando
    """
    return {"status": "ok", "message": "API está funcionando!"}
