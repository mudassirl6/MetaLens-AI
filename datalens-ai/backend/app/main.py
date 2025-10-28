

from fastapi import FastAPI
from app.api.v1 import datasets,profiling,lineage
from app.core.logger import get_logger


#initialize fastapi app
app = FastAPI(
    title="DataLens AI",
    version="1.0.0",
    description="Backend API for DataLens AI – Smart Data Profiling and Lineage Analysis"

)


# Setup logging
logger = get_logger()

#Include API routers
app.include_router(datasets.router,prefix="/api/v1/datasets",tags=["Datasets"])
app.include_router(profiling.router, prefix="/api/v1/profiling", tags=["Profiling"])
app.include_router(lineage.router, prefix="/api/v1/lineage", tags=["lineage"])


@app.get("/", tags=["Health"])
def root():
    """Health check endpoint"""
    logger.info("Root endpoint called")
    return {"message": "Welcome to DataLens AI Backend!"}
