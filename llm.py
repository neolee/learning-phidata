from phi.model.openai.like import OpenAILike
from phi.model.ollama.chat import Ollama


lmstudio = OpenAILike(
    id="qwen2.5-14b-instruct",
    api_key="lmstudio",
    base_url="http://127.0.0.1:1234/v1",
)

ollama = Ollama(
    id="qwen2.5:14b"
)

ollama_coding = Ollama(
    id="qwen2.5-coder:32b"
)

ollama_reasoning = Ollama(
    id="qwq"
)
