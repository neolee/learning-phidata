from phi.agent.agent import Agent
from phi.tools.yfinance import YFinanceTools
import llm


agent = Agent(
    name="Finance Agent",
    model=llm.default, # type: ignore
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         company_info=True,
                         company_news=True)],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

q = "Summarize analyst recommendations for NVDA"

agent.print_response(q, stream=True)
