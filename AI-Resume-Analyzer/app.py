import streamlit as st
from pypdf import PdfReader

st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄")

st.title("📄 AI Resume Analyzer")
st.write("Upload your Resume PDF to get analysis.")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    reader = PdfReader(uploaded_file)
    resume_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text:
            resume_text += text

    st.success("Resume Uploaded Successfully!")

    if st.button("Analyze Resume"):

        text = resume_text.lower()

        skills = []

        keywords = [
            "python", "java", "c", "c++", "sql", "html", "css",
            "javascript", "react", "flask", "django", "machine learning",
            "deep learning", "tensorflow", "pandas", "numpy",
            "power bi", "excel", "git", "github"
        ]

        for skill in keywords:
            if skill in text:
                skills.append(skill.title())

        score = min(len(skills) * 5 + 40, 100)

        st.header("📊 Resume Analysis")

        st.subheader("💻 Skills Found")
        if skills:
            st.write(", ".join(skills))
        else:
            st.write("No technical skills detected.")

        st.subheader("⭐ Resume Score")
        st.write(f"{score}/100")

        st.subheader("🤖 ATS Score")
        st.write(f"{score-5}/100")

        st.subheader("💪 Strengths")
        if len(skills) >= 6:
            st.write("• Good technical skill set")
            st.write("• Resume contains multiple technologies")
        else:
            st.write("• Resume can include more technical skills")

        st.subheader("⚠ Weaknesses")

        if "internship" not in text:
            st.write("• Internship experience missing")

        if "project" not in text:
            st.write("• Projects section missing")

        if "certificate" not in text:
            st.write("• Certifications missing")

        st.subheader("📚 Recommended Skills")

        recommendations = [
            "Cloud Computing",
            "AWS",
            "Docker",
            "Kubernetes",
            "Communication Skills",
            "Problem Solving"
        ]

        for skill in recommendations:
            if skill.lower() not in text:
                st.write("•", skill)

        st.subheader("💼 Recommended Job Roles")

        if "machine learning" in text:
            st.write("• Machine Learning Engineer")

        if "python" in text:
            st.write("• Python Developer")

        if "sql" in text:
            st.write("• Data Analyst")

        if "react" in text:
            st.write("• Frontend Developer")

        st.subheader("🎯 Interview Questions")

        st.write("1. Tell me about yourself.")
        st.write("2. Explain your final year project.")
        st.write("3. What is Python?")
        st.write("4. Explain SQL JOIN.")
        st.write("5. Why should we hire you?")