from phi.agent.agent import Agent
from phi.model.openai.like import OpenAILike
from phi.tools.duckduckgo import DuckDuckGo


model = OpenAILike(
    id="qwen2.5-coder-32b-instruct-mlx",
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
)

agent = Agent(
    name="Web Agent",
    model=model, #type: ignore
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

q = "Tell me about NVIDIA's Digits"

agent.print_response(q)
