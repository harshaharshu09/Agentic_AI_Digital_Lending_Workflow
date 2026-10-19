from typing import Dict


class LoanCalculator:
    """
    Calculates basic loan affordability metrics
    for the lending workflow.
    """

    def calculate_emi(
        self,
        loan_amount: float,
        annual_interest_rate: float,
        tenure_months: int
    ) -> float:
        monthly_rate = annual_interest_rate / (12 * 100)

        if monthly_rate == 0:
            return loan_amount / tenure_months

        emi = (
            loan_amount
            * monthly_rate
            * (1 + monthly_rate) ** tenure_months
        ) / (
            (1 + monthly_rate) ** tenure_months - 1
        )

        return round(emi, 2)

    def calculate_dti(
        self,
        monthly_income: float,
        existing_emi: float,
        new_emi: float
    ) -> float:
        if monthly_income <= 0:
            return 1.0

        total_emi = existing_emi + new_emi
        return round(total_emi / monthly_income, 3)

    def calculate_affordability(
        self,
        monthly_income: float,
        existing_emi: float,
        new_emi: float
    ) -> Dict[str, float]:
        dti = self.calculate_dti(
            monthly_income,
            existing_emi,
            new_emi
        )

        return {
            "total_emi": round(existing_emi + new_emi, 2),
            "debt_to_income": dti,
            "remaining_income": round(
                monthly_income - existing_emi - new_emi,
                2
            )
        }