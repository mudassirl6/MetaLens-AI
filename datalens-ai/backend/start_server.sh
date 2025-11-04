#!/bin/bash
# =======================================================================
# 🚀 DataLens AI - FastAPI Backend Startup Script
# Author: Mudassir Ahmed (DataLens AI Project)
# =======================================================================

# Function to display colored messages
info() { echo -e "\033[1;34m[INFO]\033[0m $1"; }
success() { echo -e "\033[1;32m[SUCCESS]\033[0m $1"; }
error() { echo -e "\033[1;31m[ERROR]\033[0m $1"; }

# 1️⃣ Resolve project root dynamically
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

info "Project root detected: $PROJECT_ROOT"

# 2️⃣ Activate Conda environment
CONDA_ENV="datalens-ai"
if command -v conda &> /dev/null; then
    source ~/anaconda3/etc/profile.d/conda.sh
    conda activate $CONDA_ENV
    success "Activated conda environment: $CONDA_ENV"
else
    error "Conda not found. Please install or activate manually."
    exit 1
fi

# 3️⃣ Set PYTHONPATH so FastAPI can import the 'app' package
export PYTHONPATH=$PROJECT_ROOT
info "PYTHONPATH set to: $PYTHONPATH"

# 4️⃣ Check if database exists, create if missing
DB_PATH="$PROJECT_ROOT/datalens.db"
if [ ! -f "$DB_PATH" ]; then
    info "Database not found. Initializing..."
    python - <<EOF
from app.core.database import Base, engine
from app.db.models import dataset
Base.metadata.create_all(bind=engine)
print("✅ Database created successfully at $DB_PATH")
EOF
    success "Database initialized successfully."
else
    info "Database already exists at: $DB_PATH"
fi

# 5️⃣ Start the FastAPI server
info "Starting FastAPI backend on http://127.0.0.1:8000"
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
