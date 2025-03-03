# Blanck Jupyter Notebook Docker Environment

### Gustavo Vinicius Morais

- [Pandas](./pandas.md)

### The changes are in the branches
```
[branch/kaggle-*]
```

```
sudo docker-compose up -d --build
sudo docker exec -it [container_name_1] sh
jupyter notebook --ip=0.0.0.0
jupyter server list // get the token to login
```

### Local ollama
```sh
curl -fsSL https://ollama.com/install.sh | sh
ollama 
ollama serve
# At another cli tab run
ollama pull nomic-embed-text
ollama pull mistral
# The server must be running
# The langchain in the jupyter notebook already nows the port to request, no need to config the local endpoint
```
