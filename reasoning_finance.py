from phi.agent.agent import Agent
from phi.tools.yfinance import YFinanceTools
import llm


reasoning_agent = Agent(
    model=llm.default, #type: ignore
    tools=[YFinanceTools(stock_price=True,
                         analyst_recommendations=True,
                         company_info=True,
                         company_news=True
                         )],
    instructions=["Use tables to show data"],
    show_tool_calls=True,
    reasoning=True,
    markdown=True,
    structured_outputs=True
)

task = "Write a report comparing NVDA to TSLA"
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
