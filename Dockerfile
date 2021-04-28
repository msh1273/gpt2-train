
FROM pytorch/torchserve:0.3.0-cpu

USER root
RUN apt-get update &&   apt-get install -y python3-pip python3-wheel python3-dev git make cmake pkg-config &&   rm -rf /var/lib/apt/lists/*
RUN pip install wheel &&         pip install transformers &&         pip install flask

RUN apt update
RUN apt install -y curl

ARG MODEL_NAME=gpt2-trained-model
ENV MODEL_NAME $MODEL_NAME
ARG MODEL_DOWNLOAD_LINK
ENV MODEL_DOWNLOAD_LINK $MODEL_DOWNLOAD_LINK

RUN echo $MODEL_NAME
RUN echo $MODEL_DOWNLOAD_LINK

RUN echo default_workers_per_model=1 >> /home/model-server/config.properties

USER model-server
WORKDIR /home/model-server
RUN curl -X GET $MODEL_DOWNLOAD_LINK -o model-store/$MODEL_NAME.mar

ENV LRU_CACHE_CAPACITY 1

COPY health.py .

EXPOSE 8000

CMD ["torchserve", "--start", "--ncs", "--model-store=/home/model-server/model-store", "--models=$MODEL_NAME.mar", "&", "python", "health.py"]
