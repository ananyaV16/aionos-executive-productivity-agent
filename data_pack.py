"""Structured, Data-Pack-only facts for the Executive Productivity Agent."""
from datetime import datetime

DEMO_NOW = datetime(2026, 9, 24, 17, 0)
EXECUTIVE = {"name": "Arjun Malhotra", "role": "VP Sales"}

SOURCES = {
    "Leadership Sync": "Meeting transcript - Monday 21 Sep, 9:00-9:35 AM",
    "Vendor List email thread": "Five-message email thread, 21-23 Sep",
    "Q3 Campaign Deck email thread": "Five-message email thread, 21-24 Sep",
    "Call Reschedule thread": "Five-message email thread, 21-23 Sep",
    "Expense Variance Report thread": "Five-message email thread, 21-23 Sep",
    "Mumbai Office Lease Renewal thread": "Five-message email thread, 21-24 Sep",
    "Voice Note 1": "Arjun personal memo - Monday 21 Sep, 6:40 PM",
    "Voice Note 2": "Arjun personal memo - Wednesday 23 Sep, 8:15 AM",
    "Arjun Calendar": "Week of 21-25 September 2026",
    "Neha Calendar": "Week of 21-25 September 2026",
    "Raghav Calendar": "Week of 21-25 September 2026",
    "Divya Calendar": "Week of 21-25 September 2026",
}

COMMITMENTS = [
    {
        "id": "vendor-list", "title": "Send updated vendor list", "stakeholder": "Raghav Sethi",
        "owner": "Arjun Malhotra", "bucket": "my_action", "status": "OVERDUE / OPEN",
        "deadline": "Wednesday 23 Sep - morning", "deadline_dt": datetime(2026, 9, 23, 12),
        "latest_commitment": "Wednesday morning", "next_action": "Send the updated vendor list to Raghav.",
        "summary": "One commitment with three supporting mentions; no completion evidence is recorded.",
        "why": "Latest explicit commitment was Wednesday morning. Raghav followed up at 8:45 AM, and no completion evidence appears in the supplied sources.",
        "sources": ["Leadership Sync", "Vendor List email thread", "Voice Note 1"],
        "history": [
            ("Mon 21 Sep, 9:00 AM", "Leadership Sync", "Arjun says he will send the updated vendor list by end of day Tuesday."),
            ("Mon 21 Sep, 5:40 PM", "Vendor List email thread", "Arjun says first thing Tuesday morning instead."),
            ("Tue 22 Sep, 6:30 PM", "Vendor List email thread", "Arjun revises the commitment to Wednesday morning."),
            ("Wed 23 Sep, 8:45 AM", "Vendor List email thread", "Raghav follows up: still good for this morning?"),
            ("Mon 21 Sep, 6:40 PM", "Voice Note 1", "Arjun records a personal reminder about the vendor list."),
        ],
    },
    {
        "id": "q3-deck", "title": "Review Q3 campaign deck", "stakeholder": "Neha Kapoor",
        "owner": "Arjun Malhotra", "bucket": "my_action", "status": "READY / REVIEW SCHEDULED",
        "deadline": "Thursday 24 Sep - 9:30 AM", "deadline_dt": datetime(2026, 9, 24, 9, 30),
        "latest_commitment": "Thursday 24 Sep, 9:30 AM", "next_action": "Confirm whether the scheduled review occurred; completion is not evidenced.",
        "summary": "Scheduled earlier today - completion not evidenced.",
        "why": "Neha said the deck was ready at 8:00 AM and a 9:30 AM review was scheduled. The supplied sources do not record that the review happened.",
        "sources": ["Leadership Sync", "Q3 Campaign Deck email thread", "Arjun Calendar", "Neha Calendar"],
        "history": [
            ("Mon 21 Sep, 11:00 AM", "Q3 Campaign Deck email thread", "Neha targets Wednesday for Arjun's review."),
            ("Tue 22 Sep, 4:15 PM", "Q3 Campaign Deck email thread", "Review shifts to Thursday morning."),
            ("Wed 23 Sep, 10:20 AM", "Q3 Campaign Deck email thread", "Neha proposes Thursday 9:30 AM."),
            ("Thu 24 Sep, 8:00 AM", "Q3 Campaign Deck email thread", "Neha says the deck is ready ahead of the 9:30 review."),
        ],
    },
    {
        "id": "expense-report", "title": "Receive July expense variance report", "stakeholder": "Divya Rao",
        "owner": "Divya Rao", "bucket": "completed", "status": "COMPLETED",
        "deadline": "Wednesday 23 Sep - evening", "deadline_dt": datetime(2026, 9, 23, 18),
        "latest_commitment": "Delivered Wednesday 23 Sep, 6:00 PM", "next_action": "No open action.",
        "summary": "Delivered by Divya and acknowledged by Arjun.",
        "why": "Divya sent the report at 6:00 PM Wednesday and Arjun acknowledged receipt at 6:10 PM.",
        "sources": ["Leadership Sync", "Expense Variance Report thread", "Voice Note 2"],
        "history": [
            ("Mon 21 Sep", "Leadership Sync", "Divya commits to the July expense variance report."),
            ("Tue 22 Sep, 9:00 AM", "Expense Variance Report thread", "Arjun asks for Wednesday evening instead of Thursday morning."),
            ("Wed 23 Sep, 6:00 PM", "Expense Variance Report thread", "Divya sends the report."),
            ("Wed 23 Sep, 6:10 PM", "Expense Variance Report thread", "Arjun acknowledges receipt."),
        ],
    },
    {
        "id": "meridian-call", "title": "Call Meridian Logistics", "stakeholder": "Priya Nair",
        "owner": "Arjun Malhotra", "bucket": "confirmed", "status": "CONFIRMED",
        "deadline": "Wednesday 23 Sep - 3:00 PM", "deadline_dt": datetime(2026, 9, 23, 15),
        "latest_commitment": "Confirmed Wednesday 23 Sep, 2:00 PM", "next_action": "Scheduled call; no unresolved scheduling action.",
        "summary": "The rescheduled call was mutually confirmed.",
        "why": "Arjun proposed Wednesday 3:00 PM, Priya confirmed it, and Arjun reconfirmed at 2:00 PM.",
        "sources": ["Leadership Sync", "Call Reschedule thread", "Voice Note 2", "Arjun Calendar"],
        "history": [
            ("Tue 22 Sep, 3:00 PM", "Call Reschedule thread", "Arjun proposes Wednesday 3:00 PM."),
            ("Tue 22 Sep, 5:45 PM", "Call Reschedule thread", "Priya confirms Wednesday 3:00 PM."),
            ("Wed 23 Sep, 2:00 PM", "Call Reschedule thread", "Arjun reconfirms the call."),
        ],
    },
    {
        "id": "mumbai-lease", "title": "Mumbai office lease renewal", "stakeholder": "Facilities / Raghav Sethi",
        "owner": "Unassigned", "bucket": "unclear", "status": "UNCLEAR OWNERSHIP",
        "deadline": "Friday 25 Sep - EOD", "deadline_dt": datetime(2026, 9, 25, 17),
        "latest_commitment": "Authorized signature still pending", "next_action": "Confirm the authorized signer.",
        "summary": "Authorized signature required; no source establishes an assigned signer.",
        "why": "Sources indicate uncertainty about the authorized signer. No source explicitly assigns ownership.",
        "sources": ["Leadership Sync", "Mumbai Office Lease Renewal thread", "Voice Note 1", "Arjun Calendar", "Raghav Calendar"],
        "history": [
            ("Mon 21 Sep, 9:00 AM", "Leadership Sync", "Raghav says the paperwork needs someone to sign; ownership is not known. Arjun says: flag it, don't assume."),
            ("Tue 22 Sep, 11:00 AM", "Mumbai Office Lease Renewal thread", "Raghav asks who is signing off; it has not been assigned."),
            ("Wed 23 Sep, 9:30 AM", "Mumbai Office Lease Renewal thread", "Divya says it is not on her end and believes it typically sits with Facilities."),
            ("Thu 24 Sep, 4:00 PM", "Mumbai Office Lease Renewal thread", "Facilities says signature is still pending; deadline is Friday EOD."),
            ("Thu 24 Sep, 4:45 PM", "Mumbai Office Lease Renewal thread", "Raghav says it is still unowned and asks Arjun to confirm."),
        ],
    },
]

CALENDAR = [
    ("Mon 21", "9:00-9:35 AM", "Leadership Sync", "meeting"), ("Mon 21", "2:00-2:30 PM", "1:1 with Neha", "meeting"), ("Mon 21", "4:00-5:00 PM", "Blocked", "blocked"),
    ("Tue 22", "11:00 AM-12:00 PM", "Internal Budget Review", "meeting"), ("Tue 22", "3:00-3:30 PM", "Blocked", "blocked"),
    ("Wed 23", "3:00-3:30 PM", "Call - Meridian Logistics", "related"), ("Wed 23", "6:00-6:15 PM", "Blocked", "blocked"),
    ("Thu 24", "9:00-10:00 AM", "Board Prep Session", "related"), ("Thu 24", "4:00-5:00 PM", "Hiring Panel - Sales Associate", "meeting"),
    ("Fri 25", "10:00-10:30 AM", "Facilities Check-in", "related"), ("Fri 25", "1:00-2:00 PM", "Blocked", "blocked"),
]
