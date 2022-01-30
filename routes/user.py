from fastapi import  APIRouter #  DEFINR TOAS LAS RUTAS QUE USAREMOS EN EL ARCHIVO 

user=APIRouter()


#primera ruta
@user.get('/users')
def find_all_users():
    return 'Hellow world'

@user.post('/users')
def create_users():
    return 'Hellow world'

@user.get('/users/{id}')
def find_user():
    return 'Hellow world'

@user.put('/users/{id}')
def update_user():
    return 'Hellow world'

@user.delete('/users/{id}')
def delete_users():
    return 'Hellow world'

