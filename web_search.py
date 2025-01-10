from phi.agent.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
import llm


agent = Agent(
    name="Web Agent",
    model=llm.default, #type: ignore
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

q = "Tell me about NVIDIA's Digits computer"

agent.print_response(q)
