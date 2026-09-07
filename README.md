# AI Resume Analyzer

A Python-based web application that analyzes a resume against a job description. It extracts relevant skills from a PDF resume, compares them with job requirements, and provides a match percentage along with matching skills, missing skills, and improvement suggestions.

## Screenshots

### App Overview

![App Overview](screenshots/app-overview.png)

### Results Overview

![Results Overview](screenshots/results-overview.png)

## Demo

The application takes two inputs:

- **Resume:** Upload a PDF resume
- **Job Description:** Paste the job description for the role you are applying for

For example, a user can upload a resume for a **Python Developer** position and paste a job description containing skills such as Python, SQL, Git, Flask, and REST APIs.

The application analyzes both inputs and displays:

- Resume-to-job match percentage
- Matching skills
- Missing skills
- Suggestions for improving the resume

## Features

- Upload resumes in PDF format
- Paste a job description
- Extract text from PDF resumes
- Detect relevant technical skills
- Compare resume skills with job requirements
- Calculate a match percentage
- Display matching and missing skills
- Provide basic resume improvement suggestions

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Regular Expressions

## How It Works

1. Upload a resume in PDF format.
2. The application extracts the resume text.
3. Relevant technical skills are detected.
4. Skills are identified from the job description.
5. Resume skills are compared with job requirements.
6. A match percentage is calculated.
7. Matching skills, missing skills, and suggestions are displayed.

## Match Score

The match score is calculated based on the number of job-related skills found in the resume.

```text
Match Score = (Matching Skills / Job Description Skills) × 100
Running the Project
1. Clone the repository
git clone https://github.com/Sara-png-ops/AI-Resume-Analyzer.git
2. Open the project folder
cd AI-Resume-Analyzer
3. Install dependencies
pip install -r requirements.txt
4. Run the application
streamlit run app.py

The application will open in your browser.

Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
    ├── app-overview.png
    └── results-overview.png
Future Improvements
Add semantic matching instead of basic keyword matching
Integrate AI/LLM-based resume analysis
Improve skill extraction
Add more detailed resume recommendations
Add charts and visual reports
Deploy the application online
Author

Sara Subhan

B.Tech Computer Science & Engineering

If you found this project useful, consider giving the repository a star.
