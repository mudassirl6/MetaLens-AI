from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_lineage():
    """
    Placeholder endpoint — returns data lineage info.
    """
    return {"message": "Data lineage information will appear here"}
