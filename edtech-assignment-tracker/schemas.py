from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# -------------------- User Models --------------------

class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    name: str
    password: str
    role: str  # "student" or "teacher"


class UserLogin(UserBase):
    password: str


class UserOut(UserBase):
    id: int
    name: str
    role: str

    model_config = {
        "from_attributes": True
    }


# -------------------- Assignment Models --------------------

class AssignmentBase(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: datetime


class AssignmentCreate(AssignmentBase):
    pass


class AssignmentOut(AssignmentBase):
    id: int
    created_by: int

    model_config = {
        "from_attributes": True
    }


# -------------------- Submission Models --------------------

class SubmissionBase(BaseModel):
    content: str
    file_url: Optional[str] = None


class SubmissionCreate(SubmissionBase):
    assignment_id: int


class SubmissionOut(SubmissionBase):
    id: int
    assignment_id: int
    submitted_by: int
    submitted_at: datetime

    model_config = {
        "from_attributes": True
    }
