# Local AI Agent System

This is a local-first AI agent built on Ollama.

## Model

Default model:
- :contentReference[oaicite:0]{index=0} (GGUF, quantized build by bartowski)

Runs locally via:
- :contentReference[oaicite:1]{index=1}

## Runtime

- Local inference via Ollama
- Model served at http://localhost:11434

## Features

- Tool execution
- Memory storage
- Critic feedback loop
- Autonomous task iteration

## Run

python run.py

## Goal

Build a reliable autonomous agent that:
- Takes a task
- Plans actions
- Executes tools
- Evaluates results
- Iterates

## Status

⚠️ Currently unstable — needs loop + parsing fixes