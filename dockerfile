FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "gateway.app:app", "--bind", "0.0.0.0:5000"]
