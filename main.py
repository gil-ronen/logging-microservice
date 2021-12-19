from fastapi import FastAPI
from starlette.responses import RedirectResponse
import schema
from database import SessionLocal, engine
import model
from fastapi import FastAPI, Depends, Request
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse
from typing import Any, Dict, AnyStr, List, Union

app = FastAPI()
model.Base.metadata.create_all(bind=engine)

def get_database_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "welcome to FastAPI!"}

@app.get("/log/")
async def read_logs(request: Request, db: Session = Depends(get_database_session)):
    logs = db.query(model.Log).all()
    return logs

@app.post("/log/")
async def create_log(request: Request, db: Session = Depends(get_database_session)):
    logRequest = await request.json()
    logModel = model.Log(asctime = logRequest["asctime"], name = logRequest["name"], levelname = logRequest["levelname"], message = logRequest["message"])
    db.add(logModel)
    db.commit()
    response = RedirectResponse('/', status_code=303)
    return response
