from phi.agent.agent import Agent
from phi.run.response import RunResponse
import llm


agent = Agent(
    name="Basic Agent",
    model=llm.default, #type:ignore
)

# q = "share a 2 sentence horror story"
q = "8.9和8.11哪个更大？"

run: RunResponse = agent.run(q)
print(run.content)

# agent.print_response(q)
