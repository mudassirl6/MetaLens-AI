from pydantic import BaseModel, Field

class DatasetBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str | None = None

class DatasetCreate(DatasetBase):
    pass

class DatasetResponse(DatasetBase):
    id: int

    class Config:
        orm_mode = True  # Enables SQLAlchemy model → Pydantic conversion
