# Model pins for managed-agent cookbooks

Every cookbook manifest (`agent.yaml` and `subagents/*.yaml`) sets an explicit `model` field. Cookbooks pin the same Opus-tier snapshot so scheduled runs stay reproducible across deploys.

| Field | Current value |
|---|---|
| Default model | `claude-opus-4-8` |

## Why explicit pins

Claude model IDs without a date suffix (for example `claude-opus-4-8`) are **pinned snapshots**, not evergreen pointers to "latest Opus." See [Model IDs and versioning](https://docs.claude.com/en/docs/about-claude/models/overview#model-ids-and-versioning) in the Claude Platform docs.

Cookbooks use explicit pins so:

- Platform teams can re-run evals against a known model before bumping the pin.
- Orchestrator and leaf workers stay on the same tier unless you deliberately split them.
- A stale-looking ID is a signal to review — not an accident. Bump the pin here when you have re-validated the cookbook on a newer snapshot.

## Overriding at deploy time

Your deploy pipeline may substitute a different `model` value when posting to `POST /v1/agents`. The manifests in this repo document the reference pin the cookbooks were written and smoke-tested against.
