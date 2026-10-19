from dataclasses import dataclass


@dataclass
class LoanApplication:
    applicant_name: str
    age: int
    monthly_income: float
    employment_type: str
    employment_years: float
    requested_loan: float
    existing_emi: float
    loan_term_months: int
    credit_score: int
