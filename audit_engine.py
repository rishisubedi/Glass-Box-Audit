import re
from typing import Dict, List, Tuple

class AuditEngine:
    """
    The Symbolic Logic Layer.
    This class enforces deterministic rules on text input.
    """

    def __init__(self):
        # In a real system, these would be loaded from a knowledge base or ontology
        self.forbidden_terms_low_risk = ["crypto", "leverage", "100x", "options", "margin"]
        self.mandatory_warnings = {
            "investment": "capital at risk",
            "crypto": "unregulated asset",
            "loan": "your home may be repossessed"
        }

    def audit_advice(self, user_profile: Dict, llm_response: str) -> Tuple[bool, str, List[str]]:
        """
        Audits the LLM response against the user's profile.
        Returns: (passed: bool, message: str, violations: List[str])
        """
        violations = []
        llm_response_lower = llm_response.lower()

        # --- RULE 1: Suitability Check (FCA Consumer Duty) ---
        # Logic: If user is "Low Risk", they cannot be shown "High Risk" keywords.
        if user_profile.get("risk_tolerance") == "Low":
            for term in self.forbidden_terms_low_risk:
                if term in llm_response_lower:
                    violations.append(f"VIOLATION: High-risk term '{term}' detected for Low-Risk user.")

        # --- RULE 2: Mandatory Disclosure Check ---
        # Logic: If specific topics are mentioned, specific warnings MUST be present.
        for topic, warning in self.mandatory_warnings.items():
            if topic in llm_response_lower:
                if warning not in llm_response_lower:
                    violations.append(f"VIOLATION: Missing mandatory warning for '{topic}'. Expected: '{warning}'.")

        if violations:
            return False, "Audit Failed: Regulatory Constraints Violated.", violations
        
        return True, "Audit Passed.", []

# Example Usage for Testing
if __name__ == "__main__":
    engine = AuditEngine()
    
    # Test Case 1: Vulnerable Customer
    user = {"id": "1", "risk_tolerance": "Low", "vulnerable": True}
    
    risky_advice = "You should invest your savings in Crypto for 100x gains!"
    safe_advice = "Consider a high-interest savings account. Note: capital at risk applies to investments."
    
    print("--- Test 1: Risky Advice ---")
    passed, msg, errors = engine.audit_advice(user, risky_advice)
    print(f"Advice: {risky_advice}")
    print(f"Result: {msg}")
    print(f"Errors: {errors}")
    
    print("\n--- Test 2: Safe Advice ---")
    passed, msg, errors = engine.audit_advice(user, safe_advice)
    print(f"Advice: {safe_advice}")
    print(f"Result: {msg}")
    print(f"Errors: {errors}")
