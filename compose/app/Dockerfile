FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install -y iproute2 iputils-ping dnsutils traceroute nano && pip install flask
ENTRYPOINT ["python3", "api/app.py"]