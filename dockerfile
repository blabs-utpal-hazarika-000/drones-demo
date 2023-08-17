FROM python:3.10-slim

WORKDIR /app

COPY ./api/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api /app/

EXPOSE 8000

CMD ["python3.10", "main.py"]