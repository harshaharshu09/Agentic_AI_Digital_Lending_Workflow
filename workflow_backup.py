from typing import Dict, Any

from agents.models import LoanApplication

from agents.intake_agent import IntakeValidationAgent
from agents.eligibility_agent import EligibilityAssessmentAgent
from agents.decision_agent import DecisionAgent
from agents.loan_offer_agent import LoanOfferAgent


def run_complete_lending_workflow(
    application: LoanApplication
) -> Dict[str, Any]:

    # Step 1: Intake and Validation
    intake_agent = IntakeValidationAgent()
    validation_result = intake_agent.run(application)

    if validation_result["status"] == "INVALID":
        return {
            "status": "REJECTED",
            "stage": "VALIDATION",
            "validation": validation_result
        }

    # Step 2: Eligibility Assessment
    eligibility_agent = EligibilityAssessmentAgent()
    eligibility_result = eligibility_agent.run(application)

    # Step 3: Decision
    decision_agent = DecisionAgent()
    decision_result = decision_agent.run(eligibility_result)

    # Step 4: Loan Offer Generation
    if decision_result["decision"] == "APPROVED":

        loan_offer_agent = LoanOfferAgent()

        loan_offer_result = loan_offer_agent.run(
            application,
            decision_result
        )

    else:

        loan_offer_result = {
            "agent": "Loan Offer Agent",
            "status": "NOT_GENERATED",
            "message": "Loan offer is waiting for human review."
        }

    return {
        "status": decision_result["decision"],
        "validation": validation_result,
        "eligibility": eligibility_result,
        "decision": decision_result,
        "loan_offer": loan_offer_result
    }


if __name__ == "__main__":

    sample_application = LoanApplication(
        applicant_name="Rahul",
        age=29,
        monthly_income=80000,
        employment_type="Salaried",
        employment_years=5,
        requested_loan=800000,
        existing_emi=10000,
        loan_term_months=60,
        credit_score=720
    )

    result = run_complete_lending_workflow(
        sample_application
    )

    print("\n=== Agentic AI Digital Lending Workflow ===")

    print(
        f"Applicant: "
        f"{sample_application.applicant_name}"
    )

    print(
        f"Final Decision: "
        f"{result['status']}"
    )

    print(
        f"Next Action: "
        f"{result['decision']['message']}"
    )

    if "eligibility" in result:

        dti = result["eligibility"]["details"]["affordability"]["debt_to_income"]

        print(
            f"Debt-to-Income Ratio: "
            f"{dti:.1%}"
        )

    if "loan_offer" in result:

        offer = result["loan_offer"]

        if offer["status"] == "OFFER_GENERATED":

            print("\n=== Loan Offer ===")

            print(
                f"Loan Amount: "
                f"₹{offer['loan_amount']:,.2f}"
            )

            print(
                f"Tenure: "
                f"{offer['tenure_months']} months"
            )

            print(
                f"Interest Rate: "
                f"{offer['interest_rate']}%"
            )

            print(
                f"Monthly EMI: "
                f"₹{offer['monthly_emi']:,.2f}"
            )

            print(
                f"Total Interest: "
                f"₹{offer['total_interest']:,.2f}"
            )

            print(
                f"Total Payment: "
                f"₹{offer['total_payment']:,.2f}"
            )

            print(
                offer["message"]
            )
