"""Simple calculator agent with tool-calling using LangGraph."""

from langchain_core.tools import tool
from langchain_core.language_model import LanguageModel


@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


# Create a list of all available tools
CALCULATOR_TOOLS = [add, subtract, multiply, divide]


def get_tool_by_name(name: str):
    """Get a tool by its name."""
    tools_dict = {tool.name: tool for tool in CALCULATOR_TOOLS}
    return tools_dict.get(name)
