FROM pytorch/pytorch:1.7.0-cuda11.0-cudnn8-runtime

RUN apt -y update && apt install -y protobuf-compiler
RUN pip install protobuf && \
    pip install facenet_pytorch && \
    pip install grpcio

WORKDIR /workspace

COPY ./ /workspace

ENV CUDA_VISIBLE_DEVICES=0

ENTRYPOINT ["bash", "run.sh"]