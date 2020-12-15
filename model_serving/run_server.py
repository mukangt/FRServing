'''
Author: mukangt
Date: 2020-12-07 17:48:55
LastEditors: mukangt
LastEditTime: 2020-12-15 14:42:51
Description: 
'''
import argparse
import base64
import io
import time
from concurrent import futures

import grpc
import numpy as np
from PIL import Image

from app.core.models import FaceRecognition
from app.grpc.call_pi_pb2 import PiReply, PiRequest
from app.grpc.call_pi_pb2_grpc import (PiServiceServicer,
                                       add_PiServiceServicer_to_server)
from app.utils.logging import logging

model = FaceRecognition()


def infer(img_64):
    base64_decoded = base64.b64decode(img_64)
    image = Image.open(io.BytesIO(base64_decoded))
    boxes, probs, points = model.predict(image, landmarks=True)

    return 200, boxes.tolist().__str__()


class Pi(PiServiceServicer):
    def SendData(self, request, context):
        # logging.info("start_get_data, url: {}".format(request.name) )
        start = time.time()
        code, data = infer(request.image)
        end = time.time()

        if code == 200:
            logging.info(
                "success_get_data, time: {}s, size: {}, url: {}".format(
                    (end - start), len(data), 'test'))
        else:
            logging.error("fail_get_data, time: {}s, size: {}, url: {}".format(
                (end - start), len(data), 'test'))

        return PiReply(code=code, data=data)


def serve(port):
    host = '[::]:{}'.format(port)
    logging.info(host)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_PiServiceServicer_to_server(Pi(), server)

    server.add_insecure_port(host)
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


# HTTP_PORT = 47260
# if len(sys.argv) > 1:
#     HTTP_PORT = sys.argv[1]

if __name__ == "__main__":
    paser = argparse.ArgumentParser()
    paser.add_argument('-p', '--port', default=47260)
    args = paser.parse_args()

    logging.info("-------grpc service start--------")
    serve(args.port)
