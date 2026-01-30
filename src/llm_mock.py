import random

class MockFinancialLLM:
    """
    Simulates a Large Language Model (e.g., GPT-4) generating financial advice.
    Used for demonstration without requiring API keys.
    """
    
    def __init__(self):
        self.responses = [
            "We can guarantee a 50% return on investment with our new crypto-arbitrage fund.",
            "Historical data shows this asset always goes up; it's a risk-free profit opportunity.",
            "You should consider diversifying your portfolio with index funds. Past performance is not a guide to future performance.",
            "Our savings account offers 5% APY. Your capital is at risk.",
        ]

    def generate(self, prompt: str) -> str:
        """
        Returns a random response from the preset list to simulate compliant and non-compliant outputs.
        """
        # In a real scenario, this would call OpenAI/Anthropic API
        return random.choice(self.responses)
