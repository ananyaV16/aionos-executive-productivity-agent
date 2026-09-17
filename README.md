# AIONOS Executive Productivity Agent

A local, deterministic executive productivity product for Arjun Malhotra, VP Sales. It turns supplied meeting, email, voice-note, and calendar facts into an evidence-grounded daily action brief.

## Features

- Premium Streamlit command center, daily brief, deadlines, calendar, timeline, traceability, and demo mode.
- Deduplicated Vendor List with three supporting mentions.
- Evidence-driven overdue, completed, confirmed, scheduled, and unclear-ownership states.
- Grounded natural-language workspace queries and unsupported-question handling.
- No API key, live integrations, or runtime LLM required.

## Run locally

```powershell
python -m pip install -r requirements.txt
streamlit run app.py
```

Run checks with `python -m pytest -q`.

## Architecture

`data_pack.py` holds Data-Pack-only facts; `services.py` supplies deterministic reasoning and Q&A; `app.py` is the UI. See architecture.md, DATA_LINEAGE.md, and assumptions.md.

## Limitations

This assignment build uses the fixed supplied Data Pack, not live integrations. A production version could add authenticated ingestion, review queues, audit controls, and optional retrieval while retaining evidence requirements.
