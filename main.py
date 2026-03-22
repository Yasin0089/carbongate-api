from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI(title="CarbonGate API")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])
@app.get("/health")
def health():
    return {"status":"ok","version":"1.0"}
@app.get("/")
def root():
    return {"message":"CarbonGate Engine API Live"}
