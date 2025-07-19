from fastapi import APIRouter, UploadFile, File, Form

router = APIRouter()

@router.post("/submit-assignment")
async def submit_assignment(
    assignment_id: int = Form(...),
    answer: str = Form(...),
    avatar: UploadFile = File(None)
):
    if avatar:
        contents = await avatar.read()
        with open(f"avatars/{avatar.filename}", "wb") as f:
            f.write(contents)
    return {
        "message": "Assignment submitted",
        "assignment_id": assignment_id,
        "answer": answer,
        "avatar_uploaded": bool(avatar)
    }
