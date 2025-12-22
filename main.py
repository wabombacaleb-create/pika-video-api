from fastapi import FastAPI
from pydantic import BaseModel
import fal_client

app = FastAPI()

class Request(BaseModel):
    prompt: str

@app.post("/generate-video")
def generate_video(req: Request):
    result = fal_client.subscribe(
        "fal-ai/pika/v2.2/text-to-video",
        input={"prompt": req.prompt}
    )
    return {
        "video_url": result["data"]["video"]["url"]
    }
