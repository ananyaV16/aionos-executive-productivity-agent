import streamlit as st
from data_pack import EXECUTIVE, COMMITMENTS, SOURCES, CALENDAR
from services import grouped, counts, answer_question

st.set_page_config(page_title="AIONOS | Executive Productivity", page_icon="A", layout="wide", initial_sidebar_state="expanded")
st.markdown('''<style>
  .stApp {background:#F7F9FC;color:#0F172A}.block-container{padding-top:1.5rem;max-width:1450px}
  [data-testid="stSidebar"]{background:#0F2747}.sidebar-brand{color:#fff;font-size:23px;font-weight:800;letter-spacing:-.5px}.sidebar-sub{color:#bed0e8;font-size:13px;margin-top:-10px}
  h1,h2,h3{color:#0F172A;letter-spacing:-.6px}.eyebrow{color:#2563EB;font-size:12px;font-weight:800;letter-spacing:1.1px}.subtitle{color:#64748B;font-size:16px}
  .metric{background:#fff;border:1px solid #E2E8F0;border-radius:10px;padding:17px 18px;box-shadow:0 2px 5px rgba(15,39,71,.04)}.metric .n{font-size:27px;font-weight:760;color:#0F2747}.metric .l{font-size:12px;color:#64748B;font-weight:700;text-transform:uppercase;letter-spacing:.6px}
  .card{background:#fff;border:1px solid #E2E8F0;border-radius:10px;padding:20px;margin:10px 0;box-shadow:0 2px 6px rgba(15,39,71,.04)}.card h3{margin:0 0 7px;font-size:18px}.meta{color:#64748B;font-size:13px;margin:5px 0}.badge{display:inline-block;padding:4px 9px;border-radius:4px;font-size:11px;font-weight:800;letter-spacing:.35px}.overdue{background:#FEE2E2;color:#B91C1C}.ready{background:#DBEAFE;color:#1D4ED8}.complete{background:#DCFCE7;color:#15803D}.confirmed{background:#E0F2FE;color:#0369A1}.unclear{background:#FEF3C7;color:#92400E}.neutral{background:#E2E8F0;color:#475569}
  .timeline{border-left:2px solid #CBD5E1;margin:10px 0 5px 8px;padding-left:22px}.event{position:relative;padding:0 0 16px}.event:before{content:'';position:absolute;width:10px;height:10px;border-radius:50%;background:#2563EB;left:-28px;top:5px}.event-time{font-size:12px;font-weight:800;color:#2563EB}.source{font-size:12px;color:#64748B}.note{background:#EFF6FF;border-left:3px solid #2563EB;padding:12px 15px;color:#1E3A5F;border-radius:3px}
  /* Evidence panels only: override Streamlit's default expander surface without affecting other controls. */
  [data-testid="stExpander"]{background:#FFFFFF!important;border:1px solid #D9E2EC!important;border-radius:11px!important;box-shadow:0 2px 6px rgba(15,39,71,.04)!important;overflow:hidden}
  [data-testid="stExpander"] details{background:#FFFFFF!important}
  [data-testid="stExpander"] summary{background:#F7FAFC!important;color:#0F2747!important;padding:13px 16px!important;transition:background-color .16s ease}
  [data-testid="stExpander"] summary:hover{background:#EFF6FF!important}
  [data-testid="stExpander"] summary p,[data-testid="stExpander"] summary span{color:#0F2747!important;font-weight:700!important}
  [data-testid="stExpander"] summary svg{color:#2563EB!important;fill:#2563EB!important}
  [data-testid="stExpander"] > details > summary,[data-testid="stExpander"] > details > summary > div{background-color:#F7FAFC!important;color:#0F2747!important}
  [data-testid="stExpander"] > details > summary:hover,[data-testid="stExpander"] > details > summary:hover > div{background-color:#EFF6FF!important}
  [data-testid="stExpander"] summary::marker,[data-testid="stExpander"] summary::-webkit-details-marker{color:#2563EB!important}
  [data-testid="stExpander"] [data-testid="stExpanderIcon"],[data-testid="stExpander"] [data-testid="stExpanderIcon"] *{color:#2563EB!important;fill:#2563EB!important;stroke:#2563EB!important}
  [data-testid="stExpander"] [data-testid="stExpanderDetails"]{background:#FFFFFF!important;color:#0F172A!important;padding:4px 16px 16px!important}
  [data-testid="stExpander"] [data-testid="stExpanderDetails"] p,[data-testid="stExpander"] [data-testid="stExpanderDetails"] li,[data-testid="stExpander"] [data-testid="stExpanderDetails"] span,[data-testid="stExpander"] [data-testid="stExpanderDetails"] strong{color:#0F172A!important}
</style>''', unsafe_allow_html=True)

def badge(status):
    cls = "overdue" if "OVERDUE" in status else "unclear" if "UNCLEAR" in status else "complete" if "COMPLETED" in status else "confirmed" if "CONFIRMED" in status else "ready" if "READY" in status else "neutral"
    return f'<span class="badge {cls}">{status}</span>'

def item_card(item, detailed=True):
    st.markdown(f'''<div class="card"><div style="display:flex;justify-content:space-between;gap:12px"><h3>{item['title']}</h3>{badge(item['status'])}</div><div class="meta"><b>Deadline:</b> {item['deadline']} &nbsp; | &nbsp; <b>Owner:</b> {item['owner']} &nbsp; | &nbsp; <b>Stakeholder:</b> {item['stakeholder']}</div><div>{item['summary']}</div><div class="meta"><b>Next action:</b> {item['next_action']}</div></div>''', unsafe_allow_html=True)
    if detailed:
        with st.expander("Why am I seeing this?  Evidence & provenance"):
            st.markdown(f"**Classification rationale:** {item['why']}")
            st.markdown("**Sources:** " + " · ".join(item["sources"]))
            for t, src, text in item["history"]:
                st.markdown(f"- **{t}** — *{src}*: {text}")

def header(title, subtitle=None):
    st.markdown('<div class="eyebrow">AIONOS / EXECUTIVE PRODUCTIVITY AGENT</div>', unsafe_allow_html=True)
    st.title(title)
    st.markdown(f'<div class="subtitle">{subtitle or "Arjun Malhotra · VP Sales · Week of 21-25 September 2026"}</div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-brand">AIONOS</div><div class="sidebar-sub">Executive Productivity</div><br>', unsafe_allow_html=True)
    if "active_page" not in st.session_state: st.session_state.active_page = "Executive Dashboard"
    st.markdown("**OVERVIEW**")
    for label in ["Executive Dashboard", "Daily Action Brief"]:
        if st.button(label, key="nav_"+label, use_container_width=True): st.session_state.active_page = label
    st.markdown("**COMMITMENTS**")
    for label in ["My Actions", "Waiting on Others", "Deadlines / Overdue", "Unclear Ownership", "Commitment Timeline"]:
        if st.button(label, key="nav_"+label, use_container_width=True): st.session_state.active_page = label
    st.markdown("**INTELLIGENCE**")
    for label in ["Calendar Context", "Ask the Workspace", "Demo Mode"]:
        if st.button(label, key="nav_"+label, use_container_width=True): st.session_state.active_page = label
    st.markdown("**SYSTEM**")
    if st.button("Sources & Method", key="nav_sources", use_container_width=True): st.session_state.active_page = "Sources & Method"

active = st.session_state.active_page

if active == "Executive Dashboard":
    header("Good afternoon, Arjun.", "Your commitments, deadlines and follow-ups - grounded in the supplied Data Pack.")
    c=counts(); cols=st.columns(6)
    for col,(label,num) in zip(cols, [("Open Actions",c['open']),("Overdue",c['overdue']),("Waiting on Others",c['waiting']),("Unclear Ownership",c['unclear']),("Confirmed Calls",c['confirmed']),("Completed",c['completed'])]):
        col.markdown(f'<div class="metric"><div class="n">{num}</div><div class="l">{label}</div></div>', unsafe_allow_html=True)
    st.markdown("### TODAY'S ATTENTION")
    for item in [COMMITMENTS[0], COMMITMENTS[4], COMMITMENTS[1]]: item_card(item)
    st.markdown("### AGENT ACTIVITY")
    st.markdown('<div class="note">✓ Parsed supplied sources &nbsp; ✓ Extracted executive commitments &nbsp; ✓ Reconciled deadline changes &nbsp; ✓ Deduplicated repeated commitments &nbsp; ✓ Checked completion evidence &nbsp; ✓ Detected unclear ownership &nbsp; ✓ Linked calendar context</div>', unsafe_allow_html=True)
elif active == "Daily Action Brief":
    header("Daily Action Brief", "Thursday 24 September 2026 · afternoon / evening demo state")
    st.markdown("### Executive Summary")
    st.markdown("Two executive actions require attention: an overdue vendor-list commitment and follow-up on a Q3 deck review scheduled earlier today. The Mumbai lease has a Friday EOD deadline but no established owner. The expense report is completed; the Meridian call is confirmed.")
    for label, items in [("My Actions", grouped("my_action")), ("Waiting on Others", grouped("waiting")), ("Overdue", [COMMITMENTS[0]]), ("Due Soon", [COMMITMENTS[4]]), ("Unclear Ownership", grouped("unclear")), ("Completed", grouped("completed"))]:
        st.markdown(f"### {label}")
        if items:
            for item in items: item_card(item, False)
        else: st.info("No items meet this classification in the supplied Data Pack.")
    st.markdown("### Calendar Context"); st.markdown("Facilities Check-in is Friday 10:00-10:30 AM; Q3 Deck Review was scheduled Thursday at 9:30 AM; Board Prep Session was Thursday 9:00-10:00 AM.")
    st.download_button("Download Executive Brief", data="AIONOS Executive Brief\n\n" + "\n".join(f"{x['title']}: {x['status']}" for x in COMMITMENTS), file_name="executive_brief_2026-09-24.txt")
elif active == "My Actions":
    header("My Actions", "Only commitments owned by Arjun Malhotra")
    for item in grouped("my_action"): item_card(item)
elif active == "Waiting on Others":
    header("Waiting on Others")
    st.info("No open items are waiting on a confirmed other owner. The expense report is completed; the Mumbai lease is classified separately as Unclear Ownership.")
elif active == "Deadlines / Overdue":
    header("Deadline Intelligence", "Commitment changes and present-state classification")
    st.markdown("### MON → TUE → WED → THU → FRI")
    for item in COMMITMENTS: item_card(item, False)
elif active == "Unclear Ownership":
    header("Unclear Ownership", "The agent does not infer owners without explicit evidence.")
    item_card(COMMITMENTS[4])
    st.markdown('<div class="note"><b>Recommended action: CONFIRM THE AUTHORIZED SIGNER</b><br>Ownership was intentionally not inferred because the supplied sources do not establish an assigned signer.</div>', unsafe_allow_html=True)
elif active == "Commitment Timeline":
    header("Commitment Timeline", "Evolution of evidence, commitments and outcomes")
    for item in [COMMITMENTS[0], COMMITMENTS[1], COMMITMENTS[2]]:
        st.markdown(f"### {item['title']} {badge(item['status'])}", unsafe_allow_html=True)
        st.markdown('<div class="timeline">' + ''.join(f'<div class="event"><div class="event-time">{t}</div><b>{src}</b><br><span class="source">{txt}</span></div>' for t,src,txt in item['history']) + '</div>', unsafe_allow_html=True)
elif active == "Calendar Context":
    header("Calendar Context", "Arjun Malhotra's supplied calendar · week of 21-25 September")
    cols=st.columns(5)
    days=["Mon 21","Tue 22","Wed 23","Thu 24","Fri 25"]
    for col, day in zip(cols,days):
        col.markdown(f"#### {day} Sep")
        for d,time,event,kind in [x for x in CALENDAR if x[0]==day]:
            color={"related":"#DBEAFE","blocked":"#F1F5F9","meeting":"#FFFFFF"}[kind]
            col.markdown(f'<div style="background:{color};border:1px solid #E2E8F0;border-radius:6px;padding:9px;margin:7px 0;font-size:13px"><b>{time}</b><br>{event}</div>', unsafe_allow_html=True)
    st.markdown("### Relevant to Open Commitments")
    st.markdown("Q3 Deck Review · Board Prep Session · Meridian Logistics Call · Facilities Check-in. No calendar conflict is asserted beyond the supplied times.")
elif active in ["Ask the Workspace", "Demo Mode"]:
    header("Ask the Executive Workspace" if active == "Ask the Workspace" else "Demo Mode", "Evidence-grounded analysis of the supplied Data Pack")
    prompts=["What did I promise Raghav?", "What's overdue?", "What needs action today?", "Who owns the Mumbai lease?", "What changed this week?"]
    chosen = None
    if active == "Demo Mode":
        st.markdown("### Guided scenarios")
        for i,p in enumerate(prompts,1):
            if st.button(f"{i}  {p}", use_container_width=True): chosen=p
    question = st.text_input("Ask a question", value=chosen or "", placeholder="e.g. What did I promise Raghav?")
    if question:
        result=answer_question(question)
        st.markdown("### ANSWER"); st.markdown(f'<div class="card">{result["answer"]}</div>', unsafe_allow_html=True)
        st.markdown("### EVIDENCE")
        if result["evidence"]:
            for t,src,text in result["evidence"]: st.markdown(f"- **{t}** — *{src}*: {text}")
        else: st.caption("No item-level evidence is needed for this response.")
        st.markdown("### SOURCE"); st.markdown(" · ".join(dict.fromkeys(result["sources"])) if result["sources"] else "No supporting source identified.")
        if result.get("action"): item_card(result["action"], False)
elif active == "Sources & Method":
    header("Sources & Method", "Traceability is a product rule, not an afterthought.")
    st.markdown("### Supplied sources")
    for name,desc in SOURCES.items(): st.markdown(f"- **{name}** — {desc}")
    st.markdown("### Deterministic method")
    st.markdown("Structured source facts → normalization → commitment grouping → deadline/status reconciliation → ownership classification → calendar correlation → evidence-grounded dashboard, brief and Q&A. The application does not call an LLM at runtime and introduces no external facts.")
