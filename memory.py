from phi.agent.agent import Agent
from rich.pretty import pprint
import llm


agent = Agent(
    model=llm.default, # type: ignore
    add_history_to_messages=True, # type: ignore
    num_history_responses=3,
    description="You are a helpful assistant that always responds in a polite, upbeat and positive manner.",
)

agent.print_response("Share a 2 sentence horror story", stream=True)
pprint([m.model_dump(include={"role", "content"}) for m in agent.memory.messages])

agent.print_response("What was my first message?", stream=True)
pprint([m.model_dump(include={"role", "content"}) for m in agent.memory.messages])
