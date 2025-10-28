from fastapi import APIRouter, HTTPException
from app.schemas.dataset_schema import DatasetCreate, DatasetResponse

router = APIRouter()

@router.get("/", response_model=list[DatasetResponse])
async def list_datasets():
    return [{"id": 1, "name": "Sample Dataset", "description": "Example entry"}]

@router.post("/", response_model=DatasetResponse)
async def create_dataset(dataset: DatasetCreate):
    return {"id": 1, **dataset.model_dump()}
