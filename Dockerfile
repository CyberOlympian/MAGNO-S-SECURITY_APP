FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && python -m pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

CMD ["python", "-u", "app/main.py"]
