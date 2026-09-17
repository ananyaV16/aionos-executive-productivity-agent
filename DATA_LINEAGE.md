# Data Lineage

This document describes how information moves through the Executive Productivity Agent from the supplied Data Pack to the final dashboard, brief, timeline, and Q&A outputs.

## 1. Input

The supplied Data Pack PDF is the sole business-data source.

It contains:
- Meeting transcripts
- Email threads
- Voice-note transcripts
- Calendar information

## 2. Extraction

Relevant facts are structured in `data_pack.py` as:

- Commitments
- Sources
- Event history
- Calendar events
- Owners
- Stakeholders
- Deadlines
- Current status

## 3. Normalization

Dates, commitments, deadlines, stakeholders, and ownership information are represented using a consistent structure so that information from different sources can be compared.

## 4. Deduplication

Repeated references to the same commitment are consolidated into a single record.

For example, the **Vendor List** commitment combines evidence from:

- Leadership Sync
- Vendor List email thread
- Voice Note 1

This prevents the same executive commitment from appearing as multiple tasks.

## 5. Status Calculation

Commitment status is determined from the available evidence, including:

- Explicit completion
- Follow-up messages
- Revised deadlines
- Confirmations
- Missing completion evidence

A missing completion message is **not** treated as proof of completion.

## 6. Ownership Classification

Ownership is determined only when supported by the supplied sources.

For the **Mumbai Office Lease Renewal**, the sources do not establish an authorized signer. Therefore, the commitment remains:

**UNCLEAR OWNERSHIP / UNASSIGNED**

The agent does not infer Facilities, Arjun, or any other person as the owner.

## 7. Calendar Correlation

Calendar events provide contextual information around commitments and deadlines.

The system uses the supplied calendar data to connect relevant meetings and events without asserting unsupported conflicts.

## 8. Output

The same provenance-backed commitment records are used to generate:

- Executive Dashboard
- Daily Action Brief
- Deadline / Overdue view
- Commitment Timeline
- Calendar Context
- Evidence-grounded Q&A

This ensures that the information displayed across the application remains consistent and traceable to the supplied source data.
