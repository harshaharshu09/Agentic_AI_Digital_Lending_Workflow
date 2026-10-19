import streamlit as st

from agents.models import LoanApplication
from agents.intake_agent import IntakeValidationAgent
from agents.eligibility_agent import EligibilityAssessmentAgent
from agents.decision_agent import DecisionAgent
from agents.loan_offer_agent import LoanOfferAgent
from agents.risk_analysis_agent import RiskAnalysisAgent

st.set_page_config(
    page_title="Agentic AI Digital Lending",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Agentic AI Digital Lending Workflow")
st.caption("AI-powered loan application assessment, risk analysis and offer generation")

st.divider()

st.header("👤 Applicant Details")

col1, col2 = st.columns(2)

with col1:
    applicant_name = st.text_input("Applicant Name", "Rahul")
    age = st.number_input("Age", min_value=18, max_value=100, value=29)
    monthly_income = st.number_input("Monthly Income (₹)", min_value=1.0, value=80000.0)
    employment_type = st.selectbox(
        "Employment Type",
        ["Salaried", "Self-Employed", "Business"]
    )
    employment_years = st.number_input(
        "Employment Experience (Years)",
        min_value=0.0,
        value=5.0
    )

with col2:
    requested_loan = st.number_input(
        "Requested Loan Amount (₹)",
        min_value=1.0,
        value=800000.0
    )
    existing_emi = st.number_input(
        "Existing EMI (₹)",
        min_value=0.0,
        value=10000.0
    )
    loan_term_months = st.selectbox(
        "Loan Tenure",
        [12, 24, 36, 48, 60, 72, 84],
        index=4
    )
    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=720
    )

st.divider()

if st.button("🚀 Assess Loan Application", type="primary", use_container_width=True):

    application = LoanApplication(
        applicant_name=applicant_name,
        age=age,
        monthly_income=monthly_income,
        employment_type=employment_type,
        employment_years=employment_years,
        requested_loan=requested_loan,
        existing_emi=existing_emi,
        loan_term_months=loan_term_months,
        credit_score=credit_score
    )

    # Step 1: Validation
    intake_agent = IntakeValidationAgent()
    validation_result = intake_agent.run(application)

    if validation_result["status"] == "INVALID":

        st.error("❌ LOAN APPLICATION REJECTED")

        for error in validation_result.get("errors", []):
            st.write(f"• {error}")

        st.stop()

    # Step 2: Eligibility
    eligibility_agent = EligibilityAssessmentAgent()
    eligibility_result = eligibility_agent.run(application)

    # Step 3: Decision
    decision_agent = DecisionAgent()
    decision_result = decision_agent.run(eligibility_result)

    # Step 4: Loan Offer
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

    # ==============================
    # RESULTS
    # ==============================

    st.divider()
    st.header("📊 Loan Assessment Result")

    if decision_result["decision"] == "APPROVED":
        st.success("✅ LOAN APPLICATION APPROVED")
    else:
        st.warning("⚠️ APPLICATION REQUIRES HUMAN REVIEW")

    st.write(f"**Applicant:** {application.applicant_name}")
    st.write(f"**Final Decision:** {decision_result['decision']}")

    st.info(decision_result["message"])

    dti = (
        eligibility_result
        .get("details", {})
        .get("affordability", {})
        .get("debt_to_income", 0)
    )

    st.metric("Debt-to-Income Ratio", f"{dti:.1%}")

    # Eligibility
    st.subheader("🔍 Eligibility Assessment")

    e1, e2, e3 = st.columns(3)

    with e1:
        st.metric("Credit Score", application.credit_score)

    with e2:
        st.metric("Monthly Income", f"₹{application.monthly_income:,.0f}")

    with e3:
        st.metric("Employment Experience", f"{application.employment_years} years")

    # Risk Analysis
    st.subheader("🤖 AI Risk Analysis")

    r1, r2, r3, r4 = st.columns(4)

    with r1:
        st.metric("Overall Risk", risk_result.get("overall_risk", "N/A"))

    with r2:
        st.metric("Credit Risk", risk_result.get("credit_risk", "N/A"))

    with r3:
        st.metric("DTI Risk", risk_result.get("dti_risk", "N/A"))

    with r4:
        st.metric("Employment Risk", risk_result.get("employment_risk", "N/A"))

    st.info(
        f"**Recommendation:** {risk_result.get('recommendation', 'N/A')}"
    )

    st.write(
        f"**Loan Risk:** {risk_result.get('loan_risk', 'N/A')}"
    )

    st.write(
        f"**Explanation:** {risk_result.get('explanation', 'N/A')}"
    )

    # Loan Offer
    if loan_offer_result.get("status") == "OFFER_GENERATED":

        st.subheader("💰 Loan Offer")

        o1, o2, o3 = st.columns(3)

        with o1:
            st.metric(
                "Loan Amount",
                f"₹{loan_offer_result['loan_amount']:,.2f}"
            )

        with o2:
            st.metric(
                "Monthly EMI",
                f"₹{loan_offer_result['monthly_emi']:,.2f}"
            )

        with o3:
            st.metric(
                "Interest Rate",
                f"{loan_offer_result['interest_rate']}%"
            )

        o4, o5, o6 = st.columns(3)

        with o4:
            st.metric(
                "Tenure",
                f"{loan_offer_result['tenure_months']} months"
            )

        with o5:
            st.metric(
                "Total Interest",
                f"₹{loan_offer_result['total_interest']:,.2f}"
            )

        with o6:
            st.metric(
                "Total Payment",
                f"₹{loan_offer_result['total_payment']:,.2f}"
            )

        st.success("🎉 Loan offer generated successfully.")

    else:
        st.warning(loan_offer_result.get("message", "Loan offer not generated."))
