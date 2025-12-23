from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def root():
    return {"status": "API is running"}

@app.post("/generate-video")
def generate_video(data: PromptRequest):
    return {
        "message": "Video generation started",
        "prompt_received": data.prompt,
        "video_url": "https://example.com/video.mp4"
    }

