FROM python:3.8.8

COPY . /app

WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Server will reload itself on file changes if in dev mode
EXPOSE 5050

CMD ["python", "./manage.py", "runserver"]


