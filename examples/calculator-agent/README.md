# Calculator Agent

A simple LangGraph agent that performs mathematical calculations using tool-calling.

## Overview

This example demonstrates:
- Basic tool definition using `@tool` decorator
- Building a stateful agent with LangGraph
- Conditional routing based on agent decisions
- Tool execution and message handling

## Files

- **calculator.py** - Tool definitions (add, subtract, multiply, divide)
- **agent.py** - Agent implementation using LangGraph
- **README.md** - This file

## Usage

```python
from langchain_anthropic import ChatAnthropic
from agent import create_calculator_agent
from langchain_core.messages import HumanMessage

# Initialize LLM
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")

# Create agent
agent = create_calculator_agent(llm)

# Run agent
result = agent.invoke({
    "messages": [HumanMessage(content="What is 100 / 5?")]
})

print(result["messages"][-1].content)
```

## Requirements

- langchain-core
- langgraph
- langchain-anthropic (or any LLM provider)

## Features

✅ Add, subtract, multiply, and divide operations
✅ Stateful agent with message history
✅ Tool-based reasoning
✅ Error handling (division by zero)
