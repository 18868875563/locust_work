#
# import time
# from datetime import datetime
#
# import random
#
# res = time.strftime("%M%S",time.localtime())
#
# result = random.random() * 100000
#
# result = str(result)[0:4]
#
# print(res + result)


# data = {"id": "", "orgId": "", "name": "zz_1_" + self.get_random(),
        # "icon": "http://img.souche.com/8377149a4cd1ff35d9767e947a5e4f0a.png", "description": "描述123", "builtIn": 0,
        # "code": "zl_1_" + self.get_random()}

from locust import HttpLocust,TaskSet,task

import requests
import json


import random

import time
import datetime


def get_obj():
    headers = {"Content-Type": "application/json", "_security_token_inc": "91561709377673106"}

    data = {"id": "",
            "orgId": "",
            "name": "zz_1_oooo",
            "icon": "http://img.souche.com/8377149a4cd1ff35d9767e947a5e4f0a.png",
            "description": "描述123",
            "builtIn": 0,
            "code": "zl_1_ppppp"
            }

    data_res = json.dumps(data)

    obj_1 = requests.post(url="http://titan-fall.test.dasouche-inc.net/objects/submit.json", data=data_res,headers=headers).json()

    print(obj_1)

get_obj()