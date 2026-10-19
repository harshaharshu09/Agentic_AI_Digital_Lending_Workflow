# 🤖 Agentic AI Digital Lending Workflow

An AI-powered digital lending workflow that automates loan application validation, eligibility assessment, decision making, risk analysis, and loan offer generation using a multi-agent architecture.

## 🚀 Live Demo

🔗 **Streamlit App:** https://harshaharshu09-agentic-ai-digital-lending-workflow-app-jjk0mm.streamlit.app/

## 📌 Project Overview

The Agentic AI Digital Lending Workflow is an intelligent loan assessment system where multiple specialized agents work together to evaluate loan applications.

The workflow validates applicant information, assesses eligibility, makes lending decisions, performs detailed risk analysis, and generates loan offers for eligible applicants.

## 🎯 Objectives

- Automate the digital lending assessment process
- Evaluate borrower eligibility using financial and employment information
- Support consistent lending decisions
- Analyze credit, DTI, employment, and loan-related risks
- Generate personalized loan offers
- Provide an interactive Streamlit application

## ✨ Key Features

- 📝 Application Intake & Validation
- 🔍 Eligibility Assessment
- ⚖️ Automated Decision Making
- 🤖 AI Risk Analysis
- 💰 Loan Offer Generation
- 📊 Debt-to-Income Ratio Analysis
- 👤 Human Review Handling
- 🖥️ Interactive Streamlit Dashboard

## 🧠 Agentic AI Workflow

Applicant
↓
Intake & Validation Agent
↓
Eligibility Assessment Agent
↓
Decision Agent
↓
Risk Analysis Agent
↓
Loan Offer Agent
↓
Final Lending Outcome

Each agent performs a dedicated responsibility within the lending workflow, making the system modular and scalable.

## 🔎 Risk Analysis

The Risk Analysis Agent evaluates:

- Overall Risk
- Credit Risk
- DTI Risk
- Employment Risk
- Loan Risk

It also provides a recommendation and explanation based on the applicant's financial profile.

## 💰 Loan Offer Generation

For approved applications, the Loan Offer Agent generates:

- Loan Amount
- Loan Tenure
- Interest Rate
- Monthly EMI
- Total Interest
- Total Payment

Applications requiring additional assessment can be routed for human review instead of automatically generating a loan offer.

## 🖥️ Streamlit Application

The interactive Streamlit application allows users to enter:

- Applicant Name
- Age
- Monthly Income
- Employment Type
- Employment Experience
- Requested Loan Amount
- Existing EMI
- Loan Tenure
- Credit Score

The application displays the lending decision, DTI ratio, eligibility assessment, risk analysis, and loan offer details.

## 📂 Project Structure

Agentic_AI_Digital_Lending_Workflow/
│
├── agents/
│   ├── __init__.py
│   ├── intake_agent.py
│   ├── eligibility_agent.py
│   ├── decision_agent.py
│   ├── risk_analysis_agent.py
│   ├── loan_offer_agent.py
│   └── models.py
│
├── config/
│   └── settings.py
│
├── data/
│   └── applications.json
│
├── outputs/
│   └── audit_log.json
│
├── tools/
│   ├── __init__.py
│   └── loan_calculator.py
│
├── app.py
├── workflow.py
├── workflow_test.py
├── requirements.txt
├── README.md
└── .gitignore

## ⚙️ Technologies Used

- Python
- Streamlit
- Agentic AI Architecture
- Object-Oriented Programming
- Financial Risk Analysis
- Loan EMI Calculation
- JSON
- Git & GitHub

## 🛠️ Installation

Clone the repository:

git clone https://github.com/harshaharshu09/Agentic_AI_Digital_Lending_Workflow.git

Navigate to the project:

cd Agentic_AI_Digital_Lending_Workflow

Create a virtual environment:

python -m venv .venv

Activate the environment on Windows:

.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

## ▶️ Run the Application

Start the Streamlit application:

streamlit run app.py

The application will open in your web browser.

## 🧪 Workflow Testing

Run the core lending workflow directly:

python workflow.py

## 📊 Example Workflow Output

Applicant: Rahul
Final Decision: APPROVED
Debt-to-Income Ratio: 29.2%

Loan Amount: ₹800,000.00
Tenure: 60 months
Interest Rate: 10.5%
Monthly EMI: ₹17,195.12
Total Interest: ₹231,707.22
Total Payment: ₹1,031,707.22

The risk analysis also provides overall risk, credit risk, DTI risk, employment risk, loan risk, recommendation, and explanation.

## 🔮 Future Enhancements

- Integration with real credit bureau APIs
- Machine learning-based credit scoring
- Explainable AI for lending decisions
- Database integration
- Authentication and role-based access
- Loan application history and analytics
- Cloud deployment
- Advanced fraud detection
- Automated document verification

## ⚠️ Disclaimer

This project is an educational and demonstration system designed to simulate a digital lending workflow. It is not intended to provide real-world financial or lending decisions.

## 👨‍💻 Author

**KN Harsha Vardhan Kumar**

GitHub: https://github.com/harshaharshu09

---

⭐ If you find this project useful, consider giving it a star!
