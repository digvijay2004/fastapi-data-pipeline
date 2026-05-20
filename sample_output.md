# Sample API Outputs

## Create Record
**POST /records/**
```json
{
  "name": "Sales Data Pipeline",
  "description": "Daily sales aggregation",
  "status": "active"
}
```
**Response:**
```json
{
  "id": 1,
  "name": "Sales Data Pipeline",
  "description": "Daily sales aggregation",
  "status": "active",
  "created_at": "2026-05-18T10:00:00"
}
```

## Get All Records
**GET /records/**
```json
[
  {
    "id": 1,
    "name": "Sales Data Pipeline",
    "status": "active"
  },
  {
    "id": 2,
    "name": "User Analytics Pipeline",
    "status": "inactive"
  }
]
```

## API Documentation
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc