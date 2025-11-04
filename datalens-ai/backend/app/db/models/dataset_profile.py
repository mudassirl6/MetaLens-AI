from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, JSON
from sqlalchemy.sql import func
from app.core.database import Base

class DatasetProfile(Base):
    __tablename__ = "dataset_profiles"

    id = Column(Integer, primary_key=True, index=True)
    dataset_id = Column(Integer, ForeignKey("datasets.id", ondelete="CASCADE"), nullable=False)
    rows = Column(Integer)
    columns = Column(Integer)
    missing_rate = Column(Float)
    dtype_distribution = Column(JSON)      # {"int":5, "float":2, "object":3}
    numeric_summary = Column(JSON)         # {"price":{"mean":...}}
    schema_hash = Column(String(64))
    profiled_at = Column(DateTime(timezone=True), server_default=func.now())
