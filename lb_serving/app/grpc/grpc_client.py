'''
Author: Tao Hang
Date: 2020-12-09 11:51:51
LastEditors: Tao Hang
LastEditTime: 2020-12-09 16:09:15
Description: 
'''
import time
import grpc

from app.utils.logging import logging
from app.grpc.call_pi_pb2 import PiRequest
from app.grpc.call_pi_pb2_grpc import PiServiceStub


def get_res_by_grpc(grpc_host, img_64):
    logging.info("start_call_grpc, grpc_host: {}, url: {}".format(
        grpc_host, 'test'))

    start = time.time()
    channel = grpc.insecure_channel(grpc_host)
    stub = PiServiceStub(channel)
    response = stub.SendData(PiRequest(image=img_64))
    end = time.time()

    if response.code == 200:
        logging.info("success_call_grpc, time: {}s, size: {}, url: {}".format(
            (end - start), len(response.data), 'text'))
    else:
        logging.error("fail_call_grpc, time: {}s, size: {}, url: {}".format(
            (end - start), len(response.data), 'text'))

    return response.code, response.data
