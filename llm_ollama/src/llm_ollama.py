import ollama
# linux: service ollama start
client = ollama.Client(host='127.0.0.1:11434')
client.list
r = ollama.chat(model="qwen2.5-coder:1.5b",messages=[{"role":"user","content":"test"}])
print(r)