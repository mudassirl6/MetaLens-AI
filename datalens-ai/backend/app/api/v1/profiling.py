from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def profile_dataset():
    """
    Placeholder endpoint — performs dataset profiling.
    """
    return {"message": "Dataset profiling will appear here"}
