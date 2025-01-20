from phi.agent.agent import Agent
from phi.tools.crawl4ai_tools import Crawl4aiTools
import llm


agent = Agent(
    model=llm.default, # type: ignore
    tools=[Crawl4aiTools(max_length=None)],
    show_tool_calls=True,
    markdown=True,
)

url = "https://www.news.cn/politics/20250119/f33c2caa323249ca8fd2038515ee9620/c.html"
q = "Tell me about " + url
agent.print_response(q)
