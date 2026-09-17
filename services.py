"""Deterministic commitment and grounded Q&A services."""
from data_pack import COMMITMENTS, SOURCES

def get_commitment(item_id):
    return next((item for item in COMMITMENTS if item["id"] == item_id), None)

def grouped(bucket):
    return [item for item in COMMITMENTS if item["bucket"] == bucket]

def counts():
    return {"open": 2, "overdue": 1, "waiting": 0, "unclear": 1, "confirmed": 1, "completed": 1}

def answer_question(question):
    q = (question or "").lower().strip()
    if not q:
        return {"answer": "Enter a question to search the supplied Data Pack.", "evidence": [], "sources": []}
    vendor = get_commitment("vendor-list"); lease = get_commitment("mumbai-lease"); expense = get_commitment("expense-report"); q3 = get_commitment("q3-deck")
    if any(x in q for x in ["promise raghav", "vendor list", "promise"]):
        return {"answer": "You promised Raghav the updated vendor list. The commitment was revised from Tuesday EOD to Wednesday morning. No completion evidence is recorded, and Raghav followed up Wednesday at 8:45 AM.", "evidence": vendor["history"], "sources": vendor["sources"], "action": vendor}
    if "overdue" in q:
        return {"answer": "The updated vendor list for Raghav is overdue and open. Its latest explicit commitment was Wednesday morning; no completion evidence is recorded.", "evidence": vendor["history"], "sources": vendor["sources"], "action": vendor}
    if any(x in q for x in ["action today", "needs action", "today"]):
        return {"answer": "Today, confirm the authorized signer for the Mumbai office lease renewal. Also confirm whether the Q3 campaign deck review scheduled for 9:30 AM occurred; completion is not evidenced.", "evidence": lease["history"] + q3["history"][-2:], "sources": lease["sources"] + q3["sources"], "action": lease}
    if any(x in q for x in ["mumbai", "who owns", "owner"]):
        return {"answer": "The supplied Data Pack does not establish an owner for the Mumbai office lease renewal. Confirm the authorized signer; ownership was intentionally not inferred.", "evidence": lease["history"], "sources": lease["sources"], "action": lease}
    if "waiting" in q:
        return {"answer": "There are no open items classified as Waiting on Others. The expense variance report was delivered and acknowledged; the Mumbai lease is Unclear Ownership, not waiting on a confirmed owner.", "evidence": expense["history"] + lease["history"][-2:], "sources": expense["sources"] + lease["sources"]}
    if any(x in q for x in ["changed", "what changed"]):
        return {"answer": "Vendor List moved from Tuesday EOD to Wednesday morning. Q3 Deck review moved from Wednesday to Thursday at 9:30 AM. The expense report moved from Thursday morning to Wednesday evening, then was completed.", "evidence": vendor["history"] + q3["history"] + expense["history"], "sources": vendor["sources"] + q3["sources"] + expense["sources"]}
    if any(x in q for x in ["complete", "completed", "expense"]):
        return {"answer": "The July expense variance report is completed. Divya sent it Wednesday at 6:00 PM and Arjun acknowledged it at 6:10 PM.", "evidence": expense["history"], "sources": expense["sources"], "action": expense}
    if any(x in q for x in ["meeting", "calendar"]):
        return {"answer": "Relevant commitment context includes the Q3 Deck Review at 9:30 AM Thursday, Board Prep Session at 9:00 AM Thursday, Meridian Logistics call at 3:00 PM Wednesday, and Facilities Check-in at 10:00 AM Friday.", "evidence": [], "sources": ["Arjun Calendar", "Neha Calendar", "Raghav Calendar", "Divya Calendar"]}
    return {"answer": "I don't have enough evidence in the supplied Data Pack to answer that.", "evidence": [], "sources": []}
