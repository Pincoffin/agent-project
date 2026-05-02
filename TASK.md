# TASK

Fix and stabilize the agent loop.

## Goals

1. Ensure agent_core loop works reliably:
   - No crashes
   - Handles invalid JSON from LLM
   - Always produces an action or fallback

2. Fix JSON parsing issues:
   - Extract valid JSON from LLM responses
   - Ignore malformed outputs safely

3. Improve tool execution:
   - Ensure correct tool is selected
   - Validate arguments before execution

4. Improve logging:
   - Log every step:
     - LLM response
     - Parsed action
     - Tool execution
     - Result
     - Critic feedback

5. Add retry logic:
   - If LLM output is invalid → retry once

---

## Constraints

- DO NOT rewrite the entire system
- Keep architecture intact
- Improve robustness only

---

## Output

- Updated files only
- Clean diffs
- Working agent loop