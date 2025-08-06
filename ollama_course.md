# Local LLM Course
- Requirements
  - [Ollama](https://ollama.com/download/linux)

```bash
service ollama start
ollama
ollama pull qwen2.5-coder:1.5b
ollama run qwen2.5-coder:1.5b
ollama stop qwen2.5-coder:1.5b
ollama rm qwen2.5-coder:1.5b
ollama ls
```
### create model
```bash
ollama create jimmy -f ./Modelfile
```
### curl
```bash
curl localhost:11434/api/generate \
-d '{"model":"jimmy","prompt":"give me a simple php function to sum two numbers", "stream":false}'
```
