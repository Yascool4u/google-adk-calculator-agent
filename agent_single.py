import os
from dotenv import load_dotenv
from google.adk.agents import Agent
# from google.adk.tools import tool

load_dotenv()

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

root_agent = Agent(
    name="calculator_agent",
    model="gemini-3.5-flash",
    instruction=(
        "Answer user questions using available math tools"
    ),
    tools = [add, subtract, multiply, divide]
)