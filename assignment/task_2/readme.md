# Task 2: Audio Upload and Get Job Data API

A FastAPI application that handles audio file uploads and provides mock transcription analysis.

## Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the development server:

```bash
fastapi dev main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### 1. Upload Audio
- **URL**: `/upload_audio/`
- **Method**: `POST`
- **Parameters**:
  - `file`: Audio file (required)
  - `metadata`: Additional metadata (optional)

**Example**:
```bash
curl --request POST \
  --url http://127.0.0.1:8000/upload_audio/ \
  --header 'content-type: multipart/form-data' \
  --form file=@/media/Aion/openssource_projects/Alliance-Bioversity-Assignment/audio/q1.mp3 \
  --form 'metadata={
  "farmer_id": "F123",
  "crop": "paddy",
  "location": "Tamil Nadu",
  "timestamp": "2025-12-14T10:30:00"
}
'
```

**Response**:
```json
{
  "filename": "q1.mp3",
  "job_id": "89b6e076-a5a1-4ae1-91b7-77e786baa522",
}
```

### 2. Get Job Status
- **URL**: `/job/{job_id}`
- **Method**: `GET`
- **Parameters**:
  - `job_id`: The job ID from upload response (path parameter)

**Example**:
```bash
curl http://localhost:8000/job/550e8400-e29b-41d4-a716-446655440000
```

**Response**:
```json
{
  "job_id": "e14b1d3b-c570-41d0-8b27-3d7becc42683",
  "transcription": "The paddy leaves are turning yellow in some patches. I also noticed a few insects on the lower leaves. Water level is normal. What should I do?",
  "analysis": {
    "problem_type": [
      "crop_health",
      "pest"
    ],
    "severity": "moderate",
    "possible_causes": [
      "nutrient deficiency",
      "pest attack"
    ],
    "sentiment": "concerned"
  },
  "keywords": [
    "paddy",
    "yellow leaves",
    "insects",
    "lower leaves",
    "water level normal"
  ],
  "follow_up_questions": [
    "Are the insects visible on many plants or only a few?",
    "When did the yellowing start?"
  ]
}
```

## Key Technologies

- **FastAPI**: Modern Python web framework for building APIs
- **Uvicorn**: ASGI server for running the application
- **Python 3.8+**: Programming language

## Notes

- Uploaded files are stored in the `uploads/` directory
- Job IDs are generated using UUID for unique identification

## Things to consider beyond the scope of this assignment

- folder architecture that seperate api route, schemeas and business logic
- API versioning to support future changes without breaking clients
- Open API contract to clearly communicate between different stakeholder including mobile, backend and ML team

## Future Enhancements

- Integrate real speech-to-text service (e.g., Google Cloud Speech-to-Text)
- Implement database for persistent job storage
- Add authentication and authorization
- Implement real AI-based analysis
- Add file cleanup and storage management
- Support for multiple audio formats and languages
