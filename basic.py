from phi.agent.agent import Agent
from phi.run.response import RunResponse
from llm import model


agent = Agent(
    name="Basic Agent",
    model=model, #type:ignore
)

q = "share a 2 sentence horror story"

run: RunResponse = agent.run(q)
print(run.content)

# agent.print_response(q)
