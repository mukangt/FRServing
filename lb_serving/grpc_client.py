'''
Author: mukangt
Date: 2020-12-09 13:56:25
LastEditors: mukangt
LastEditTime: 2020-12-15 14:30:19
Description: 
'''
import base64

import grpc
import numpy as np

from app.grpc.call_pi_pb2 import PiRequest
from app.grpc.call_pi_pb2_grpc import PiServiceStub


def read_image(image_path):
    with open(image_path, 'rb') as f:
        img_64 = base64.b64encode(f.read())

    return img_64


def run():
    img_64 = read_image('./test.jpg')

    channel = grpc.insecure_channel('localhost:9959')
    stub = PiServiceStub(channel)
    response = stub.SendData(PiRequest(image=img_64))
    print(response.code)
    a = response.data
    print(a)


if __name__ == "__main__":
    run()
