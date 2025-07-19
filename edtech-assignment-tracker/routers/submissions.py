from fastapi import APIRouter, Form
from models import Submission
from database import SessionLocal

router = APIRouter()

@router.post("/submissions/submit")
def submit_assignment(
    assignment_id: int = Form(...),
    student_name: str = Form(...),
    answer: str = Form(...)
):
    db = SessionLocal()
    submission = Submission(assignment_id=assignment_id, student_name=student_name, answer=answer)
    db.add(submission)
    db.commit()
    db.refresh(submission)
    return {"message": "Submission successful", "submission": submission}
