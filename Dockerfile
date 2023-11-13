FROM python:3.8

WORKDIR /app

RUN git clone https://github.com/alicia1916/Application-Personal-Assistant.git .

RUN pip install poetry

RUN poetry install

CMD ["python", "main.py"]
