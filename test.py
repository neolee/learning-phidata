from phi.agent import Agent, RunResponse
from phi.model.openai.like import OpenAILike

agent = Agent(
    model=OpenAILike(
        id="qwen2.5-coder-32b-instruct-mlx",
        api_key="LM Studio",
        base_url="http://127.0.0.1:1234/v1",
    )
)

q = "share a 2 sentence horror story"

run: RunResponse = agent.run(q)
print(run.content)

# agent.print_response(q)
