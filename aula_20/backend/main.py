import models
from database import engine
from fastapi import FastAPI
from router import router

# Cria todas as tabelas definidas no models
models.Base.metadata.create_all(bind=engine)

# Cria a aplicação FastAPI
app = FastAPI()

# Inclui as rotas definidas no router
app.include_router(router)
