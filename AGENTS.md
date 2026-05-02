# AGENTS.md

## Project Overview
This is a local AI agent system built using:
- Ollama (local LLM backend)
- Modular Python architecture
- Tool-based execution system
- Memory + critic loop

The goal is to create an autonomous agent capable of:
- Executing tasks
- Using tools
- Evaluating results
- Iterating toward completion

---

## Architecture

Core modules:

- core/
  - agent_core.py (main loop)
  - executor.py (runs tools)
  - critic.py (evaluates actions)
  - memory.py (stores events)

- tools/
  - dynamically loaded tools

- config/
  - model + runtime settings

---

## Rules

1. DO NOT remove existing working logic unless necessary
2. Prefer modifying existing files over creating new ones
3. Keep functions small and testable
4. Maintain compatibility with Ollama API (http://localhost:11434)
5. NEVER hardcode secrets or API keys
6. All outputs must be valid JSON when required
7. Fix bugs BEFORE adding new features

---

## Dev Commands

Run agent:
python run.py

Install deps:
pip install -r requirements.txt

---

## Coding Style

- Python 3.10+
- No unnecessary abstractions
- Clear logging for all actions
- Avoid global state where possible

---

## Priority

1. Stability of agent loop
2. Correct tool execution
3. Memory reliability
4. Then new features

---

## Notes for Codex

The correct entry point is run.py.
Do not create or use main.py.

If unsure:
- Inspect existing files first
- Preserve current architecture
- Ask for clarification ONLY if blocked

Otherwise:
→ proceed with implementation