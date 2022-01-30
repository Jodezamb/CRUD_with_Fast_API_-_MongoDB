from fastapi import FastAPI
from routes.user import user # importar desde el moduo carptea router y modulo user

app = FastAPI()

app.include_router(user)