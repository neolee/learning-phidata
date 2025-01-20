from phi.agent.agent import Agent
import llm


model = llm.deepseek

# basic
agent = Agent(
    model=model, # type: ignore
    markdown=True)

q = "Share a 2 sentence horror story."
agent.print_response(q)

# reasoning
reasoning_agent = Agent(
    model=model, # type: ignore
    reasoning=True,
    markdown=True,
)

task = "请给出一个从上海到南京的旅游行程规划"
reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)
