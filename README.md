# Agentic AI Digital Lending Workflow

A modular Python application that demonstrates a digital lending workflow: application validation, eligibility checks, decision routing, risk analysis, and illustrative loan-offer generation.

## Live Demo

**Streamlit Application:** https://harshaharshu09-agentic-ai-digital-lending-workflow-app-jjk0mm.streamlit.app/

## Project Overview

This project simulates how a digital lending application can be processed through specialised agents. Each agent handles a defined task, while the workflow coordinates the results and routes the application to the next step.

The current version uses configurable, rule-based Python logic for eligibility and risk assessment. It does not call an external large language model or a real credit bureau. The outputs are intended for learning and demonstration, not real lending decisions.

## Workflow

```text
Applicant submits loan details
            |
            v
Intake and Validation Agent
            |
       Valid input?
        /       \
      No         Yes
      |           |
      v           v
REJECTED     Eligibility Assessment Agent
                  |
                  v
              Decision Agent
                  |
          +-------+--------+
          |                |
       APPROVED        HUMAN_REVIEW
          |                |
          v                v
    Loan Offer Agent   No offer generated
          |                |
          +-------+--------+
                  |
                  v
          Risk Analysis Agent
                  |
                  v
         Assessment results shown
             in Streamlit
```

The workflow stops at validation if the application contains invalid data. When validation passes, eligibility rules feed into the decision agent. An approved application receives an illustrative offer; a case requiring manual review does not receive an offer automatically. Risk analysis then summarises the applicant's financial profile.

## Agents and Responsibilities

### Intake and Validation Agent
Checks key application fields, including age, income, requested loan amount, tenure, and credit-score range.

### Eligibility Assessment Agent
Applies the project's configured demonstration rules using age, credit score, debt-to-income ratio, and employment experience.

### Decision Agent
Routes eligible cases to the offer path and sends cases that fail the configured eligibility criteria to human review. Validation failures are returned as rejected applications.

### Loan Offer Agent
For approved applications, calculates an illustrative monthly EMI, total interest, and total repayment using a configured annual interest rate of 10.5%.

### Risk Analysis Agent
Summarises credit, DTI, employment, and loan-to-income risk categories and returns an overall risk level, recommendation, and explanation. These are heuristic demonstration rules, not a validated credit-risk model.

## Key Features

- Applicant input through a Streamlit web interface
- Initial application validation
- Rule-based eligibility assessment
- Conditional decision routing and human-review status
- Debt-to-income ratio calculation
- Risk summaries for credit, DTI, employment, and loan size
- Illustrative EMI and total repayment calculation
- Streamlit results dashboard

## Technology Stack

- Python
- Streamlit
- Dataclasses and type annotations
- Rule-based decision logic
- Git and GitHub
- Streamlit Community Cloud

## Project Structure

```text
Agentic_AI_Digital_Lending_Workflow/
|
+-- agents/
|   +-- __init__.py
|   +-- models.py
|   +-- intake_agent.py
|   +-- eligibility_agent.py
|   +-- decision_agent.py
|   +-- loan_offer_agent.py
|   +-- risk_analysis_agent.py
|
+-- config/
|   +-- settings.py
|
+-- data/
|   +-- applications.json
|
+-- outputs/
|   +-- audit_log.json
|
+-- tools/
|   +-- __init__.py
|   +-- loan_calculator.py
|
+-- app.py
+-- workflow.py
+-- requirements.txt
+-- README.md
+-- .gitignore
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/harshaharshu09/Agentic_AI_Digital_Lending_Workflow.git
cd Agentic_AI_Digital_Lending_Workflow
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Launch the application

```powershell
python -m streamlit run app.py
```

You can also run the command-line workflow example:

```powershell
python workflow.py
```

## Example Scenario

The sample applicant used during development has monthly income of Rs. 80,000, existing EMI of Rs. 10,000, a requested loan of Rs. 8,00,000, a 60-month tenure, and a credit score of 720.

The demo calculates a debt-to-income ratio using the project's affordability calculation and generates an illustrative offer when the configured rules route the application to approval. The exact result depends on the inputs and rules in the current code.

## Limitations

- This is an educational prototype using synthetic sample details and heuristic rules.
- Eligibility thresholds, risk categories, and the illustrative interest rate are not financial advice and do not represent any bank's policy.
- No external LLM, real credit bureau, identity verification, or lender service is connected.
- The generated offer is not a binding offer or a real loan approval.
- The current workflow uses lightweight local files; it is not designed for production lending operations.

## Possible Enhancements

- Add a genuine LLM-assisted agent with transparent configuration and safe fallbacks
- Add tests for validation, approval, human review, and offer calculations
- Persist application history and audit events
- Add document checks, authentication, and role-based reviewer actions
- Integrate approved external data sources and explainable decision methods

## Author

**KN Harsha Vardhan Kumar**

GitHub: https://github.com/harshaharshu09

