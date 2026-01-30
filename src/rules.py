from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AuditRule:
    """
    Represents a symbolic rule derived from regulatory frameworks (e.g., FCA Consumer Duty).
    """
    id: str
    description: str
    forbidden_concepts: List[str]
    required_concepts: List[str]
    severity: str  # "CRITICAL", "WARNING", "INFO"

# --- FCA Consumer Duty: Financial Promotions Rules ---

RULE_FCA_001 = AuditRule(
    id="FCA-FIN-PROM-001",
    description="Prohibits guaranteeing returns without risk warnings.",
    forbidden_concepts=["guaranteed returns", "risk-free profit", "certainty of gain"],
    required_concepts=["risk warning", "capital at risk"],
    severity="CRITICAL"
)

RULE_FCA_002 = AuditRule(
    id="FCA-FIN-PROM-002",
    description="Ensures clarity on past performance not indicating future results.",
    forbidden_concepts=["past performance guarantees future"],
    required_concepts=["past performance disclaimer"],
    severity="WARNING"
)

# Registry of active rules
ACTIVE_RULES = [RULE_FCA_001, RULE_FCA_002]
