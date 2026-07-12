# ARIES – Local Phi-3.5 AI Inference Server

<p align="center">

A lightweight local AI inference server built on **Microsoft Phi-3.5 Mini** using **llama.cpp**, **FastAPI**, and **Python**.

Designed for offline conversational AI and integrated with the **GAAC (GITAM Aero Astro Club)** assistant.

</p>

---

## Features

- Local inference using **Microsoft Phi-3.5 Mini**
- Automatic model download from Hugging Face
- FastAPI REST API
- Swagger API documentation
- Automatic virtual environment creation
- Cross-platform (Windows, Linux)
- Configurable inference parameters
- Request logging
- Runtime statistics
- Health monitoring endpoints
- Production-ready project structure

---

## Repository Structure

```text
ARIES/

├── utils/
│   ├── helpers.py
│   ├── logger.py
│   └── stats.py
│
├── .env.example
├── .gitignore
├── banner.py
├── config.py
├── model_loader.py
├── requirements.txt
├── run.py
├── server.py
├── startup.py
├── README.md
├── LICENSE
├── run.bat
└── run.sh
```

---

# Requirements

## Operating System

- Windows 10 / 11
- Ubuntu 22.04+
- Other Linux distributions
- macOS (should work but not officially tested)

---

## Software

- Python 3.10 or newer
- Git
- Internet connection (required only for the initial model download)

---

## Hardware

Minimum

- Quad-core CPU
- 8 GB RAM

Recommended

- Intel i5 / Ryzen 5 or better
- 16 GB RAM
- SSD Storage

GPU acceleration is optional.

---

# Installation

Clone the repository

```bash
git clone https://github.com/<YOUR_USERNAME>/ARIES.git

cd ARIES
```

---

# Running the Server

## Windows

Simply double-click

```
run.bat
```

or

```cmd
python run.py
```

---

## Linux

```bash
python3 run.py
```

or

```bash
./run.sh
```

---

# Automatic Setup

The launcher automatically performs the following tasks:

- Creates a virtual environment
- Installs required Python packages
- Creates a local configuration file
- Downloads the Phi-3.5 Mini model (first launch only)
- Loads the model into memory
- Starts the FastAPI server

No manual installation of the model is required.

---

# Model

The server automatically downloads

**Microsoft Phi-3.5 Mini Instruct (GGUF)**

Repository

bartowski/Phi-3.5-mini-instruct-GGUF

Quantization

```
Q4_K_M
```

The model is downloaded only once and cached by Hugging Face.

---

# API Endpoints

## Root

```
GET /
```

Returns

```json
{
    "status":"running",
    "model":"Phi-3.5 Mini",
    "uptime":"00:03:12"
}
```

---

## Health

```
GET /health
```

Returns server status.

---

## Configuration

```
GET /config
```

Returns current inference configuration.

---

## Statistics

```
GET /stats
```

Returns

- uptime
- request count
- average latency
- CPU threads

---

## Chat Completion

```
POST /generate
```

Example request

```json
{
    "prompt":"Tell me about GAAC."
}
```

Example response

```json
{
    "response":"GAAC is the official GITAM Aero Astro Club dedicated to aerospace innovation and hands-on engineering.",
    "latency":1.84
}
```

---

# Swagger Documentation

After launching the server

Open

```
http://127.0.0.1:8000/docs
```

Interactive API documentation will be available.

---

# Configuration

Server settings can be modified through the environment file.

Example

```text
HOST=0.0.0.0

PORT=8000

CONTEXT_LENGTH=4096

TEMPERATURE=0.7

MAX_TOKENS=300

GPU_LAYERS=-1
```

---

# Logging

Logs are automatically stored in

```
logs/server.log
```

The log includes

- request timestamps
- inference latency
- server startup events
- runtime errors

---

# Integrating with Other Applications

The server exposes a standard REST API and can easily be integrated into web applications, desktop applications, robotics systems, or embedded AI assistants.

Example

```http
POST http://127.0.0.1:8000/generate
```

---

# Development

Install manually

```bash
pip install -r requirements.txt
```

Run directly

```bash
python server.py
```

---

# Troubleshooting

## Model download fails

Verify your internet connection and rerun

```bash
python run.py
```

---

## Port already in use

Change the port inside

```
.env
```

or

```
config.py
```

---

## Slow inference

CPU inference speed depends on the processor.

For improved performance

- Close unnecessary applications
- Use SSD storage
- Use an NVIDIA GPU (if available)

---

# Future Improvements

- Conversation memory
- Streaming responses
- OpenAI-compatible API
- GPU acceleration improvements
- Docker support
- Authentication
- Multi-model support

---

# License

This project is released under the MIT License.

See the LICENSE file for details.

---

# Acknowledgements

- Microsoft Research (Phi-3.5 Mini)
- llama.cpp
- llama-cpp-python
- Hugging Face
- FastAPI

---

## Author

**Pragyanshu Ghosh**

B.Tech Computer Science (AI & ML)

GITAM University

Research Interests

- Artificial Intelligence
- Computer Vision
- Embedded AI
- Aerospace AI
- Human–Computer Interaction

---

If you use this project in your own work, a citation or acknowledgement is appreciated.
