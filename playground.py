from phi.agent.agent import Agent
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from phi.playground.playground import Playground
from phi.playground.serve import serve_playground_app
import llm


model = llm.ollama

web_agent = Agent(
    name="Web Agent",
    model=model, #type: ignore
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    storage=SqlAgentStorage(table_name="web_agent", db_file="db/agents.db"),
    add_history_to_messages=True, #type: ignore
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=model, #type: ignore
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True)],
    instructions=["Use tables to display data"],
    storage=SqlAgentStorage(table_name="finance_agent", db_file="db/agents.db"),
    add_history_to_messages=True, #type: ignore
    markdown=True,
)

app = Playground(agents=[finance_agent, web_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)
