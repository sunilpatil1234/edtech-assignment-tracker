from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import os

from database import Base, engine, get_db
from models import User
from schemas import UserCreate
from auth import get_password_hash
from routers import users, assignments, submissions

# Create necessary directories for static files
os.makedirs("static", exist_ok=True)
os.makedirs("src", exist_ok=True)

# Initialize FastAPI app
app = FastAPI()

# Mount static directory
app.mount("/", StaticFiles(directory="static", html=True), name="static")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(users.router)
app.include_router(assignments.router)
app.include_router(submissions.router)

# Root API endpoint
@app.get("/api")
def root():
    return {"message": "Welcome to EdTech Assignment Tracker"}

# Signup endpoint
@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    hashed_password = get_password_hash(user.password)
    db_user = User(
        username=user.username,
        hashed_password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully"}
