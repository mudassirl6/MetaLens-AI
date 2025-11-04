from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Optional

class DatasetProfileBase(BaseModel):
    rows: Optional[int]
    columns: Optional[int]
    missing_rate: Optional[float]
    dtype_distribution: Optional[Dict[str, int]]
    numeric_summary: Optional[Dict[str, Dict[str, float]]]
    schema_hash: Optional[str]

class DatasetProfileResponse(DatasetProfileBase):
    id: int
    dataset_id: int
    profiled_at: datetime

    class Config:
        from_attributes = True   # pydantic-v2 replacement for orm_mode
