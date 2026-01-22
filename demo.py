from audit_engine import AuditEngine
from llm_mock import LLMMock
import time

def main():
    print("=================================================================")
    print("   GLASS BOX AUDIT: Neuro-Symbolic Gatekeeper Demo")
    print("=================================================================")
    print("Scenario: A 'Low Risk' customer asks for investment advice.")
    print("Constraint: NO high-risk assets (Crypto/Leverage) allowed.\n")

    # Initialize Systems
    auditor = AuditEngine()
    bot = LLMMock()
    
    user_profile = {"id": "user_123", "risk_tolerance": "Low"}
    prompt = "Where should I put my savings?"

    # Simulate 5 Interactions
    for i in range(1, 6):
        print(f"--- Interaction {i} ---")
        print(f"User > {prompt}")
        
        # 1. Neuro Step (LLM Generation)
        raw_response = bot.generate_response(prompt)
        print(f"[LLM Generating] ... '{raw_response}'")
        
        # 2. Symbolic Step (Audit)
        passed, status_msg, violations = auditor.audit_advice(user_profile, raw_response)
        
        if passed:
            print(f"[PASSED] AUDIT PASSED: Response sent to user.")
            print(f"Bot > {raw_response}")
        else:
            print(f"[BLOCKED] AUDIT BLOCKED: {status_msg}")
            for v in violations:
                print(f"   - {v}")
            print("Action: Fallback response sent.")
            print("Bot > I cannot provide that advice based on your risk profile.")
        
        print("\n")
        time.sleep(1)

if __name__ == "__main__":
    main()
