# 🤖 AI Resume Analyzer

An AI-powered resume analysis web application built with **Python and Streamlit** that compares a candidate's resume with a job description, identifies matching and missing skills, and generates a resume match score.

## 🚀 Project Overview

Finding out whether a resume matches a particular job description can be time-consuming.

**AI Resume Analyzer** simplifies this process by allowing users to upload their resume as a PDF and paste a job description. The application analyzes both and provides an easy-to-understand compatibility report.

### ✨ Key Features

* 📄 Upload PDF resumes
* 💼 Enter a job description
* 🔍 Automatically extract resume text
* 🧠 Detect relevant technical skills
* ✅ Identify matching skills
* ❌ Identify missing skills
* 📊 Calculate a resume-to-job match percentage
* 💡 Provide personalized improvement suggestions
* ⚡ Simple and interactive Streamlit interface

## 🛠️ Technologies Used

* **Python**
* **Streamlit**
* **PyPDF2**
* **Regular Expressions**
* **Keyword-based NLP techniques**

## ⚙️ How It Works

```text
Resume PDF
     ↓
Text Extraction
     ↓
Skill Detection
     ↓
        ← Job Description
              ↓
        Skill Detection
              ↓
     Skill Comparison
              ↓
       Match Score
              ↓
 Matching + Missing Skills
              ↓
    Improvement Suggestions
```

## 📊 Match Score

The application calculates the percentage of job-description skills that are also found in the resume.

```text
Match Score =
(Matching Skills / Job Description Skills) × 100
```

The result is displayed as a percentage along with matching and missing skills.

## 💻 Installation

Clone this repository:

```bash
git clone https://github.com/YOUR-USERNAME/AI-Resume-Analyzer.git
```

Move into the project directory:

```bash
cd AI-Resume-Analyzer
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your browser.

## 📂 Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    └── resume-analyzer.png
```

## 🎯 Example Use Case

A student or job seeker can:

1. Upload their resume.
2. Paste a software developer job description.
3. Analyze the resume.
4. View the overall match percentage.
5. Identify skills already matching the position.
6. Discover skills that may need to be highlighted or developed.

## 🔮 Future Improvements

* 🤖 Integrate an LLM for deeper resume analysis
* 📌 Detect skills using semantic similarity instead of only keywords
* 📝 Provide AI-generated resume improvement suggestions
* 🎯 Support multiple job descriptions
* 📈 Add visual analytics and skill charts
* ☁️ Deploy the application online
* 📑 Generate an automated resume analysis report

## 👩‍💻 Author

**Sara Subhan**

B.Tech Computer Science & Engineering Student

---

⭐ If you found this project interesting, consider giving the repository a star!
