FROM python:3.11
ENV PYTHONUNBUFFERED 1

RUN mkdir /bot
COPY . /bot/
WORKDIR /bot

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD ["python", "app.py"]