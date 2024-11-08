FROM python:3.11
COPY requirements.txt .
RUN pip install --no-cache-dir -U pip &&  \
    pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt /root/.cache/pip -rf
WORKDIR /opt/app