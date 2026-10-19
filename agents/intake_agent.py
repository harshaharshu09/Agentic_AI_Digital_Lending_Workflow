from typing import Dict, Any

from agents.models import LoanApplication


def validate_application(application: LoanApplication) -> Dict[str, Any]:
    errors = []

    if application.age < 18:
        errors.append("Applicant must be at least 18 years old.")

    if application.monthly_income <= 0:
        errors.append("Monthly income must be greater than zero.")

    if application.requested_loan <= 0:
        errors.append("Requested loan amount must be greater than zero.")

    if application.loan_term_months <= 0:
        errors.append("Loan term must be greater than zero.")

    if not 300 <= application.credit_score <= 900:
        errors.append("Credit score must be between 300 and 900.")

    return {
        "valid": len(errors) == 0,
        "errors": errors
    }


class IntakeValidationAgent:

    def run(self, application: LoanApplication) -> Dict[str, Any]:
        validation = validate_application(application)

        if validation["valid"]:
            return {
                "agent": "Intake & Validation Agent",
                "status": "VALID",
                "message": "Application passed initial validation.",
                "errors": []
            }

        return {
            "agent": "Intake & Validation Agent",
            "status": "INVALID",
            "message": "Application failed initial validation.",
            "errors": validation["errors"]
        }
