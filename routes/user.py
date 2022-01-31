# DEFINR TOAS LAS RUTAS QUE USAREMOS EN EL ARCHIVO , response que es una respuesta y status que es una propiedad
import re
from fastapi import APIRouter, Response, status
from config.db import conn  # importar el puntero de la base de datos
# importando los esquemas desde la car schemas
from schemas.user import userEntity, usersEntity
from models.user import User  # para importar el modelo user
from passlib.hash import sha256_crypt  # Para encriptar la contrasena
from bson import ObjectId  # Para converitr a un Object ID
# RESPUESTA DEL SISTEMA SIN CONTENIDO
from starlette.status import HTTP_204_NO_CONTENT
from typing import List

user = APIRouter()


# primera ruta
@user.get('/users',response_model=List[User], tags=["users"])
def find_all_users():
    return usersEntity(conn.local.user.find())


@user.post('/users', response_model=User,tags=["users"])
def create_users(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user['password'])
    del new_user["id"]
    id = conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id": id})
    return userEntity(user)


@user.get('/users/{id}',response_model=User,tags=["users"])
def find_user(id: str):
    return userEntity(conn.local.user.find_one({"_id": ObjectId(id)}))


@user.put('/users/{id}',response_model=User,tags=["users"])
def update_user(id: str, user: User):
    conn.local.user.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(user)}
        )
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/users/{id}',status_code=HTTP_204_NO_CONTENT,tags=["users"])
def delete_users(id: str):
    userEntity(conn.local.user.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)
