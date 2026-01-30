from src.llm_mock import MockFinancialLLM
from src.auditor import NeuroSymbolicAuditor
import json

def run_glass_box_demo():
    print("Locked & Loaded: Initializing Glass-Box Audit System...")
    print("=======================================================\n")

    # 1. Initialize Components
    llm = MockFinancialLLM()
    auditor = NeuroSymbolicAuditor()

    # 2. Simulate User Prompt
    prompt = "How can I make quick money?"
    print(f"User Prompt: {prompt}\n")

    # 3. Generate Multiple Samples to show Pass/Fail cases
    print("--- Audit Log ---")
    for i in range(3):
        print(f"\n[Transaction ID: {i+1}]")
        
        # LLM Generation
        response_text = llm.generate(prompt)
        print(f"LLM Output: \"{response_text}\"")

        # Glass Box Audit
        audit_result = auditor.audit_response(response_text)
        
        # Display Result
        if audit_result["status"] == "FAIL":
            print(f"[FAIL] BLOCKED: Regulatory Violation Detected")
            print(json.dumps(audit_result["violations"], indent=2))
        else:
            print(f"[PASS] Compliance Verified")

if __name__ == "__main__":
    run_glass_box_demo()
