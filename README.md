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
- qwen2.5:14b `tools` `structued output` `reasoning`
- qwen2.5-coder:32b `tools` `coding`
- qwq `tools` `auto-reasoning`
- snowflake-arctic-embed2 `embedding`

### OpenAI Compatible API by LM Studio
- qwen2.5-14b-instruct `tools` `reasoning*`

\* with warnings for lack of structured output support
