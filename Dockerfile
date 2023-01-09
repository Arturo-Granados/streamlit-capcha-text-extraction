# app/Dockerfile

FROM python:3.9-slim

EXPOSE 8501

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/Arturo-Granados/streamlit-capcha-text-extraction.git .

RUN pip3 install -r requirements.txt

#RUN pip uninstall protobuf

RUN pip install protobuf==3.20

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]