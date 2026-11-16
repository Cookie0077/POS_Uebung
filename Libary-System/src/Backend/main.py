from fastapi import FastAPI
import Tierheim_Flask.routers.animals as animals
from Tierheim_Flask.database import engine
import Tierheim_Flask.models as models


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Tierheim', description='mYaPP', version='1.0.0')
app.include_router(animals.router)

@app.get("/")
def root():
    return {"Message": "Hello World\n Besuche /docs für die API"}

