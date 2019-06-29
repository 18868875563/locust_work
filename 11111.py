import requests

def login(self):
    global string_list
    url = 'http://titan-fall.test.dasouche-inc.net'
    url_denglu = "/account/login.json?username=17758031018&password=souche2015"
    response = requests.get(url=url + url_denglu).json()
    string_list = response['data']
    header = {'Content-Type': 'application/json', '_security_token':string_list}
    requests.get(url + "/account/info.json", headers=header).json()

def on_start(self):
    self.login()

import time,random


class Login(object):

    def __init__(self):
        self._security_token = []

        self.url = 'http://titan-fall.test.dasouche-inc.net/account/'

    def login(self):

        global string_list
        #账号登录
        login_str = 'login.json?username=17758031018&password=souche2015'

        response = requests.get(self.url + login_str).json()

        string_list = response['data']


    def info(self):

        url_info = 'info.json'

        header = {'Content-Type': 'application/json', '_security_token':string_list}

        res_1 = requests.get(self.url + url_info,headers=header).json()

        print(res_1)

    def obj_list(self):

        url_list = 'http://titan-fall.test.dasouche-inc.net/layouts/detail.json?layoutId=ltKikIP7WA'

        headers = {'Content-Type': 'application/json', '_security_token': string_list}

        # h = {"User-Agent":"PostmanRuntime/7.15.0","Accept":"*/*","Cache-Control":"no-cache","Postman-Token":"f7667845-d3a3-4e19-8f10-41fd531bbed4","Host":"titan-fall.test.dasouche-inc.net","cookie": self._security_token[0],"accept-encoding":"gzip","Connection":"keep-alive"}

        res_list = requests.get(url_list,headers=headers).json()
        print(res_list)



    def get_random(self):
        res = time.strftime("%M%S", time.localtime())

        result = random.random() * 100000

        result = str(result)[0:4]

        random_num = res + result

        return random_num

    def get_obj(self):

        headers = {"Content-Type":"application/json","_security_token_inc":"91561709377673106"}

        data = {"id": "",
                "orgId": "",
                "name": "zz_1_oooo",
                "icon": "http://img.souche.com/8377149a4cd1ff35d9767e947a5e4f0a.png",
                "description": "描述123",
                "builtIn": 0,
                "code": "zl_1_ppppp"
        }

        obj_1 = requests.post(url="http://titan-fall.test.dasouche-inc.net/objects/submit.json",data=data,headers=headers).json()

        print(obj_1)



if __name__ == '__main__':
    P = Login()
    w = P.login()
    e = P.info()
    r = P.obj_list()
    t = P.get_obj()