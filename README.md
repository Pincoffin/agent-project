
# Local AI Agent System

This is a local-first AI agent built on Ollama.

## Model

Default model:
- Qwen2.5-Coder-7B-Instruct (GGUF, quantized build by bartowski)

## Runtime

- Local inference via [Ollama](https://ollama.com)
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