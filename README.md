# AI Resume Analyzer

A Python-based web application that analyzes a resume against a given job description. It extracts skills from a PDF resume, compares them with the skills mentioned in the job description, and provides a match percentage along with missing and matching skills.

## Features

* Upload a resume in PDF format
* Paste a job description
* Extract text from the resume
* Detect technical skills
* Compare resume skills with job requirements
* Calculate a match percentage
* Display matching and missing skills
* Provide basic suggestions for improving the resume

## Technologies Used

* Python
* Streamlit
* PyPDF2
* Regular Expressions

## How It Works

The application follows a simple process:

1. The user uploads a PDF resume.
2. The application extracts the text from the resume.
3. Technical skills are identified from the resume.
4. Skills are also identified from the job description.
5. The two sets of skills are compared.
6. A match percentage is calculated.
7. Matching skills, missing skills, and suggestions are displayed.

## Match Score

The match score is calculated based on the number of job-related skills found in the resume.

```text
Match Score = (Matching Skills / Job Description Skills) × 100
```

## Running the Project

First, install the required libraries:

```bash
pip install -r requirements.txt
```

Then run the application:

```bash
streamlit run app.py
```

The application will open in the browser.

## Project Structure

```text
AI-Resume-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Future Improvements

* Add semantic matching instead of basic keyword matching
* Use AI/LLM-based resume analysis
* Improve skill extraction
* Add resume recommendations
* Add charts and visual reports
* Deploy the application online

## Author

Sara Subhan

B.Tech Computer Science & Engineering


B.Tech Computer Science & Engineering Student

---

⭐ If you found this project interesting, consider giving the repository a star!
