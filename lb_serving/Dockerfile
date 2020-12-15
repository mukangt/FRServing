FROM python:3.8.3-slim

RUN apt -y update && apt install -y protobuf-compiler
RUN pip install protobuf && \
    pip install grpcio
#     pip install flask -i http://mirrors.aliyun.com/pypi/simple && \

RUN mkdir /workspace
WORKDIR /workspace

COPY ./ /workspace

ENTRYPOINT ["bash", "run.sh"]