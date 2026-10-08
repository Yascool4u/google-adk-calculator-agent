import os
from dotenv import load_dotenv
from google.adk.agents import Agent
# from google.adk.tools import tool

load_dotenv()

model_name="gemini-3.5-flash"

# ==========================================
# 1. Define Tools with the @tool Decorator
# ==========================================

def add(a: float, b: float) -> float:
    """Adds two numbers together."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first number."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divides the first number by the second number."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

# ==========================================
# 2. Define Specialist Worker Agents
# ==========================================

addition_agent = Agent(
    name="AdditionAgent",
    model=model_name,
    instruction="You perform addition using the add tool.",
    tools=[add]  # Pass the decorated function directly
)

subtraction_agent = Agent(
    name="SubtractionAgent",
    model=model_name,
    instruction="You perform subtraction using the subtract tool.",
    tools=[subtract]
)

multiplication_agent = Agent(
    name="MultiplicationAgent",
    model=model_name,
    instruction="You perform multiplication using the multiply tool.",
    tools=[multiply]
)

division_agent = Agent(
    name="DivisionAgent",
    model=model_name,
    instruction="You perform division using the divide tool.",
    tools=[divide]
)

# ==========================================
# 3. Supervisor Agent & Execution
# ==========================================

root_agent = Agent(
    name="calculator_agent",
    model=model_name,
    instruction=(
        "Break down complex math queries into single operations, delegate "
        "to sub-agents, and aggregate the results."
    ),
    sub_agents=[
        addition_agent,
        subtraction_agent,
        multiplication_agent,
        division_agent
    ]
)

# if __name__ == "__main__":
#     response = supervisor_agent.run("Calculate (15 * 4) + (100 / 5) - 12")
#     print(response.text)