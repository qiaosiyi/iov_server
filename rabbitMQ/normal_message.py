#!/usr/bin/env python

from rpc_server import rpc_server
import requests
import json

basedir = "/var/www/iov-apis/yinspect-iov/storage/app/drivers/"
url = "http://www.tangjs.cn:9999/api/v1/sensor/sync"

class vehicle_status(rpc_server):
	"""docstring for vehicle_status"""
	def __init__(self, username, passwd, hostip, queuename):
		super(vehicle_status, self).__init__(username, passwd, hostip, queuename)

	def do_something(self, response):
		try:
			response = eval(response)
			if response['tag'] == 1:
#				print response
				#sensor data
				payload = {"result":response['result'], "vid":response['vid'], "tag":1}
				print "payload:",payload
				r = requests.post(url , data=payload)
				print "r.text:",r.text
				print
			

			elif response['tag'] == 2:
				#person not found
				#print response['file']
				#print response
				savepath = basedir + "DriverNotFound/" + str(response['vid']) + "_" + response['filename']
				fw = open(savepath, 'wb')
				fw.write(response['file'])
				fw.close()
				filepath = "DriverNotFound/" + str(response['vid']) + "_" + response['filename']
				payload = {"filepath":filepath, "vid":response['vid'], "tag":2, "time":response['time']}
				print "payload:",payload
				r = requests.post(url , data=payload)
				print "r.text:",r.text
				

			elif response['tag'] == 3:
				print response
				#face recognize result
				print "face recognize result"
				payload = {"did":response['did'], "vid":response['vid'], "tag":3, "time":response['time']}
				print "payload:",payload
				r = requests.post(url , data=payload)
				print "r.text:",r.text
				

			elif response['tag'] == 4:
				#fatigue detect
				print "fatigue detect"
				savepath = basedir + "fatigue_image/" + str(response['vid']) + "_" + response['filename']
				fw = open(savepath, 'wb')
				fw.write(response['file'])
				fw.close()
				filepath = "fatigue_image/" + str(response['vid']) + "_" + response['filename']
				payload = {"fatigue":response['fatigue'], "filepath":filepath ,"vid":response['vid'], "tag":4, "time":response['time']}
				print "payload:",payload
				r = requests.post(url , data=payload)
				print "r.text:",r.text
				
							
			elif response['tag'] == 5:
				print response
				#road detect
				print 'road detect'

			return (True, "success")
		except:
			print "try error resove!!"

if __name__ == '__main__':
	factory = vehicle_status("iov", "iovpro", "127.0.0.1", "normal_message")
	factory.start()
