# SW API GraphQL

## Requirements
* [Python](https://www.python.org/) (realizado en python 3.8)
* [Django](https://github.com/django/django)
* [Django Filter](https://github.com/carltongibson/django-filter)
* [Django model utils](https://github.com/jazzband/django-model-utils)
* [Graphene](https://github.com/graphql-python/graphene-django)
* [.EVN](https://github.com/theskumar/python-dotenv)

## Setup

Clone the project
```
git clone https://github.com/luisa104/swapi-back.git
```


### Runing in docker
```
docker build .
docker-compose build
docker-compose up
```
### Created super user
```
docker-compose run app  sh -c "python manage.py createsuperuser"
```