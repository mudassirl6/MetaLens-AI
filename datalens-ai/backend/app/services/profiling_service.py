import pandas as pd, hashlib
from sqlalchemy.orm import Session
from app.db.models.dataset_profile import DatasetProfile

def profile_dataset(db: Session, dataset_id: int, file_path: str):
    df = pd.read_csv(file_path)
    df = pd.read_csv(file_path)
    if df.empty:
        raise ValueError("Uploaded CSV is empty or unreadable")

    rows, cols = df.shape

    missing_rate = float(df.isna().sum().sum()) / (rows * cols) if rows and cols else 0
    dtype_distribution = {str(k): int(v) for k, v in df.dtypes.value_counts().items()}

    numeric_summary = {
        col: df[col].describe().to_dict()
        for col in df.select_dtypes(include="number").columns
    }

    schema_hash = hashlib.sha256(str(list(df.columns)).encode()).hexdigest()

    profile = DatasetProfile(
        dataset_id=dataset_id,
        rows=rows,
        columns=cols,
        missing_rate=missing_rate,
        dtype_distribution=dtype_distribution,
        numeric_summary=numeric_summary,
        schema_hash=schema_hash,
    )

    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile
