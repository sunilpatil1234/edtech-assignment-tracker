from fastapi import APIRouter, Form
from models import Assignment
from database import SessionLocal

router = APIRouter()

@router.post("/assignments/create")
def create_assignment(
    title: str = Form(...),
    description: str = Form(...),
    due_date: str = Form(...)
):
    db = SessionLocal()
    assignment = Assignment(title=title, description=description, due_date=due_date)
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return {"message": "Assignment created successfully", "assignment": assignment}
