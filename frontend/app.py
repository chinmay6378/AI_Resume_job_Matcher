import streamlit as st
import requests

# ---------- Page Config ----------
st.set_page_config(
    page_title="AI Resume Job Matcher",
    page_icon="✨",
    layout="centered"
)

# ---------- Animated CSS ----------
st.markdown("""
<style>
@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e, #000);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
    color: white;
}

.glass {
    background: rgba(255, 255, 255, 0.08);
    backdrop-filter: blur(18px);
    border-radius: 20px;
    padding: 20px;
    margin-top: 15px;
    box-shadow: 0 0 25px rgba(0, 255, 204, 0.15);
    transition: 0.4s ease;
}

.glass:hover {
    transform: scale(1.02);
    box-shadow: 0 0 35px rgba(0, 255, 204, 0.3);
}

.badge {
    display: inline-block;
    background: linear-gradient(135deg, #00ffcc, #00ccff);
    color: #000;
    padding: 7px 14px;
    border-radius: 25px;
    margin: 6px 6px 0 0;
    font-size: 14px;
    font-weight: bold;
}

.job-card {
    background: rgba(0, 0, 0, 0.6);
    border-left: 5px solid #00ffcc;
    border-radius: 16px;
    padding: 18px;
    margin-top: 14px;
    transition: 0.4s ease-in-out;
}

.job-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 20px rgba(0, 255, 204, 0.4);
}

.role-box {
    background: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 18px;
    padding: 20px;
    margin-top: 10px;
}

.progress-glow > div > div {
    background: linear-gradient(90deg, #00ffcc, #00ccff) !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown("""
<h1 style="text-align:center; font-size: 42px;">✨ AI Resume Analyzer + Job Matcher</h1>
<p style="text-align:center; color: #aaa;">AI-powered career insights with smart role matching</p>
""", unsafe_allow_html=True)

# ---------- Upload ----------
uploaded_file = st.file_uploader("📄 Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("✨ Analyzing your resume with AI..."):
        files = {
            "file": (uploaded_file.name, uploaded_file, "application/pdf")
        }
        response = requests.post("http://127.0.0.1:8000/analyze", files=files)
        data = response.json()

    skills_text = data.get("skills", "")
    jobs = data.get("matched_jobs", [])

    # ---------- Skills ----------
    st.markdown("## ✅ Your AI-Extracted Skills")

    skills = [s.strip() for s in skills_text.replace("•", "").split(",") if s.strip()]

    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    for skill in skills:
        st.markdown(f"<span class='badge'>{skill}</span>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- Role Matching ----------
    st.markdown("## 🎯 Best Matching Career Roles")

    role_summary = {
        "Machine Learning Engineer": ["Python", "TensorFlow", "NLP", "Deep Learning"],
        "Backend Developer": ["FastAPI", "Docker", "REST", "Node.js"],
        "Data Analyst": ["SQL", "Excel", "Power BI", "Visualization"]
    }

    st.markdown("<div class='role-box'>", unsafe_allow_html=True)

    for role, req_skills in role_summary.items():
        matched = len([s for s in skills if any(r.lower() in s.lower() for r in req_skills)])
        score = int((matched / len(req_skills)) * 100)

        st.markdown(f"### 🚀 {role}")
        st.markdown('<div class="progress-glow">', unsafe_allow_html=True)
        st.progress(score)
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f"✅ Match Strength: **{score}%**")

    st.markdown("</div>", unsafe_allow_html=True)

    # ---------- Jobs ----------
    st.markdown("## 💼 AI-Matched Job Opportunities")

    if jobs:
        for job in jobs:
            title = job.split(" - ")[0]
            desc = job.replace(title + " - ", "")

            st.markdown(f"""
            <div class="job-card">
                <h4>🏷️ {title}</h4>
                <p style="color:#ccc;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("No strong job matches found.")

    # ---------- Footer ----------
    st.markdown("""
    <hr style="margin-top:40px;">
    <p style="text-align:center; color:#888;">🚀 Built by Chinmay | AI Career Platform</p>
    """, unsafe_allow_html=True)
