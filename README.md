## How to run services


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


