from phi.agent.agent import Agent
import llm


def reasoning(task: str):
    reasoning_agent = Agent(
        model=llm.default, # type: ignore
        reasoning=True,
        markdown=True,
        structured_outputs=True
    )

    reasoning_agent.print_response(task, stream=True, show_full_reasoning=True)


if __name__ == "__main__":
    # task = (
    #     "Three missionaries and three cannibals need to cross a river. "
    #     "They have a boat that can carry up to two people at a time. "
    #     "If, at any time, the cannibals outnumber the missionaries on either side of the river, the cannibals will eat the missionaries. "
    #     "How can all six people get across the river safely? Provide a step-by-step solution and show the solutions as an ascii diagram"
    # )

    task = (
        "三个传教士和三个食人族需要过河。他们有一艘船，最多可以载两个人。"
        "如果在任何时候，河的任何一边食人族的数量超过传教士的数量，食人族就会吃掉传教士。"
        "所有六个人怎样才能安全地过河？请提供一个分步解决方案，并用ASCII图表示此解决方案。"
    )

    reasoning(task)
