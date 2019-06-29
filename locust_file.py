

from locust import HttpLocust,TaskSet,task

import requests

import random

import time

import datetime

import json


class Stay(TaskSet):
    # 登录
    def login(self):
        global string_list
        url = 'http://titan-fall.test.dasouche-inc.net'
        url_denglu = "/account/login.json?username=17758031018&password=souche2015"
        response = requests.get(url=url + url_denglu).json()
        string_list = response['data']
        header = {'Content-Type': 'application/json', '_security_token': string_list}
        requests.get(url + "/account/info.json", headers=header).json()

    def on_start(self):
        res = time.strftime("%M%S", time.localtime())
        result = random.random() * 100000
        result = str(result)[0:4]
        random_num = res + result
        return random_num

    # 业务1
    @task
    def get_obj(self):
        headers = {'Content-Type': 'application/json', '_security_token':"91561703409951248"}
        data = {
                "id": "",
                "orgId": "",
                "name": "zz_1_" + self.on_start(),
                "icon": "http://img.souche.com/8377149a4cd1ff35d9767e947a5e4f0a.png",
                "description": "描述123",
                "builtIn": 0,
                "code": "zl_1_" + self.on_start()
            }
        print("--------1--------")
        self.client.post(url="http://titan-fall.test.dasouche-inc.net/objects/submit.json",data=json.dumps(data),headers=headers)
        print("--------2--------")


    # 业务2
    @task
    def obj_list(self):
        print("-------1--------")

        headers = {'Content-Type': 'application/json', '_security_token':"91561703409951248"}

        self.client.get(url="http://titan-fall.test.dasouche-inc.net/layouts/detail.json?layoutId=ltKikIP7WA",headers=headers)

        print("-------2--------")


class User(HttpLocust):

    task_set = Stay
    # min_wait = 50
    # max_wait = 150

    host = "http://titan-fall.test.dasouche-inc.net"

