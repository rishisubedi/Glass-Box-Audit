import random

class LLMMock:
    """
    Simulates a stochastic LLM (Large Language Model).
    It generates random financial advice, some of which is compliant, some is not.
    """
    
    def __init__(self):
        self.responses = [
            "We recommend a diversified portfolio of index funds. Remember, your capital at risk.",
            "You should definitely buy this new Crypto coin! It's going to the moon!",
            "Savings accounts are safe, but have you considered high-leverage options trading?",
            "For your retirement, a government bond is suitable.",
            "Investing involves risk. Ensure you understand that your capital at risk."
        ]

    def generate_response(self, prompt: str) -> str:
        # Simulate "thinking" based on prompt, but just return random for demo
        return random.choice(self.responses)
