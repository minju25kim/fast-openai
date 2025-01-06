from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from summarize import openai_summarize
from gemini import genai_generate

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LinkRequest(BaseModel):
    link: str


@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}


@app.post("/summarize")
async def summarize(request: LinkRequest):
    summary = await openai_summarize(request.link)
    return summary


@app.get("/generate")
async def generate():
    summary = await genai_generate()
    response = {"summary": summary}
    return response
