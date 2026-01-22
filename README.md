# Glass Box Audit: Neuro-Symbolic Logic Layer for Financial LLMs

![Status](https://img.shields.io/badge/Status-Prototype-green)
![Topic](https://img.shields.io/badge/Topic-AI_Governance-blue)
![Tech](https://img.shields.io/badge/Tech-Neuro--Symbolic-purple)

## 🔬 Research Overview
This project implements a **"Glass Box" audit layer** designed to operationalize regulatory constraints (such as the **UK FCA Consumer Duty**) within autonomous financial agents.

Unlike "Black Box" approaches that rely solely on training data alignment (RLHF), this framework uses **deterministic symbolic logic** to verify LLM outputs *before* they are presented to the user.

### The Problem
Large Language Models (LLMs) used in finance are prone to:
1.  **Hallucinations:** Inventing financial products or rates.
2.  **Regulatory Breaches:** Failing to provide mandatory risk warnings.
3.  **Inconsistency:** Giving different advice for identical risk profiles.

### The Solution: Neuro-Symbolic Architecture
We propose a post-hoc logic layer that acts as a "Gatekeeper":
1.  **Neuro System (LLM):** Generates natural language financial advice.
2.  **Symbolic System (Audit Layer):** Parsers the output and validates it against hard-coded logic rules derived from regulations.
3.  **Outcome:** If the constraint is violated, the output is blocked or modified.

## 🛠 Project Structure
- `audit_engine.py`: The core symbolic logic engine that defines regulatory constraints.
- `llm_mock.py`: Simulates financial advice outputs (Simulating an LLM for testing).
- `compliance_rules.json`: A codified set of FCA-inspired rules.
- `demo.py`: Run this to see the "Glass Box" in action.

## 🚀 Getting Started

### Prerequisites
- Python 3.8+

### Installation
```bash
git clone https://github.com/rishisubedi/Glass-Box-Audit.git
cd Glass-Box-Audit
pip install -r requirements.txt
```

### Usage
Run the demonstration script:
```bash
python demo.py
```

## 📜 Example Rule (Pseudo-Code)
```python
IF user_risk_profile == "Low" AND advice_contains("Crypto"):
    BLOCK_RESPONSE()
    RETURN "Regulatory Violation: High-risk asset recommended to low-risk profile."
```

## 📚 Future Work
- Integration with LangChain for real-time interception.
- Expanding the rule base to include GDPR and MiFID II constraints.
