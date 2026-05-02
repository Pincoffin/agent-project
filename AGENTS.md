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

## File Placement Rules

- All new files must be created in the repository root or correct subfolder
- NEVER use /workspace paths
- NEVER create nested project directories
- cli_chat.py must be in the repository root

---

## Git Commit & Push Rules (MANDATORY)

After making ANY file changes:

1. Ensure correct branch:
   git branch --show-current
   (must be "main")

2. Stage changes:
   git add .

3. Commit changes:
   git commit -m "<clear description of changes>"

4. Push to remote:
   git push origin main

5. VERIFY:
   - Confirm that the updated files exist in the GitHub repository
   - Confirm the commit appears in the commit history
   - Do not finish the task unless verified

Failure to push is considered an incomplete task.

---

## File Creation Verification

After creating a file:
- Confirm the file exists in the repository root or intended directory
- Confirm the file is tracked by git
- Confirm the file is visible in GitHub after push

---

## Environment Constraints

- NEVER use /workspace paths in commands
- NEVER run git -C /workspace/...
- All commands must be run relative to repository root

---

## Error Handling

- If any git command fails, STOP and fix it
- Do not continue after a failed commit or push
- Do not assume success without verification

---

## Priority

1. Stability of agent loop
2. Correct tool execution
3. Memory reliability
4. Then new features

---

## Completion Criteria

A task is NOT complete unless:
- Files are committed
- Files are pushed
- Files are visible in GitHub

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