import os
from phi.model.openai.like import OpenAILike
from phi.model.ollama.chat import Ollama
from phi.model.deepseek.deepseek import DeepSeekChat


ollama_phi = Ollama(id="phi-4")
ollama_qwen = Ollama(id="qwen2.5:14b")
ollama_qwen_coder_lite = Ollama(id="qwen2.5-coder:7b")
ollama_qwen_coder = Ollama(id="qwen2.5-coder:32b")
ollama_r1_qwen = Ollama(id="r1-qwen:32b")

lmstudio = OpenAILike(
    id="default",
    api_key="lmstudio",
    base_url="http://127.0.0.1:1234/v1",
)
ali_qwen = OpenAILike(
    id="qwen-max-latest",
    api_key=os.environ.get("ALIYUN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
ali_deepseek = OpenAILike(
    id="deepseek-v3",
    api_key=os.environ.get("ALIYUN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
ali_deepseek_r1 = OpenAILike(
    id="deepseek-r1",
    api_key=os.environ.get("ALIYUN_API_KEY"),
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

deepseek = DeepSeekChat(id="deepseek-chat")

default = ali_qwen
coding = ollama_qwen_coder
reasoning = ollama_r1_qwen
