from typing import Dict, Any

from agents.models import LoanApplication


class LoanOfferAgent:

    def run(
        self,
        application: LoanApplication,
        decision_result: Dict[str, Any]
    ) -> Dict[str, Any]:

        if decision_result["decision"] != "APPROVED":
            return {
                "agent": "Loan Offer Agent",
                "status": "NOT_GENERATED",
                "message": "Loan offer cannot be generated before approval."
            }

        loan_amount = application.requested_loan
        tenure = application.loan_term_months

        annual_interest_rate = 10.5
        monthly_interest_rate = annual_interest_rate / 100 / 12

        monthly_emi = (
            loan_amount * monthly_interest_rate
            * (1 + monthly_interest_rate) ** tenure
            / (
                (1 + monthly_interest_rate) ** tenure - 1
            )
        )

        total_payment = monthly_emi * tenure
        total_interest = total_payment - loan_amount

        return {
            "agent": "Loan Offer Agent",
            "status": "OFFER_GENERATED",
            "loan_amount": round(loan_amount, 2),
            "tenure_months": tenure,
            "interest_rate": annual_interest_rate,
            "monthly_emi": round(monthly_emi, 2),
            "total_interest": round(total_interest, 2),
            "total_payment": round(total_payment, 2),
            "message": "Loan offer generated successfully."
        }
