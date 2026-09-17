# QA Report

## Automated coverage

tests/test_logic.py contains 15 assignment-critical assertions: vendor extraction, revision, deduplication and overdue status; expense completion; Meridian confirmation; Q3 revision and non-completion; Mumbai unclear ownership and Friday deadline; voice-note extraction; calendar correlation; grounded and unsupported Q&A; and no inferred owner.

## Manual smoke tests

- Navigate every sidebar page.
- Expand Vendor List and Mumbai Lease evidence.
- Run all five Demo Mode scenarios.
- Confirm Q3 is scheduled earlier today, not completed.
- Confirm Expense Report is absent from open actions.
