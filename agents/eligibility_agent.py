from typing import Dict, Any

from agents.models import LoanApplication


def calculate_affordability(application: LoanApplication) -> Dict[str, Any]:
    monthly_income = application.monthly_income
    existing_emi = application.existing_emi

    estimated_new_emi = (
        application.requested_loan / application.loan_term_months
    )

    total_emi = existing_emi + estimated_new_emi

    debt_to_income = total_emi / monthly_income

    return {
        "estimated_new_emi": round(estimated_new_emi, 2),
        "total_emi": round(total_emi, 2),
        "debt_to_income": round(debt_to_income, 3)
    }


def determine_eligibility(application: LoanApplication) -> Dict[str, Any]:

    affordability = calculate_affordability(application)

    reasons = []
    eligible = True

    if application.age < 21:
        eligible = False
        reasons.append(
            "Applicant age is below the preferred lending age."
        )

    if application.credit_score < 650:
        eligible = False
        reasons.append(
            "Credit score is below the preferred threshold."
        )

    if affordability["debt_to_income"] > 0.50:
        eligible = False
        reasons.append(
            "Debt-to-income ratio is too high."
        )

    if application.employment_years < 1:
        eligible = False
        reasons.append(
            "Employment stability is below the preferred threshold."
        )

    return {
        "eligible": eligible,
        "reasons": reasons,
        "affordability": affordability
    }


class EligibilityAssessmentAgent:

    def run(self, application: LoanApplication) -> Dict[str, Any]:

        result = determine_eligibility(application)

        if result["eligible"]:
            return {
                "agent": "Eligibility Assessment Agent",
                "status": "ELIGIBLE",
                "message": "Applicant meets the initial eligibility criteria.",
                "details": result
            }

        return {
            "agent": "Eligibility Assessment Agent",
            "status": "NOT_ELIGIBLE",
            "message": "Applicant does not meet the initial eligibility criteria.",
            "details": result
        }
