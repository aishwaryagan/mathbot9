import streamlit as st
import time
from bot_logic import chat_with_mathbot
from curriculum import GRADE9_EXPECTATIONS, QUICK_PROMPTS, GROWING_SUCCESS_LEVELS
from dotenv import load_dotenv

load_dotenv()

# ─── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MathBot9 | Ontario Grade 9 Math",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Exo+2:wght@300;400;600;700&display=swap');

/* ── ROOT VARIABLES ── */
:root {
    --bg-deep:    #050b1a;
    --bg-card:    #0d1b35;
    --bg-panel:   #0a1628;
    --cyan:       #00d2ff;
    --pink:       #ff6b9d;
    --yellow:     #ffd93d;
    --green:      #06ffa5;
    --purple:     #c77dff;
    --orange:     #ff9a3c;
    --text:       #e8f4fd;
    --muted:      #7a9cc0;
    --border:     rgba(0,210,255,0.18);
    --glow-cyan:  0 0 20px rgba(0,210,255,0.4);
    --glow-pink:  0 0 20px rgba(255,107,157,0.4);
}

/* ── GLOBAL ── */
html, body, [class*="css"] {
    font-family: 'Exo 2', sans-serif;
    background-color: var(--bg-deep) !important;
    color: var(--text) !important;
}

/* Animated star background */
.main > div {
    background: 
        radial-gradient(ellipse at 20% 20%, rgba(0,210,255,0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(199,125,255,0.06) 0%, transparent 50%),
        radial-gradient(ellipse at 50% 50%, rgba(6,255,165,0.03) 0%, transparent 70%),
        var(--bg-deep);
}

/* ── SIDEBAR ── */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #060d1f 0%, #0a1628 100%) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] * { color: var(--text) !important; }

/* ── HEADER / TITLE ── */
.mathbot-header {
    text-align: center;
    padding: 1.5rem 0 0.5rem;
    position: relative;
}
.mathbot-logo {
    font-family: 'Orbitron', monospace;
    font-size: 3.2rem;
    font-weight: 900;
    background: linear-gradient(135deg, #00d2ff 0%, #c77dff 50%, #06ffa5 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: 0.08em;
    line-height: 1;
    text-shadow: none;
    animation: pulse-logo 3s ease-in-out infinite;
}
@keyframes pulse-logo {
    0%, 100% { filter: drop-shadow(0 0 8px rgba(0,210,255,0.6)); }
    50% { filter: drop-shadow(0 0 20px rgba(199,125,255,0.8)); }
}
.mathbot-subtitle {
    font-family: 'Exo 2', sans-serif;
    font-size: 0.9rem;
    color: var(--muted);
    letter-spacing: 0.25em;
    text-transform: uppercase;
    margin-top: 0.3rem;
}
.robot-emoji {
    font-size: 4rem;
    display: block;
    margin-bottom: 0.5rem;
    animation: float 3s ease-in-out infinite;
}
@keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
}

/* ── CHAT CONTAINER ── */
.chat-container {
    max-width: 860px;
    margin: 0 auto;
    padding: 0 1rem;
}

/* ── CHAT MESSAGES ── */
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 0.3rem 0 !important;
}

/* User bubble */
[data-testid="stChatMessage"][data-testid*="user"],
.stChatMessage:has([data-testid="chatAvatarIcon-user"]) {
    justify-content: flex-end;
}

/* ── CHAT INPUT ── */
[data-testid="stChatInput"] {
    background: var(--bg-card) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    color: var(--text) !important;
}
[data-testid="stChatInput"]:focus-within {
    border-color: var(--cyan) !important;
    box-shadow: var(--glow-cyan) !important;
}
[data-testid="stChatInput"] textarea {
    color: var(--text) !important;
    font-family: 'Exo 2', sans-serif !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: var(--muted) !important;
}

/* ── STRAND PILLS ── */
.strand-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 6px;
    margin: 8px 0;
}
.strand-pill {
    background: rgba(0,210,255,0.08);
    border: 1px solid rgba(0,210,255,0.25);
    border-radius: 10px;
    padding: 6px 10px;
    font-size: 0.75rem;
    font-family: 'Exo 2', sans-serif;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: center;
    color: var(--text);
}
.strand-pill:hover {
    background: rgba(0,210,255,0.2);
    border-color: var(--cyan);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(0,210,255,0.2);
}
.strand-pill.active {
    background: rgba(0,210,255,0.25);
    border-color: var(--cyan);
    box-shadow: var(--glow-cyan);
}

/* ── QUICK PROMPT BUTTONS ── */
.stButton > button {
    background: linear-gradient(135deg, rgba(0,210,255,0.1), rgba(199,125,255,0.1)) !important;
    border: 1px solid rgba(0,210,255,0.3) !important;
    border-radius: 12px !important;
    color: var(--text) !important;
    font-family: 'Exo 2', sans-serif !important;
    font-size: 0.8rem !important;
    padding: 0.4rem 0.7rem !important;
    transition: all 0.2s ease !important;
    width: 100% !important;
    text-align: left !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, rgba(0,210,255,0.25), rgba(199,125,255,0.25)) !important;
    border-color: var(--cyan) !important;
    transform: translateX(3px) !important;
    box-shadow: var(--glow-cyan) !important;
}

/* ── ACHIEVEMENT BADGE ── */
.achievement-badge {
    background: linear-gradient(135deg, rgba(255,217,61,0.15), rgba(255,154,60,0.15));
    border: 1px solid rgba(255,217,61,0.4);
    border-radius: 12px;
    padding: 10px 14px;
    margin: 8px 0;
    font-size: 0.8rem;
    text-align: center;
}

/* ── STAT CARDS ── */
.stat-card {
    background: rgba(13,27,53,0.8);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 12px;
    text-align: center;
    margin: 4px 0;
}
.stat-number {
    font-family: 'Orbitron', monospace;
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--cyan);
}
.stat-label {
    font-size: 0.7rem;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* ── WELCOME CARD ── */
.welcome-card {
    background: linear-gradient(135deg, rgba(0,210,255,0.08), rgba(199,125,255,0.08));
    border: 1px solid rgba(0,210,255,0.2);
    border-radius: 20px;
    padding: 1.5rem;
    margin: 1rem auto;
    max-width: 860px;
    text-align: center;
}

/* ── DIVIDER ── */
.neon-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, var(--cyan), transparent);
    margin: 12px 0;
    opacity: 0.4;
}

/* ── SELECTBOX ── */
[data-testid="stSelectbox"] > div > div {
    background: var(--bg-card) !important;
    border-color: var(--border) !important;
    color: var(--text) !important;
    border-radius: 10px !important;
}

/* ── SCROLLBAR ── */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--bg-deep); }
::-webkit-scrollbar-thumb { background: rgba(0,210,255,0.3); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--cyan); }

/* ── HIDE STREAMLIT BRANDING ── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* ── FLOATING MATH SYMBOLS ── */
.math-floater {
    position: fixed;
    font-size: 1.2rem;
    opacity: 0.06;
    color: var(--cyan);
    pointer-events: none;
    animation: drift linear infinite;
    z-index: 0;
}
@keyframes drift {
    0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
    10% { opacity: 0.06; }
    90% { opacity: 0.06; }
    100% { transform: translateY(-100px) rotate(360deg); opacity: 0; }
}
</style>

<!-- Floating math symbols for atmosphere -->
<div class="math-floater" style="left:5%;animation-duration:18s;animation-delay:0s;">∑</div>
<div class="math-floater" style="left:15%;animation-duration:22s;animation-delay:3s;">π</div>
<div class="math-floater" style="left:28%;animation-duration:16s;animation-delay:7s;">∫</div>
<div class="math-floater" style="left:42%;animation-duration:25s;animation-delay:1s;">√</div>
<div class="math-floater" style="left:58%;animation-duration:19s;animation-delay:9s;">∞</div>
<div class="math-floater" style="left:72%;animation-duration:21s;animation-delay:5s;">Δ</div>
<div class="math-floater" style="left:85%;animation-duration:17s;animation-delay:12s;">θ</div>
<div class="math-floater" style="left:93%;animation-duration:23s;animation-delay:4s;">λ</div>
""", unsafe_allow_html=True)

# ─── SESSION STATE INIT ────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "active_strand" not in st.session_state:
    st.session_state.active_strand = "All Strands"
if "question_count" not in st.session_state:
    st.session_state.question_count = 0
if "streak" not in st.session_state:
    st.session_state.streak = 0
if "pending_input" not in st.session_state:
    st.session_state.pending_input = None

# ─── SIDEBAR ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 0.5rem 0 1rem;">
        <span style="font-family:'Orbitron',monospace; font-size:1.2rem; font-weight:900;
              background:linear-gradient(135deg,#00d2ff,#c77dff);
              -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            🤖 MathBot9
        </span>
        <div style="font-size:0.65rem; color:#7a9cc0; letter-spacing:0.2em; text-transform:uppercase; margin-top:3px;">
            Ontario MTH1W
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{st.session_state.question_count}</div>
            <div class="stat-label">Questions</div>
        </div>""", unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{st.session_state.streak}🔥</div>
            <div class="stat-label">Streak</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # Strand selector
    st.markdown('<p style="font-size:0.8rem; color:#7a9cc0; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">📚 Focus Strand</p>', unsafe_allow_html=True)
    strand_options = ["All Strands"] + list(GRADE9_EXPECTATIONS.keys())
    active_strand = st.selectbox(
        "Strand",
        strand_options,
        label_visibility="collapsed",
        key="strand_selector"
    )
    st.session_state.active_strand = active_strand

    # Show expectations if strand selected
    if active_strand != "All Strands":
        strand_data = GRADE9_EXPECTATIONS[active_strand]
        st.markdown(f"""
        <div style="background:rgba(0,210,255,0.06); border:1px solid rgba(0,210,255,0.2);
             border-radius:12px; padding:10px; margin-top:8px;">
            <p style="font-size:0.75rem; color:#00d2ff; margin:0 0 6px; font-weight:700;">
                {strand_data['emoji']} Curriculum Expectations
            </p>
        """, unsafe_allow_html=True)
        for exp in strand_data["expectations"]:
            code = exp.split(" - ")[0]
            desc = exp.split(" - ")[1] if " - " in exp else exp
            st.markdown(f'<p style="font-size:0.68rem; color:#b0cce0; margin:3px 0;">• <span style="color:#00d2ff;">{code}</span> {desc}</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # Quick prompts
    st.markdown('<p style="font-size:0.8rem; color:#7a9cc0; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:8px;">⚡ Quick Start</p>', unsafe_allow_html=True)
    for prompt in QUICK_PROMPTS:
        if st.button(f"{prompt['emoji']} {prompt['text']}", key=f"qp_{prompt['text']}"):
            st.session_state.pending_input = prompt["text"]
            st.rerun()

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # Growing Success legend
    st.markdown('<p style="font-size:0.8rem; color:#7a9cc0; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:6px;">📋 Growing Success</p>', unsafe_allow_html=True)
    for level, data in GROWING_SUCCESS_LEVELS.items():
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:8px; margin:4px 0; padding:5px 8px;
             background:rgba(255,255,255,0.03); border-radius:8px;">
            <span style="font-size:1rem;">{data['emoji']}</span>
            <div>
                <span style="font-size:0.72rem; font-weight:700; color:{data['color']};">{level}</span>
                <span style="font-size:0.65rem; color:#7a9cc0;"> · {data['range']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="neon-divider"></div>', unsafe_allow_html=True)

    # Clear chat
    if st.button("🗑️ Clear Chat", key="clear_chat"):
        st.session_state.messages = []
        st.session_state.question_count = 0
        st.session_state.streak = 0
        st.rerun()

# ─── MAIN CONTENT ─────────────────────────────────────────────────────────────

# Header
st.markdown("""
<div class="mathbot-header">
    <span class="robot-emoji">🤖</span>
    <div class="mathbot-logo">MathBot9</div>
    <div class="mathbot-subtitle">Ontario Grade 9 Mathematics · MTH1W · Powered by AI</div>
</div>
""", unsafe_allow_html=True)

# Welcome card (only when no messages)
if not st.session_state.messages:
    st.markdown("""
    <div class="welcome-card">
        <p style="font-size:1.1rem; font-weight:600; margin:0 0 0.5rem; color:#e8f4fd;">
            Welcome to your personal math tutor! 🎉
        </p>
        <p style="font-size:0.9rem; color:#7a9cc0; margin:0 0 1rem;">
            I'm here to help you crush Ontario Grade 9 Math (MTH1W).<br>
            Ask me anything — from algebra to financial literacy — and I'll guide you step-by-step!
        </p>
        <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
            <span style="background:rgba(0,210,255,0.1); border:1px solid rgba(0,210,255,0.3);
                  border-radius:20px; padding:4px 14px; font-size:0.78rem;">📐 Algebra</span>
            <span style="background:rgba(255,107,157,0.1); border:1px solid rgba(255,107,157,0.3);
                  border-radius:20px; padding:4px 14px; font-size:0.78rem;">🔢 Number</span>
            <span style="background:rgba(6,255,165,0.1); border:1px solid rgba(6,255,165,0.3);
                  border-radius:20px; padding:4px 14px; font-size:0.78rem;">📊 Data</span>
            <span style="background:rgba(199,125,255,0.1); border:1px solid rgba(199,125,255,0.3);
                  border-radius:20px; padding:4px 14px; font-size:0.78rem;">📏 Geometry</span>
            <span style="background:rgba(255,154,60,0.1); border:1px solid rgba(255,154,60,0.3);
                  border-radius:20px; padding:4px 14px; font-size:0.78rem;">💰 Financial Literacy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ─── CHAT MESSAGES ────────────────────────────────────────────────────────────
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar="🤖" if message["role"] == "assistant" else "🧑‍🎓"):
        st.markdown(message["content"])

# ─── HANDLE INPUT ─────────────────────────────────────────────────────────────
user_input = st.chat_input("Ask MathBot9 anything... 🔢✨", key="main_input")

# Check for pending input from quick prompts
if st.session_state.pending_input:
    user_input = st.session_state.pending_input
    st.session_state.pending_input = None

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.question_count += 1

    with st.chat_message("user", avatar="🧑‍🎓"):
        st.markdown(user_input)

    # Get bot response
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("MathBot9 is calculating... 🧮"):
            # Build API message history (user + assistant only)
            api_messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]

            response = chat_with_mathbot(
                api_messages,
                active_strand=st.session_state.active_strand if st.session_state.active_strand != "All Strands" else None
            )

        # Typewriter effect
        placeholder = st.empty()
        displayed = ""
        for char in response:
            displayed += char
            placeholder.markdown(displayed + "▌")
            time.sleep(0.005)
        placeholder.markdown(displayed)

        # Update streak on positive responses
        positive_keywords = ["correct", "right", "exactly", "nailed", "perfect", "great", "excellent", "well done"]
        if any(kw in response.lower() for kw in positive_keywords):
            st.session_state.streak += 1
            if st.session_state.streak > 0 and st.session_state.streak % 3 == 0:
                st.balloons()
                st.markdown(f"""
                <div class="achievement-badge">
                    🏆 <strong>{st.session_state.streak}-question streak!</strong> You're on fire! Keep it up! 🔥
                </div>
                """, unsafe_allow_html=True)

    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
