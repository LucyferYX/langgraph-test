"""Calculator agent implementation using LangGraph."""

from typing import Annotated, Any
from langgraph.graph import StateGraph
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage
from langchain_core.language_model import LanguageModel
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

from calculator import CALCULATOR_TOOLS, get_tool_by_name


class AgentState(TypedDict):
    """State definition for the calculator agent."""
    messages: Annotated[list[BaseMessage], add_messages]


def create_calculator_agent(llm: LanguageModel):
    """Create a calculator agent that can use math tools."""
    
    # Bind tools to the LLM
    llm_with_tools = llm.bind_tools(CALCULATOR_TOOLS)
    
    def should_continue(state: AgentState) -> str:
        """Determine if we should continue or end."""
        messages = state["messages"]
        last_message = messages[-1]
        
        # If it's a tool message, continue to the agent
        if isinstance(last_message, ToolMessage):
            return "agent"
        
        # If the last message has tool calls, we go to tools
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "tools"
        
        # Otherwise, we're done
        return "end"
    
    def call_agent(state: AgentState) -> AgentState:
        """Call the LLM agent."""
        messages = state["messages"]
        response = llm_with_tools.invoke(messages)
        return {"messages": [response]}
    
    def call_tools(state: AgentState) -> AgentState:
        """Execute the tools requested by the agent."""
        messages = state["messages"]
        last_message = messages[-1]
        
        tool_results = []
        for tool_call in last_message.tool_calls:
            tool_name = tool_call["name"]
            tool_input = tool_call["args"]
            
            # Get and execute the tool
            tool = get_tool_by_name(tool_name)
            if tool:
                result = tool.invoke(tool_input)
                tool_results.append(
                    ToolMessage(
                        content=str(result),
                        tool_call_id=tool_call["id"],
                        name=tool_name,
                    )
                )
        
        return {"messages": tool_results}
    
    # Build the graph
    workflow = StateGraph(AgentState)
    
    # Add nodes
    workflow.add_node("agent", call_agent)
    workflow.add_node("tools", call_tools)
    
    # Add edges
    workflow.set_entry_point("agent")
    workflow.add_conditional_edges("agent", should_continue)
    workflow.add_edge("tools", "agent")
    
    # Compile the graph
    return workflow.compile()


# Example usage
if __name__ == "__main__":
    try:
        from langchain_anthropic import ChatAnthropic
        
        llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
        agent = create_calculator_agent(llm)
        
        # Test the agent
        result = agent.invoke({
            "messages": [HumanMessage(content="What is 25 * 4?")]
        })
        
        print("Agent response:")
        print(result["messages"][-1].content)
        
    except ImportError:
        print("Please install langchain-anthropic to run this example")
