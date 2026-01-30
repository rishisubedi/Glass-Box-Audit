from typing import List, Dict
from .rules import ACTIVE_RULES, AuditRule

class NeuroSymbolicAuditor:
    """
    The 'Glass Box' layer. 
    It intercepts LLM outputs and applies symbolic logic rules to ensure regulatory compliance.
    """
    
    def __init__(self):
        self.rules = ACTIVE_RULES

    def audit_response(self, text: str) -> Dict:
        """
        Scans the text for rule violations and required disclosures.
        Returns a dictionary containing the audit result.
        """
        violations = []
        text_lower = text.lower()
        
        for rule in self.rules:
            # Check for forbidden concepts (Simplistic keyword matching for demo)
            # In production, this would use a NLI (Natural Language Inference) model
            for concept in rule.forbidden_concepts:
                if concept in text_lower:
                    violations.append({
                        "rule_id": rule.id,
                        "type": "FORBIDDEN_CONCEPT",
                        "concept": concept,
                        "severity": rule.severity,
                        "message": rule.description
                    })

            # Check for required concepts
            # If a Forbidden concept is NOT found, we might still check for required disclaimers if context matches
            # For this demo, we check if required concepts are missing ONLY if the rule implies specific context
            # (Simplified logic: if any forbidden concept is found, that's a violation. 
            #  If no forbidden concept, check standard requirements like 'risk warning' if it looks like advice)
            
            # Simple check: If the text contains "return" or "profit", it MUST have a risk warning
            if "return" in text_lower or "profit" in text_lower:
                 for req in rule.required_concepts:
                    if req not in text_lower and "risk" not in text_lower: # broadly checking for 'risk'
                         violations.append({
                            "rule_id": rule.id,
                            "type": "MISSING_DISCLAIMER",
                            "concept": req,
                            "severity": rule.severity,
                            "message": f"Financial promotion missing required disclaimer: '{req}'"
                        })

        status = "FAIL" if violations else "PASS"
        
        return {
            "status": status,
            "violations": violations,
            "original_text": text
        }
