from fastapi import  APIRouter #  DEFINR TOAS LAS RUTAS QUE USAREMOS EN EL ARCHIVO 
from config.db import  conn  #importar el puntero de la base de datos 
from schemas.user import userEntity,usersEntity # importando los esquemas desde la car schemas
from models.user import User
from passlib.hash import sha256_crypt



user=APIRouter()


#primera ruta
@user.get('/users')
def find_all_users():
    return usersEntity(conn.local.user.find())

@user.post('/users')
def create_users(user: User):
    new_user=dict(user)
    new_user["password"]=sha256_crypt.encrypt(new_user['password'])
    del new_user["id"]
    id= conn.local.user.insert_one(new_user).inserted_id
    user = conn.local.user.find_one({"_id":id})
    return userEntity(user)
    

@user.get('/users/{id}')
def find_user():
    return 'Hellow world'

@user.put('/users/{id}')
def update_user():
    return 'Hellow world'

@user.delete('/users/{id}')
def delete_users():
    return 'Hellow world'

