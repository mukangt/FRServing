'''
Author: mukangt
Date: 2020-12-09 13:27:11
LastEditors: mukangt
LastEditTime: 2020-12-15 14:30:35
Description: 
'''
import argparse
import time
from concurrent import futures

import grpc

from app.core.hashring import HashRing
from app.grpc.call_pi_pb2 import PiReply
from app.grpc.call_pi_pb2_grpc import (PiServiceServicer,
                                       add_PiServiceServicer_to_server)
from app.grpc.grpc_client import get_res_by_grpc
from app.utils.logging import logging
from conf.config import Config

hash_ring = HashRing(Config.GRPC_HOST_LIST)


def inference(img_64):
    grpc_host = hash_ring.get_node(str(time.time()))
    code, data = get_res_by_grpc(grpc_host, img_64)
    return code, data
    # return 200, 'bingo'


class Pi(PiServiceServicer):
    def SendData(self, request, context):
        logging.info('start_get_data, url:{}'.format('request.image'))

        start = time.time()
        code, data = inference(request.image)
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
    host = '[::]:' + str(port)
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


if __name__ == "__main__":
    paser = argparse.ArgumentParser()
    paser.add_argument('-p', '--port', default=9959)
    args = paser.parse_args()

    logging.info("-------grpc service start--------")
    serve(args.port)
