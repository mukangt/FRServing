'''
Author: mukangt
Date: 2020-12-11 17:35:25
LastEditors: mukangt
LastEditTime: 2020-12-15 14:29:12
Description: 
'''
from locust import User, between, task

from grpc_client import run


class MyUser(User):
    @task
    def my_task(self):
        run()

    # wait_time = between(0.1, 1)
