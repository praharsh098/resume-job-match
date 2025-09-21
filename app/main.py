from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from app.matcher import Matcher

app = FastAPI(title='Resume Job Matcher')
matcher = Matcher()

class MatchRequest(BaseModel):
    resume_text: str
    top_k: int = 5

class JobResult(BaseModel):
    id: str
    title: str
    company: str
    location: str
    description: str
    score: float


@app.post('/match', response_model=List[JobResult])
def match(req: MatchRequest):
    if not req.resume_text.strip():
        raise HTTPException(status_code=400, detail='Empty resume text')
    results = matcher.match(req.resume_text, top_k=req.top_k)
    return results


@app.get('/')
def root():
    return {'status': 'ok', 'msg': 'Resume Job Matcher API'}

