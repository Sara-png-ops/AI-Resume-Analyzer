import streamlit as st
import PyPDF2
import re

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

# -----------------------------
# SKILLS DATABASE
# -----------------------------
SKILLS = [
    "python", "java", "c++", "c", "javascript", "html", "css",
    "sql", "mysql", "mongodb", "flask", "django", "streamlit",
    "react", "node.js", "git", "github", "docker",
    "machine learning", "deep learning", "artificial intelligence",
    "data analysis", "pandas", "numpy", "tensorflow",
    "cybersecurity", "networking", "linux", "aws",
    "nlp", "api", "rest api"
]


# -----------------------------
# EXTRACT TEXT FROM PDF
# -----------------------------
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + " "

    return text.lower()


# -----------------------------
# FIND SKILLS
# -----------------------------
def find_skills(text):
    found_skills = []

    for skill in SKILLS:
        if skill in text.lower():
            found_skills.append(skill)

    return list(set(found_skills))


# -----------------------------
# CALCULATE MATCH SCORE
# -----------------------------
def calculate_match(resume_skills, job_skills):
    if not job_skills:
        return 0

    matched = set(resume_skills) & set(job_skills)

    score = (len(matched) / len(set(job_skills))) * 100

    return round(score)


# -----------------------------
# MAIN UI
# -----------------------------
st.title("🤖 AI-Powered Resume Analyzer")
st.write("Upload your resume and compare it with a job description!")

st.divider()

col1, col2 = st.columns(2)

with col1:
    st.subheader("📄 Upload Your Resume")
    uploaded_file = st.file_uploader(
        "Upload a PDF resume",
        type=["pdf"]
    )

with col2:
    st.subheader("💼 Job Description")
    job_description = st.text_area(
        "Paste the job description here",
        height=250,
        placeholder="Paste the job requirements here..."
    )


# -----------------------------
# ANALYZE BUTTON
# -----------------------------
if st.button("🔍 Analyze Resume", use_container_width=True):

    if uploaded_file is None:
        st.warning("⚠️ Please upload your resume PDF first.")

    elif not job_description.strip():
        st.warning("⚠️ Please paste a job description first.")

    else:
        resume_text = extract_text_from_pdf(uploaded_file)

        resume_skills = find_skills(resume_text)
        job_skills = find_skills(job_description.lower())

        matched_skills = list(
            set(resume_skills) & set(job_skills)
        )

        missing_skills = list(
            set(job_skills) - set(resume_skills)
        )

        score = calculate_match(
            resume_skills,
            job_skills
        )

        st.divider()

        # SCORE
        st.subheader("📊 Resume Match Score")
        st.progress(score)
        st.metric("Match Percentage", f"{score}%")

        # RESULTS
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("✅ Matching Skills")

            if matched_skills:
                for skill in sorted(matched_skills):
                    st.success(skill.title())
            else:
                st.info("No matching skills found.")

        with col2:
            st.subheader("❌ Missing Skills")

            if missing_skills:
                for skill in sorted(missing_skills):
                    st.error(skill.title())
            else:
                st.success("Great! No important skills are missing.")

        # SUGGESTIONS
        st.divider()
        st.subheader("💡 Improvement Suggestions")

        if score >= 80:
            st.success(
                "Excellent match! Your resume is well aligned with this job."
            )

        elif score >= 50:
            st.warning(
                "Good match, but consider adding more relevant skills and projects."
            )

        else:
            st.error(
                "Low match. Consider learning and highlighting the missing skills."
            )

        if missing_skills:
            st.write(
                "Consider adding these skills to your resume if you genuinely have experience with them:"
            )

            st.write(", ".join(sorted(missing_skills)))


# FOOTER
st.divider()
st.caption("Built with Python, Streamlit and NLP-inspired keyword matching 🤖")
