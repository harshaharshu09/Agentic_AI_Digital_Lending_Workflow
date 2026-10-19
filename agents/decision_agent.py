from typing import Dict, Any


class DecisionAgent:

    def run(
        self,
        eligibility_result: Dict[str, Any]
    ) -> Dict[str, Any]:

        if eligibility_result["status"] == "ELIGIBLE":

            return {
                "agent": "Decision Agent",
                "decision": "APPROVED",
                "route": "AUTOMATED",
                "message": "Application can proceed to loan offer generation."
            }

        return {
            "agent": "Decision Agent",
            "decision": "HUMAN_REVIEW",
            "route": "MANUAL",
            "message": "Application requires human review before a final decision."
        }
