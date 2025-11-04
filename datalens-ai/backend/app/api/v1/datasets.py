from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.dataset_schema import DatasetCreate, DatasetResponse
from app.db.models.dataset import Dataset

router = APIRouter()

@router.get("/", response_model=List[DatasetResponse])
def list_datasets(db: Session = Depends(get_db)):
    """
    Fetch all datasets from the database.
    """
    datasets = db.query(Dataset).all()
    return datasets

@router.get("/{dataset_id}", response_model=DatasetResponse)
def get_dataset(dataset_id: int, db: Session = Depends(get_db)):
    """
    Fetch a single dataset by ID.
    """
    dataset = db.query(Dataset).filter(Dataset.id == dataset_id).first()
    if not dataset:
        raise HTTPException(status_code=404, detail="Dataset not found")
    return dataset

@router.post("/", response_model=DatasetResponse, status_code=status.HTTP_201_CREATED)
def create_dataset(dataset_in: DatasetCreate, db: Session = Depends(get_db)):
    """
    Add a new dataset entry to the database.
    """
    # Check if name already exists
    existing = db.query(Dataset).filter(Dataset.name == dataset_in.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Dataset with this name already exists")

    new_dataset = Dataset(name=dataset_in.name, description=dataset_in.description)
    db.add(new_dataset)
    db.commit()
    db.refresh(new_dataset)
    return new_dataset
