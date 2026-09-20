import re
import json
import os
from typing import Dict, List, Tuple

class AuditEngine:
    """
    The Symbolic Logic Layer.
    This class enforces deterministic rules on text input,
    dynamically loaded from external enterprise configurations.
    """

    def __init__(self, rules_path: str = "compliance_rules.json"):
        # Dynamic Rules Loading: Prevents hardcoded constraints and allows
        # compliance officers to update rules without redeploying code.
        self.rules_path = rules_path
        self._load_rules()

    def _load_rules(self):
        """Loads rules dynamically from JSON. Falls back to defaults if missing."""
        if os.path.exists(self.rules_path):
            with open(self.rules_path, "r", encoding="utf-8") as f:
                rules = json.load(f)
                self.forbidden_terms_low_risk = rules.get("forbidden_terms_low_risk", [])
                self.mandatory_warnings = rules.get("mandatory_warnings", {})
        else:
            print(f"Warning: {self.rules_path} not found. Using empty defaults.")
            self.forbidden_terms_low_risk = []
            self.mandatory_warnings = {}

    def audit_advice(self, user_profile: Dict, llm_response: str) -> Tuple[bool, str, List[str]]:
        """
        Audits the LLM response against the user's profile.
        Returns: (passed: bool, message: str, violations: List[str])
        """
        violations = []
        llm_response_lower = llm_response.lower()

        # --- RULE 1: Suitability Check (FCA Consumer Duty) ---
        if user_profile.get("risk_tolerance") == "Low":
            for term in self.forbidden_terms_low_risk:
                # OPTIMIZATION: Regex word boundary prevents false positives 
                # (e.g., 'cryptography' won't trigger 'crypto')
                if re.search(rf"\b{re.escape(term)}\b", llm_response_lower):
                    violations.append(f"VIOLATION: High-risk term '{term}' detected for Low-Risk user.")

        # --- RULE 2: Mandatory Disclosure Check ---
        for topic, warning in self.mandatory_warnings.items():
            if re.search(rf"\b{re.escape(topic)}\b", llm_response_lower):
                # Warning checks are usually substrings, but let's ensure it exists
                if warning.lower() not in llm_response_lower:
                    violations.append(f"VIOLATION: Missing mandatory warning for '{topic}'. Expected: '{warning}'.")

        if violations:
            return False, "Audit Failed: Regulatory Constraints Violated.", violations
        
        return True, "Audit Passed.", []

# Example Usage for Testing
if __name__ == "__main__":
    engine = AuditEngine()
    
    user = {"id": "1", "risk_tolerance": "Low", "vulnerable": True}
    risky_advice = "You should invest your savings in Crypto for 100x gains!"
    safe_advice = "Consider a high-interest savings account. Note: capital at risk applies to investments."
    false_positive_test = "Cryptography is an interesting topic for investment. Note: capital at risk."
    
    print("--- Test 1: Risky Advice ---")
    passed, msg, errors = engine.audit_advice(user, risky_advice)
    print(f"Result: {msg} | Errors: {errors}")
    
    print("\n--- Test 2: Safe Advice ---")
    passed, msg, errors = engine.audit_advice(user, safe_advice)
    print(f"Result: {msg} | Errors: {errors}")

    print("\n--- Test 3: False Positive Prevention (Cryptography) ---")
    passed, msg, errors = engine.audit_advice(user, false_positive_test)
    print(f"Result: {msg} | Errors: {errors}")
