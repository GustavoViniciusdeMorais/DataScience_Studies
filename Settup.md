# Blanck Jupyter Notebook Docker Environment

### Gustavo Vinicius Morais

### The changes are in the branches
```
[branch/image-classification]
```

```sh
sudo docker-compose up -d --build
sudo docker exec -it [container_name_1] sh
jupyter notebook --ip=0.0.0.0
jupyter server list // get the token to login
```

### Troubleshooting
```sh
pip install --upgrade notebook
pip install keras
pip install tensorflow
```

### Requirements
```sh
pip install keras
pip install tensorflow
```
