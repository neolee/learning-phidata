from phi.agent.agent import Agent
from phi.run.response import RunResponse
from phi.model.openai.like import OpenAILike


model=OpenAILike(
    id="qwen2.5-coder-32b-instruct-mlx",
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
)

agent = Agent(
    name="Basic Agent",
    model=model, #type:ignore
)

q = "share a 2 sentence horror story"

run: RunResponse = agent.run(q)
print(run.content)

# agent.print_response(q)
