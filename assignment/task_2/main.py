import json
import os
import uuid

from fastapi import FastAPI, File, Form, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()


UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)

status = {}


@app.post("/upload_audio/")
async def upload_audio(file: UploadFile, metadata: str = Form(...)):

    try:
        metadata_dict = json.loads(metadata)
    except json.JSONDecodeError as e:
        return JSONResponse(
            status_code=400,
            content={
                "error": "Invalid metadata JSON",
                "details": str(e)
            }
        )
    job_id = str(uuid.uuid4())

    if not file.filename.endswith((".wav", ".mp3", ".m4a")):
        return JSONResponse(status_code=400, content={
            "error": "Invalid file format."})
    filepath = os.path.join(UPLOAD_DIR, f"{job_id}_{file.filename}")

    with open(filepath, "wb") as f:
        f.write(await file.read())
    status[job_id] = {"filepath": filepath,
                      "metadata": metadata_dict, }
    return {"filename": file.filename,
            "job_id": job_id, }


@app.get("/job/{job_id}")
async def get_job_status(job_id: str):

    if (job_id not in status):
        return JSONResponse(status_code=404, content={"error": "Job ID not found"})

    transcription = "The paddy leaves are turning yellow in some patches. I also noticed a few insects on the lower leaves. Water level is normal. What should I do?"
    keywords = ["paddy", "yellow leaves", "insects",
                "lower leaves", "water level normal"]
    analytics = {
        "problem_type": ["crop_health", "pest"],
        "severity": "moderate",
        "possible_causes": ["nutrient deficiency", "pest attack"],
        "sentiment": "concerned"
    }
    follow_up_questions = [
        "Are the insects visible on many plants or only a few?",
        "When did the yellowing start?"
    ]
    return {"job_id": job_id,
            "transcription": transcription,
            "analysis": analytics,
            "keywords": keywords,
            "follow_up_questions": follow_up_questions
            }
