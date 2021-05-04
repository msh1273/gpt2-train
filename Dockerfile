FROM pytorch/torchserve:0.3.0-gpu

USER root
RUN apt-get update &&   apt-get install -y python3-pip python3-wheel python3-dev git make cmake pkg-config &&   rm -rf /var/lib/apt/lists/*
RUN pip install wheel &&   pip install transformers

RUN apt update
RUN apt install -y curl

ARG MODEL_NAME=gpt2-trained-model
ENV MODEL_NAME $MODEL_NAME
ARG MODEL_DOWNLOAD_LINK
ENV MODEL_DOWNLOAD_LINK $MODEL_DOWNLOAD_LINK

RUN echo $MODEL_NAME
RUN echo $MODEL_DOWNLOAD_LINK

USER model-server
WORKDIR /home/model-server
RUN curl -X GET $MODEL_DOWNLOAD_LINK -o model-store/$MODEL_NAME.mar

EXPOSE 8080

CMD ["torchserve", "--start", "--ncs", "--model-store=/home/model-server/model-store", "--models=$MODEL_NAME.mar"]