---
name: antigravity-multiagent
description: Use when orchestrating native multi-agent workflows in Antigravity (CLI, 2.0 Desktop, IDE), dispatching Gemini Pro Lead Architect with Gemini Flash or Flash-Lite worker subagents, managing isolated workspace branching, or delegating tasks via the 3-Route Framework.
---

# Antigravity Multi-Agent Orchestration Skill

Provides the protocol, schemas, and automation patterns for running high-efficiency multi-agent workflows inside Google Antigravity across all three surfaces: **Antigravity CLI (`agy`)**, **Antigravity 2.0 (Desktop App)**, and **Antigravity IDE**.

## 1. Core Architecture: Pro Orchestrator + Flash Workers

```
                    ┌────────────────────────────────────────┐
                    │    Lead Architect (Gemini Pro)         │
                    │  Planning, System Design, Diff Review  │
                    └───────────────────┬────────────────────┘
                                        │
             ┌──────────────────────────┼──────────────────────────┐
             ▼                          ▼                          ▼
 ┌───────────────────────┐  ┌───────────────────────┐  ┌───────────────────────┐
 │ Explorer/Investigator │  │ Default Executor      │  │ Tester                │
 │ Model: flash          │  │ Model: flash          │  │ Model: flash          │
 │ Sandbox: read-only    │  │ Workspace: 'branch'   │  │ Test flags: terse     │
 │ Tools: QMD/Serena/CTX │  │ Produces diff only    │  │ 2-strike stop rule    │
 └───────────────────────┘  └───────────────────────┘  └───────────────────────┘
```

- **Token & Cost Efficiency**: Routes repetitive boilerplate, multi-file searches, test suite execution, and AST updates to **Gemini Flash** (~10× cheaper/faster) or **Flash-Lite** (~20× cheaper), saving >90% of Pro's context window.
- **Workspace Branching**: Workers executing code changes run with `Workspace: "branch"`, ensuring experimental code remains in an isolated git branch and never pollutes the developer's main branch until verified.

---

## 2. The 3-Route Framework

### Light Route (Default)
- Direct inline execution by Gemini Pro.
- Best for: Quick single-turn queries, clarifying questions, and surgical 1–2 file patches.
- Overhead: 0 subagents dispatched.

### Medium Route
- Lead Architect (Pro) creates the implementation plan and handles code changes.
- Dispatches read-only workers (`Model: "flash"`) to explore dependencies or diagnose errors.
- Dispatches `archivist` (`Model: "flash"`) to update session ledgers.
- Best for: Tasks where reading 5–15 files would otherwise bloat the main conversation context.

### Heavy Route (3× Token Saver)
- Lead Architect (Pro) acts strictly as Knowledge Architect / Lead Reviewer.
- Formulates a self-contained **Task Capsule** and delegates:
  1. `explorer` / `investigator` (Flash, read-only) -> gathers facts and citations.
  2. `default_executor` (Flash, `Workspace: "branch"`) -> produces working tree diff in isolated branch.
  3. `tester` (Flash, `pytest -q --tb=short`) -> runs regression checks with 2-strike stop rule.
  4. `archivist` (Flash) -> updates `CONTINUITY.md` and `HANDOFF.md`.
- Lead Architect inspects `git diff`, merges branch, and commits to main.

---

## 3. Subagent Catalog & Invocation Patterns

### A. Codebase Explorer (Read-Only)
```json
{
  "Subagents": [
    {
      "TypeName": "research",
      "Role": "Codebase Explorer",
      "Model": "flash",
      "Workspace": "inherit",
      "Prompt": "### Task Capsule: EXP-001\n- Scope: Map all references to shots.py and list callers.\n- Tools: Use Serena find_referencing_symbols and Codebase-Memory search_graph.\n- Output: Concise path:line citations only."
    }
  ]
}
```

### B. Isolated Code Implementer (Branch Mode)
```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Feature Implementer",
      "Model": "flash",
      "Workspace": "branch",
      "Prompt": "### Task Capsule: IMP-002\n- Scope: src/youtube_automation/production/shots.py\n- Goal: Add new duration validator for interactive exercise grids.\n- Constraints: Produce working tree diff only. NEVER run git commit or git push.\n- Guidance: Obey 2-strike loop brake on syntax errors."
    }
  ]
}
```

### C. Independent Tester (Terse Shell)
```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Test Verification Engineer",
      "Model": "flash",
      "Workspace": "inherit",
      "Prompt": "### Task Capsule: TST-003\n- Scope: tests/unit/production/test_shots.py\n- Command: Run pytest -q --tb=short tests/unit/production/test_shots.py\n- Invariant: 2-strike stop rule. If test fails twice consecutively, stop and report 2-sentence summary."
    }
  ]
}
```

### D. Archivist (DOX Framework Protector)
```json
{
  "Subagents": [
    {
      "TypeName": "self",
      "Role": "Session Archivist",
      "Model": "flash",
      "Workspace": "inherit",
      "Prompt": "### Task Capsule: ARC-004\n- Scope: docs/short-term-plan/CONTINUITY.md & docs/sessions/HANDOFF.md\n- Goal: Record completed milestone and next steps.\n- STRICT PROHIBITION: NEVER create or edit agent_docs/. All documentation stays in docs/."
    }
  ]
}
```

---

## 4. Antigravity UI & Surface Features

- **Antigravity 2.0 Desktop**:
  - Open the **Auxiliary Pane** on the right side.
  - Switch to the **Subagents** tab to view live cards for all running subagents, their current tool executions, and status (`running`, `idle`, `waiting_for_input`).
  - View proposed file modifications in the **Files Changed** tab.
- **Antigravity CLI (`agy`)**:
  - Dispatched subagents run asynchronously in the background.
  - The CLI automatically handles reactive wakeups when subagents report back.
- **Antigravity IDE**:
  - Autocomplete runs via Tab in editor.
  - Complex background subagents operate without interrupting active typing.

## 5. Verification Checklist

```bash
# Verify Python test runner under terse flags
pytest -q --tb=short tests/unit

# Check git status for uncommitted subagent diffs
git status --short
git diff --stat
```

## Keywords
Keywords: antigravity, subagent, invoke_subagent, define_subagent, multi-agent, gemini-pro, gemini-flash, branch-workspace, 3-route, task-capsule, auxiliary-pane

