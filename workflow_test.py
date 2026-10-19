from workflow import LoanApplication, run_complete_lending_workflow


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


result = run_complete_lending_workflow(sample_application)


print("\n=== Agentic AI Digital Lending Workflow ===")
print(f"Applicant: {sample_application.applicant_name}")
print(f"Final Decision: {result['status']}")


if result["status"] == "APPROVED":
    print("Next Action: Application can proceed to loan offer generation.")

elif result["status"] == "HUMAN_REVIEW":
    print("Next Action: Application requires human review before a final decision.")

else:
    print("Next Action: Application cannot proceed.")


# Display Debt-to-Income Ratio
if "eligibility" in result:
    eligibility = result["eligibility"]

    if "affordability" in eligibility:
        dti = eligibility["affordability"]["debt_to_income"]
        print(f"Debt-to-Income Ratio: {dti:.1%}")


# Display Loan Offer
if "loan_offer" in result:
    offer = result["loan_offer"]

    print("\n=== Loan Offer ===")
    print(f"Loan Amount: ₹{offer['loan_amount']:,.2f}")
    print(f"Tenure: {offer['tenure_months']} months")
    print(f"Interest Rate: {offer['interest_rate']}%")
    print(f"Monthly EMI: ₹{offer['monthly_emi']:,.2f}")
    print(f"Total Interest: ₹{offer['total_interest']:,.2f}")
    print(f"Total Payment: ₹{offer['total_payment']:,.2f}")