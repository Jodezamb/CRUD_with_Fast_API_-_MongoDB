from turtle import title
from fastapi import FastAPI
from routes.user import user # importar desde el moduo carptea router y modulo user

app = FastAPI(
    title=" REST API with FastApi and MongoDB",
    description="This is a simple REST API with FastAPI and MongoDB By: Jose Adrian Delgado Zambrano",
    version="0.0.1",
    
    

)

app.include_router(user)