# Local LLM Course
- Requirements
  - [Ollama](https://ollama.com/download/linux)
  - [Python UV](https://docs.astral.sh/uv/#installation)

```bash
service ollama start
ollama
ollama pull qwen2.5-coder:1.5b
ollama run qwen2.5-coder:1.5b
ollama stop qwen2.5-coder:1.5b
ollama rm qwen2.5-coder:1.5b
ollama ls
```
### UV Env
```bash
# https://docs.astral.sh/uv/#installation
curl -LsSf https://astral.sh/uv/install.sh | sh
uv init sci
cd sci
uv add ollama
uv run src/ollama_curl.py
```
### create model
```bash
ollama create jimmy -f ./Modelfile
```
### curl
```bash
curl localhost:11434/api/generate \
-d '{
  "model":"jimmy",
  "prompt":"give me a simple php function to sum two numbers",
  "stream":false,
  "format": "json"
}'
```
### python
```python
import ollama
# linux: service ollama start
client = ollama.Client(host='172.17.0.1:11434')
client.list
r = ollama.chat(model="qwen2.5-coder:1.5b",messages=[{"role":"user","content":"test"}])
print(r)
```
