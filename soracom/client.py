# -*- coding: utf-8 -*-

"""SORACOM client module"""

import os
import urllib
import json
import requests

class SoracomClient:
    """Soracom Client Class"""
    
    API_BASE_URL = "https://api.soracom.io/v1"
    
    def __init__(self):
        self.headers = {}
        
    def auth(self, email=os.environ.get("SORACOM_EMAIL"), password=os.environ.get("SORACOM_PASSWORD")):
        data = {}
        headers = {'Content-Type': 'application/json'}
        payload = {'email': email, 'password': password}
        res = requests.post("https://api.soracom.io/v1/auth", headers=headers,data=json.dumps(payload)).text
        data = json.loads(res)
        apiKey = data['apiKey']
        token = data['token']
        self.headers = {
            'Accept': 'application/json',
            'X-Soracom-Api-Key': apiKey,
            'X-Soracom-Token': token
        }

    def get(self, path, params={}):
        query_string = "&".join(["{0}={1}".format(y,z) for y, z in params.items()])
        res = requests.get(self.API_BASE_URL+path+"?"+query_string,headers=self.headers).text
        if len(res) > 0 :
            data = json.loads(res)
            return data
        return True

    def post(self, path, params={}, payload={}):
        if len(params)>0:
            query_string = "&".join(["{0}={1}".format(y,z) for y, z in params.items()])
            path = path + "?" + query_string 
        headers = dict(self.headers.items() + {'Content-Type':'application/json'}.items())
        res = requests.post(self.API_BASE_URL+path,headers=headers,data=json.dumps(payload)).text
        if len(res) > 0 :
            data = json.loads(res)
            return data
        return True

    def put(self, path, params={}, payload={}):
        if len(params)>0:
            query_string = "&".join(["{0}={1}".format(y,z) for y, z in params.items()])
            path = path + "?" + query_string 
        headers = dict(self.headers.items() + {'Content-Type':'application/json'}.items())
        res = requests.put(self.API_BASE_URL+path,headers=headers,data=json.dumps(payload)).text
        if len(res) > 0 :
            data = json.loads(res)
            return data
        return True

    def delete(self, path, params={}):
        query_string = "&".join(["{0}={1}".format(y,z) for y, z in params.items()])
        res = requests.delete(self.API_BASE_URL+path+"?"+query_string,headers=self.headers).text
        if len(res) > 0 :
            data = json.loads(res)
            return data
        return True
