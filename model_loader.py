import os
import time

from huggingface_hub import hf_hub_download

from llama_cpp import Llama

from config import *

MODEL = None


def load_model():

    global MODEL

    if MODEL is not None:

        return MODEL

    print("[4/5] Checking Model Cache...\n")

    start = time.time()

    model_path = hf_hub_download(

        repo_id=MODEL_REPO,

        filename=MODEL_FILE

    )

    print("Model Location")

    print(model_path)

    print()

    print("[5/5] Loading Phi-3.5 Mini...\n")

    MODEL = Llama(

        model_path=model_path,

        n_ctx=CONTEXT_LENGTH,

        n_gpu_layers=GPU_LAYERS,

        n_threads=os.cpu_count(),

        verbose=False

    )

    elapsed = time.time() - start

    print()

    print("✓ Model Loaded Successfully")

    print(f"Load Time : {elapsed:.2f} seconds")

    print()

    return MODEL