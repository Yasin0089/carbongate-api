

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from anthropic import Anthropic
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "CarbonGate Engine API Live"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": request.message}]
    )
    return {"response": response.content[0].text}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from anthropic import Anthropic
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "CarbonGate Engine API Live"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": request.message}]
    )
    return {"response": response.content[0].text}

from pydantic import BaseModel
from anthropic import Anthropic

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

class ChatRequest(BaseModel):
    message: str

