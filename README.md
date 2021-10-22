## How to run services


### Prerequisites
Using python version `3.8.11`

```shell
    pip install --no-deps git+https://github.com/maciejkula/spotlight.git@master#egg=spotlight
```

```shell
  pip install --no-deps git+https://github.com/maciejkula/spotlight.git@master#egg=spotlight
```
```shell
  pip install torch==1.7.0 -f https://download.pytorch.org/whl/torch_stable.html
```

### Download English library with spacy, run this command:
```shell
  python -m spacy download en_core_web_md
```


## Run services
```shell
  python manage.py server
```


## Test Services
```shell
  python -m pytest
```
-------------------
##Build docker image

```shell
    docker build --rm \
        -f "Dockerfile" \
        -t ai-recommendation-service:latest .
```

## Running container
```shell
    docker run --restart always\
         -p 5002:5002 --name aiml_recomendation_latest\
         -d ai-recommendation-service:latest
```

## Accessing swagger

Please Open [http://localhost:5002/apidocs/](http://localhost:5002/apidocs/)

