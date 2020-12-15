'''
Author: mukangt
Date: 2020-12-07 17:18:41
LastEditors: mukangt
LastEditTime: 2020-12-15 14:42:01
Description: 
'''
import logging

import torch
from facenet_pytorch import MTCNN


class FaceRecognition():
    def __init__(self):
        super().__init__()
        self.mtcnn = MTCNN(select_largest=False, device='cuda')

    def predict(self, image, landmarks=False):
        # boxes, probs, points
        return self.mtcnn.detect(image, landmarks)
