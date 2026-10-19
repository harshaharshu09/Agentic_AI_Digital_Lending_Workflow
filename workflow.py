from typing import Dict, Any

from agents.models import LoanApplication

from agents.intake_agent import IntakeValidationAgent
from agents.eligibility_agent import EligibilityAssessmentAgent
from agents.decision_agent import DecisionAgent
from agents.loan_offer_agent import LoanOfferAgent
from agents.risk_analysis_agent import RiskAnalysisAgent


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

    # Step 5: Risk Analysis
    risk_agent = RiskAnalysisAgent()

    risk_result = risk_agent.run(
        application,
        eligibility_result
    )

    # Final Workflow Result
    return {
        "status": decision_result["decision"],
        "validation": validation_result,
        "eligibility": eligibility_result,
        "decision": decision_result,
        "loan_offer": loan_offer_result,
        "risk_analysis": risk_result
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

    # Eligibility Output
    if "eligibility" in result:

        dti = (
            result["eligibility"]
            ["details"]
            ["affordability"]
            ["debt_to_income"]
        )

        print(
            f"Debt-to-Income Ratio: "
            f"{dti:.1%}"
        )

    # Loan Offer Output
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

    # Risk Analysis Output
    if "risk_analysis" in result:

        risk = result["risk_analysis"]

        print("\n=== AI Risk Analysis ===")

        print(
            f"Overall Risk: "
            f"{risk.get('overall_risk', 'N/A')}"
        )

        print(
            f"Recommendation: "
            f"{risk.get('recommendation', 'N/A')}"
        )

        print(
            f"Credit Risk: "
            f"{risk.get('credit_risk', 'N/A')}"
        )

        print(
            f"DTI Risk: "
            f"{risk.get('dti_risk', 'N/A')}"
        )

        print(
            f"Employment Risk: "
            f"{risk.get('employment_risk', 'N/A')}"
        )

        print(
            f"Loan Risk: "
            f"{risk.get('loan_risk', 'N/A')}"
        )

        print(
            f"Explanation: "
            f"{risk.get('explanation', 'N/A')}"
        )