# Utiliser une image Python légère
FROM python:3.9

WORKDIR /app
COPY . /app

RUN pip install flask flask_sqlalchemy psycopg2-binary

CMD ["python", "app.py"]
