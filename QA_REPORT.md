# QA Report

This document summarizes the automated and manual validation performed for the Executive Productivity Agent.

## Automated Coverage

`tests/test_logic.py` contains **15 assignment-critical assertions** covering:

- Vendor List extraction
- Deadline revision
- Commitment deduplication
- Overdue status
- Expense report completion
- Meridian call confirmation
- Q3 Campaign Deck deadline revision
- Q3 review non-completion handling
- Mumbai lease unclear ownership
- Mumbai Friday deadline
- Voice-note commitment extraction
- Calendar correlation
- Grounded Q&A
- Unsupported-question handling
- Prevention of inferred ownership

## Manual Smoke Tests

The following application flows were manually checked:

- Navigate through every sidebar page.
- Expand Vendor List evidence.
- Expand Mumbai Lease evidence.
- Run all five Demo Mode scenarios.
- Confirm the Q3 Campaign Deck is scheduled earlier today and is **not marked completed** without evidence.
- Confirm the Expense Report is completed and excluded from open actions.

## Validation Principles

The QA process specifically verifies that the agent:

1. Uses only supplied Data Pack evidence.
2. Preserves the latest explicit commitment.
3. Deduplicates repeated commitment mentions.
4. Does not treat missing evidence as completion.
5. Does not infer ownership when the source is unclear.
6. Produces consistent results across the dashboard, timeline, brief, and Q&A.
