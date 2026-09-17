# Data Lineage

1. Input: the supplied Data Pack PDF is the sole business-data source.
2. Extraction: facts are structured as commitments, sources, event history, and calendar events in data_pack.py.
3. Normalization: dates, commitments, deadlines, stakeholders, and owners use a consistent schema.
4. Deduplication: Vendor List is one entity with Leadership Sync, email-thread, and Voice Note 1 evidence.
5. Status calculation: completion, follow-up, and confirmation evidence produces status; missing completion is not completion.
6. Ownership classification: Mumbai remains Unassigned because no source assigns it.
7. Calendar correlation: supplied events are context only; no unsupported conflict is asserted.
8. Output: dashboard, brief, timeline, and Q&A render the same provenance-backed record.
