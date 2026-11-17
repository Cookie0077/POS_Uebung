from fastapi import FastAPI
from routers.Books import router
import models


#models.Base.metadata.create_all(bind=engine)

app = FastAPI(title='Libary', description='mYaPP', version='1.0.0')
app.include_router(router)

@app.get("/")
def root():
    return {"Message": "Hello World\n Besuche /docs für die API"}

