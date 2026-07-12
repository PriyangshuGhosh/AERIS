from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST", "0.0.0.0")

PORT = int(os.getenv("PORT", 8000))

MODEL_REPO = os.getenv(
    "MODEL_REPO",
    "bartowski/Phi-3.5-mini-instruct-GGUF"
)

MODEL_FILE = os.getenv(
    "MODEL_FILE",
    "Phi-3.5-mini-instruct-Q4_K_M.gguf"
)

CONTEXT_LENGTH = int(
    os.getenv("CONTEXT_LENGTH", 4096)
)

TEMPERATURE = float(
    os.getenv("TEMPERATURE", 0.7)
)

MAX_TOKENS = int(
    os.getenv("MAX_TOKENS", 300)
)

GPU_LAYERS = int(
    os.getenv("GPU_LAYERS", -1)
)

LOG_REQUESTS = (
    os.getenv("LOG_REQUESTS", "true").lower()
    == "true"
)