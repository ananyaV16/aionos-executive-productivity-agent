# Architecture

```mermaid
flowchart TD
 A[Input sources] --> B[Structured ingestion] --> C[Commitment extraction] --> D[Entity resolution] --> E[Deadline normalization] --> F[Deduplication] --> G[Status engine] --> H[Ownership classification] --> I[Calendar correlation] --> J[Evidence and provenance] --> K[Executive brief and Q&A]
```

The implementation is deliberately deterministic. data_pack.py contains only supplied facts, services.py determines grounded classifications, and app.py renders the enterprise UI. Every item keeps sources, rationale, and evidence history.
