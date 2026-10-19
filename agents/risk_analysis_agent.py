from typing import Dict, Any

from agents.models import LoanApplication


class RiskAnalysisAgent:

    def run(
        self,
        application: LoanApplication,
        eligibility_result: Dict[str, Any]
    ) -> Dict[str, Any]:

        credit_score = application.credit_score
        monthly_income = application.monthly_income
        existing_emi = application.existing_emi
        requested_loan = application.requested_loan
        employment_years = application.employment_years

        affordability = eligibility_result.get("details", {}).get(
            "affordability", {}
        )

        debt_to_income = affordability.get("debt_to_income", 0)

        # Credit Risk
        if credit_score >= 750:
            credit_risk = "LOW"
        elif credit_score >= 650:
            credit_risk = "MEDIUM"
        else:
            credit_risk = "HIGH"

        # DTI Risk
        if debt_to_income <= 0.35:
            dti_risk = "LOW"
        elif debt_to_income <= 0.50:
            dti_risk = "MEDIUM"
        else:
            dti_risk = "HIGH"

        # Employment Risk
        if employment_years >= 3:
            employment_risk = "LOW"
        elif employment_years >= 1:
            employment_risk = "MEDIUM"
        else:
            employment_risk = "HIGH"

        # Loan Risk
        loan_to_income = requested_loan / monthly_income

        if loan_to_income <= 10:
            loan_risk = "LOW"
        elif loan_to_income <= 15:
            loan_risk = "MEDIUM"
        else:
            loan_risk = "HIGH"

        # Overall Risk
        risk_levels = [
            credit_risk,
            dti_risk,
            employment_risk,
            loan_risk
        ]

        if "HIGH" in risk_levels:
            overall_risk = "HIGH"
            recommendation = "Manual review recommended."
        elif risk_levels.count("MEDIUM") >= 2:
            overall_risk = "MEDIUM"
            recommendation = "Proceed with additional verification."
        else:
            overall_risk = "LOW"
            recommendation = "Application appears financially stable."

        explanation = (
            f"Credit score is {credit_score}, "
            f"debt-to-income ratio is {debt_to_income:.1%}, "
            f"employment experience is {employment_years} years, "
            f"and requested loan is ₹{requested_loan:,.2f} "
            f"against monthly income of ₹{monthly_income:,.2f}."
        )

        return {
            "agent": "Risk Analysis Agent",
            "overall_risk": overall_risk,
            "recommendation": recommendation,
            "credit_risk": credit_risk,
            "dti_risk": dti_risk,
            "employment_risk": employment_risk,
            "loan_risk": loan_risk,
            "explanation": explanation
        }
