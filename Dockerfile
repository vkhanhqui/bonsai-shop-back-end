FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
WORKDIR /back_end
ENV PORT 8000
COPY ["requirements.txt", "/back_end/"]
RUN apt-get update && apt-get -y dist-upgrade \
    && apt install -y netcat \
    && pip install -r requirements.txt