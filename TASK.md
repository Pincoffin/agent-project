# TASK

Upgrade the agent to support planning and reflection.

## Goals

1. Add planning phase before main loop:
   - Create core/planner.py
   - Generate plan using LLM
   - Store plan as list of steps

2. Add reflection after each action:
   - Create core/reflector.py
   - Analyze last action + result
   - Store reflection in memory

3. Modify agent_core:
   - Include TASK, PLAN, LAST RESULT in every LLM prompt
   - Inject reflection into memory
   - Use summarized results (max 500 chars)

4. Improve repetition handling:
   - Replace fallback with self_reflect tool
   - Prevent repeated action loops

5. Add new tool:
   - self_reflect in executor

## Constraints

- DO NOT rewrite existing architecture
- Extend current system only
- Maintain JSON-only outputs

## Output

- Updated agent_core.py
- New planner.py and reflector.py
- Updated executor.py
- Clean diffs only