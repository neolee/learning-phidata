from phi.model.openai.like import OpenAILike


model = OpenAILike(
    id="qwen2.5-coder-32b-instruct-mlx",
    api_key="lm-studio",
    base_url="http://127.0.0.1:1234/v1",
)
