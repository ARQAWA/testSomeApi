FROM python:3.11-slim
RUN pip install --no-cache-dir -U pip fastapi uvicorn
WORKDIR /opt/app
COPY main.py /opt/app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
