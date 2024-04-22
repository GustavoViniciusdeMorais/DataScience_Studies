# API

### Setup
```sh
pip install fastapi
pip install "uvicorn[standard]"
pip install python-multipart
```
### Run API
```sh
uvicorn main:app --reload --host=0.0.0.0 --port=8080
```
### Endpoints doc
http://localhost:8080/docs
http://localhost:8080/check
### Classification flow description
```
```
### Classification Request
```sh
curl --location 'localhost:8080/classify' \
--form 'file=@"/usr/GustavoVinicius/Downloads/ImageRecyclingDataSet/Train/Glass/glass98.jpg"'
```
