from phi.agent.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import llm


model = llm.ollama

web_agent = Agent(
    name="Web Agent",
    role="Search the web for information",
    model=model, #type: ignore
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=model, # type: ignore
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         company_info=True,
                         company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    model=model, # type:ignore
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

q = "Summarize analyst recommendations for NVDA then search for the latest news about NVIDIA"

agent_team.print_response(q, stream=True)
