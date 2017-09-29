#!/usr/bin/env python

from rabbitMQ.rpc_server import rpc_server
import json
import requests

class vehicle_status(rpc_server):
	"""docstring for vehicle_status"""
	def __init__(self, username, passwd, hostip, queuename):
		super(vehicle_status, self).__init__(username, passwd, hostip, queuename)

	def do_something(self, response):
		print response
		response = eval(response)
                payload = {"result":"ad", "vid":100001, "tag":1}
                payload['result'] = response['result']
                payload['vid'] = response['vid']
                #url = "http://httpbin.org/post"
                url = "http://www.tangjs.cn:9999/api/v1/sensor/sync"
                r = requests.post(url , data=response)
                print r.text

		return (True, "success")

factory = vehicle_status("iov", "iovpro", "127.0.0.1", "normal_message")
factory.start()
