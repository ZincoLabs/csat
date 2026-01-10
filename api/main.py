from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, conint
from supabase_client import insert_survey

app = FastAPI()

class SurveyRequest(BaseModel):
    q1: conint(ge=1, le=5)
    q2: conint(ge=1, le=5)
    q3: conint(ge=1, le=5)
    q4: conint(ge=1, le=5)
    comentarios: str | None = None

@app.post("/submit-survey")
def submit_survey(payload: SurveyRequest):
    try:
        insert_survey(payload.dict())
        return {"status": "ok"}
    except Exception:
        raise HTTPException(status_code=500, detail="Error saving survey")
