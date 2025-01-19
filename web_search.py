from phi.agent.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
import llm


agent = Agent(
    name="DuckDuckGo Agent",
    model=llm.default, #type: ignore
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

q = "Tell me about NVIDIA's Digits computer"
agent.print_response(q)

agent = Agent(
    name="Google Agent",
    model=llm.default, #type: ignore
    tools=[GoogleSearch()],
    description="你是一个新闻文章智能体，帮助用户获得最新的新闻资料",
    instructions=[
        "对用户的每个查询主题提供4篇最新的相关新闻报道，",
        "搜索最新的10篇报道并选取里面排名最高的4篇非重复的内容，",
        "所搜所有中文和英文的内容。",
    ],
    show_tool_calls=True,
    markdown=True,
    # debug_mode=True,
)

q = "为什么小红书来了那么多老外？"
agent.print_response(q)
