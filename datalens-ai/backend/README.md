backend/
├── app/
│   ├── api/v1/           → FastAPI routers for datasets, profiling, lineage
│   ├── core/             → Config, logging, constants
│   ├── db/               → Database base, models, and session
│   ├── ml/               → ML modules (column classification, quality checks)
│   ├── schemas/          → Pydantic schemas for request/response models
│   ├── services/         → Business logic layer
│   ├── tests/            → Unit/integration tests (to fill next)
│   └── main.py           → Entry point for FastAPI app
├── requirements.txt
└── README.md
