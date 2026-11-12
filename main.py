from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException, Path, status
from sqlalchemy.orm import Session
import model
from model import Todos
from database import engine, SessionLocal
from pydantic import BaseModel, Field
from routers import auth,todos, admin,users

app = FastAPI()

model.Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)



