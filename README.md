# Learning `phidata`

## Setup

``` shell
# core
pip install packaging openai phidata ollama

# tools deps
pip install 'httpx[socks]' duckduckgo-search yfinance

# rag deps
pip install lancedb tantivy pypdf sqlalchemy

# playground deps
pip install 'fastapi[standard]' sqlalchemy
```

## Models
### Ollama
#### Large Language Models
- phi-4 `structued output` `reasoning`
  - based on hf.co/bartowski/phi-4-GGUF:IQ4_XS
- qwen2.5:14b `tools` `structued output` `reasoning`
  - based on hf.co/bartowski/Qwen2.5-14B-Instruct-GGUF:IQ4_XS
- qwen2.5-coder:32b `tools` `coding`
  - based on hf.co/bartowski/Qwen2.5-Coder-32B-Instruct-GGUF:IQ4_XS
- qwq `tools` `auto-reasoning`
  - based on hf.co/bartowski/QwQ-32B-Preview-GGUF:IQ4_XS
  
#### Embedding Models
- snowflake-arctic-embed2 `embedding`

### OpenAI Compatible API by LM Studio
The `llm.lmstudio` provider is the current loaded LLM in LM Studio server, which can be any model listed in the above section. But pay attention to the difference:
- LM Studio's API server support tools calling from version 0.3.6 and it even (seemingly) works on some models not labeled as supporting tools (e.g. phi-4). See [official docs for more details](https://lmstudio.ai/docs/advanced/tool-use).
- LM Studio's API server does NOT support `pydantic`'s structured output (for now).
- LM Studio's API server does NOT support `phidata`'s experimental reasoning feature (for now).
