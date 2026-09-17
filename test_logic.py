from services import get_commitment, answer_question, grouped

def test_vendor_extraction(): assert get_commitment("vendor-list")["owner"] == "Arjun Malhotra"
def test_vendor_deadline_revision(): assert get_commitment("vendor-list")["latest_commitment"] == "Wednesday morning"
def test_vendor_deduplication(): assert len([x for x in grouped("my_action") if x["id"] == "vendor-list"]) == 1
def test_vendor_overdue(): assert get_commitment("vendor-list")["status"] == "OVERDUE / OPEN"
def test_expense_completion(): assert get_commitment("expense-report")["status"] == "COMPLETED"
def test_meridian_confirmation(): assert get_commitment("meridian-call")["status"] == "CONFIRMED"
def test_q3_revision(): assert get_commitment("q3-deck")["deadline"] == "Thursday 24 Sep - 9:30 AM"
def test_q3_not_completed(): assert get_commitment("q3-deck")["status"] == "READY / REVIEW SCHEDULED"
def test_mumbai_unclear(): assert get_commitment("mumbai-lease")["status"] == "UNCLEAR OWNERSHIP"
def test_friday_deadline(): assert get_commitment("mumbai-lease")["deadline"] == "Friday 25 Sep - EOD"
def test_voice_note_source(): assert "Voice Note 1" in get_commitment("vendor-list")["sources"]
def test_calendar_correlation(): assert "Arjun Calendar" in get_commitment("q3-deck")["sources"]
def test_qa_grounding(): assert "Wednesday morning" in answer_question("What did I promise Raghav?")["answer"]
def test_unsupported_question(): assert "don't have enough evidence" in answer_question("What is the weather?")["answer"]
def test_no_hallucinated_owner(): assert get_commitment("mumbai-lease")["owner"] == "Unassigned"
