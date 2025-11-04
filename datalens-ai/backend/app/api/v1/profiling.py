from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.profiling_service import profile_dataset
from app.schemas.profile_schema import DatasetProfileResponse
from app.db.models.dataset import Dataset
import os

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/{dataset_id}", response_model=DatasetProfileResponse)
async def upload_and_profile(
    dataset_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)
):
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")

    UPLOAD_DIR = "uploads"
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    contents = await file.read()
    print(f"[DEBUG] received {len(contents)} bytes")
    if not contents:
        raise HTTPException(status_code=400, detail="Empty upload")
    with open(file_path, "wb") as f:
        f.write(contents)
    print(f"[DEBUG] wrote file to {file_path} ({os.path.getsize(file_path)} bytes)")

    try:
        profile = profile_dataset(db, dataset_id, file_path)
        return profile
    except Exception as e:
        import traceback
        print("[ERROR] profiling failed:", e)
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

