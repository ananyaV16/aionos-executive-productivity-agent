# AIONOS Executive Productivity Agent

> An evidence-grounded AI productivity workspace that turns fragmented executive communications into clear actions, deadlines, ownership signals, and decision-ready briefs.

**Built for:** AIONOS Agentic AI Factory — Assignment 1  
**User:** Arjun Malhotra, VP Sales  
**Scenario:** Week of 21–25 September 2026

---

## Overview

Executives often receive commitments and follow-ups across meetings, emails, voice notes, and calendars. Important actions can become buried, deadlines can shift, and ownership can remain unclear.

The **Executive Productivity Agent** consolidates these fragmented inputs into a single workspace that helps an executive answer:

- What do I need to do?
- What is overdue?
- What am I waiting on?
- What changed?
- Who owns this?
- What needs my attention today?
- What evidence supports this conclusion?

The system is designed around **evidence-first reasoning**: it uses only the supplied Data Pack, preserves source provenance, and avoids inventing ownership or completion status.

---

## ✨ Key Capabilities

### Commitment Intelligence
- Extracts executive commitments from meetings, emails, and voice notes
- Identifies the latest commitment and deadline
- Deduplicates repeated mentions of the same commitment
- Tracks commitment evolution over time

### Deadline Intelligence
- Detects open and overdue commitments
- Reconciles revised deadlines
- Separates completed work from unresolved work
- Connects commitments with relevant calendar events

### Ownership Intelligence
- Distinguishes **My Actions**, **Waiting on Others**, and **Unclear Ownership**
- Never assigns an owner without supporting evidence
- Explicitly flags unresolved ownership for follow-up

### Evidence & Traceability
Every important classification can be traced back to:
- Source
- Supporting evidence
- Classification rationale
- Commitment history

### Executive Q&A
The workspace supports grounded questions such as:

> "What did I promise Raghav?"

> "What's overdue?"

> "Who owns the Mumbai lease?"

> "What changed this week?"

> "What needs action today?"

Responses include supporting evidence and source information.


## Application Views

The Streamlit workspace includes:

- **Executive Dashboard**
- **Daily Action Brief**
- **My Actions**
- **Waiting on Others**
- **Deadlines / Overdue**
- **Unclear Ownership**
- **Commitment Timeline**
- **Calendar Context**
- **Ask the Executive Workspace**
- **Demo Mode**
- **Sources & Method**
---

## 🧠 Architecture

```text
Input Sources
     ↓
Structured Ingestion
     ↓
Commitment Extraction
     ↓
Entity Resolution
     ↓
Deadline Normalization
     ↓
Deduplication
     ↓
Status Engine
     ↓
Ownership Classification
     ↓
Calendar Correlation
     ↓
Evidence & Provenance
     ↓
Executive Brief + Q&A
