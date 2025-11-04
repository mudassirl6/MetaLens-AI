from sqlalchemy.orm import Session
from app.db.models.dataset import Dataset
from app.schemas.dataset_schema import DatasetCreate

def create_dataset(db: Session, dataset_in: DatasetCreate):
    dataset = Dataset(name=dataset_in.name, description=dataset_in.description)
    db.add(dataset)
    db.commit()
    db.refresh(dataset)
    return dataset

def get_all_datasets(db: Session):
    return db.query(Dataset).all()

def get_dataset_by_id(db: Session, dataset_id: int):
    return db.query(Dataset).filter(Dataset.id == dataset_id).first()
