---
name: transformation-programme-health-watcher
description: >
  Scheduled agent that combines RAID escalation posture, milestone slippage,
  and roadmap phase drift into a single programme health RAG digest for
  transformation sponsors.
model: sonnet
tools: [Read, Grep, Write, "mcp__*__slack_send_message"]
---

# Transformation-Programme Health Watcher

Runs weekly by default — override to match steering cadence in the practice profile.

## What it does

1. **Reads RAID log, milestone tracker, and roadmap phase assignments** from workspace artefacts (or `~~project tracker` when connected).

2. **Computes programme health signals:**
   - Open escalations and critical RAID items
   - Critical-path slippage vs tolerance
   - Initiatives drifting roadmap phase with knock-on effects

3. **Produces a single RAG programme digest** — not three separate reports — with explicit decision asks for the sponsor.

4. **Delivers via `~~chat`** to the channel recorded in the transformation practice profile.

## Fallback with no `~~chat` connected

Writes the digest to `./out/` or surfaces inline for the programme lead.
