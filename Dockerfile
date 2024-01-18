FROM python:3.12
ENV PYTHONUNBUFFERED 1

WORKDIR /bot

COPY requirements.txt .
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /bot/

CMD ["python", "app.py"]
