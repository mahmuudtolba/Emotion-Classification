FROM python:3.8.10
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app