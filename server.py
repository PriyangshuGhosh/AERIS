import time
import signal
import sys
import os

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Local modules
from config import *
from startup import startup_checks
from model_loader import load_model
from utils.logger import logger
import utils.stats as stats

############################################################
# Startup
############################################################

startup_checks()

llm = load_model()

############################################################
# FastAPI
############################################################

app = FastAPI(
    title="GAAC AI Local Server",
    description="Local Phi-3.5 Mini Inference Server",
    version="1.0.0"
)

############################################################
# Default System Prompt
############################################################

SYSTEM_PROMPT = """
You are AERIS (Aeronautical & Astronautical Engineering Representative & Induction Steward),
the official AI representative of GITAM Aero Astro Club (GAAC).

Your target audience is first-year university students interested in aerospace.

Your personality is elegant, cinematic, calm, modern, and trustworthy.

Keep responses concise (2–3 short paragraphs).

Avoid markdown.

Speak naturally.

If you do not know something, honestly say that you do not know.
"""

############################################################
# Request Model
############################################################

class ChatRequest(BaseModel):
    prompt: str
    system_prompt: str | None = None

############################################################
# Root Endpoint
############################################################

@app.get("/")
def root():

    return {
        "status": "running",
        "model": MODEL_FILE,
        "uptime": stats.uptime()
    }

############################################################
# Health Endpoint
############################################################

@app.get("/health")
def health():

    return {
        "status": "healthy",
        "requests": stats.REQUEST_COUNT,
        "uptime": stats.uptime()
    }

############################################################
# Configuration Endpoint
############################################################

@app.get("/config")
def configuration():

    return {
        "model": MODEL_FILE,
        "context_length": CONTEXT_LENGTH,
        "temperature": TEMPERATURE,
        "max_tokens": MAX_TOKENS,
        "gpu_layers": GPU_LAYERS,
        "threads": os.cpu_count()
    }

############################################################
# Statistics Endpoint
############################################################

@app.get("/stats")
def statistics():

    return {
        "uptime": stats.uptime(),
        "requests": stats.REQUEST_COUNT,
        "average_latency": stats.average_latency(),
        "threads": os.cpu_count()
    }

############################################################
# Chat Generation Endpoint
############################################################

@app.post("/generate")
def generate(req: ChatRequest):

    start = time.time()

    try:

        system_prompt = req.system_prompt or SYSTEM_PROMPT

        output = llm.create_chat_completion(

            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": req.prompt
                }
            ],

            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS

        )

        reply = output["choices"][0]["message"]["content"]

        latency = time.time() - start

        stats.record_request(latency)

        if LOG_REQUESTS:

            logger.info(
                f"Prompt='{req.prompt[:60]}' | "
                f"Latency={latency:.2f}s"
            )

        return {
            "response": reply,
            "latency": round(latency, 3)
        }

    except Exception as e:

        logger.exception(e)

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

############################################################
# Graceful Shutdown
############################################################

def shutdown(sig, frame):

    print()
    print("=" * 60)
    print("Stopping Server...")
    print("Saving Logs...")
    print("Goodbye!")
    print("=" * 60)

    sys.exit(0)

signal.signal(signal.SIGINT, shutdown)

############################################################
# Main
############################################################

if __name__ == "__main__":

    print()
    print("=" * 60)
    print("Server Ready")
    print()
    print(f"API         : http://127.0.0.1:{PORT}")
    print(f"Swagger UI  : http://127.0.0.1:{PORT}/docs")
    print(f"Health      : http://127.0.0.1:{PORT}/health")
    print(f"Config      : http://127.0.0.1:{PORT}/config")
    print(f"Statistics  : http://127.0.0.1:{PORT}/stats")
    print("=" * 60)

    uvicorn.run(
        app,
        host=HOST,
        port=PORT
    )