from sqlalchemy.orm import Session
from models import User, Assignment, Submission
from schemas import UserCreate, AssignmentCreate, SubmissionCreate
from utils import get_password_hash  # NOT from auth.py anymore



# --------------------------
# USER CRUD
# --------------------------

def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password,
        role=user.role
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# --------------------------
# ASSIGNMENT CRUD
# --------------------------

def create_assignment(db: Session, assignment: AssignmentCreate, teacher_id: int):
    db_assignment = Assignment(
        title=assignment.title,
        description=assignment.description,
        due_date=assignment.due_date,
        teacher_id=teacher_id
    )
    db.add(db_assignment)
    db.commit()
    db.refresh(db_assignment)
    return db_assignment

def get_all_assignments(db: Session):
    return db.query(Assignment).all()

def get_assignment_by_id(db: Session, assignment_id: int):
    return db.query(Assignment).filter(Assignment.id == assignment_id).first()

# --------------------------
# SUBMISSION CRUD
# --------------------------

def create_submission(db: Session, submission: SubmissionCreate, student_id: int):
    db_submission = Submission(
        assignment_id=submission.assignment_id,
        student_id=student_id,
        content=submission.content,
        file_url=submission.file_url
    )
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission

def get_submissions_by_assignment(db: Session, assignment_id: int):
    return db.query(Submission).filter(Submission.assignment_id == assignment_id).all()
