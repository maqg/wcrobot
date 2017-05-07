#!/usr/bin/python
# -*- coding: utf-8 -*-

import pika
import json

from core.log import ERROR
from core.routingkeys_code import *


RABBITMQ_USER = "octlink"
RABBITMQ_PASSWD = "123456"
RABBITMQ_RVM_VHOST = "/octlink"
RABBITMQ_RVM_EXCHANGE = "exchageRVMServer"


def build_payload(msgType, payload):
	data = {
		"msgType": msgType,
		"routingKey": routingkeys.get(msgType),
		"data": payload,
	}
	return json.dumps(data)


#
# sent OK=>True, sent failed=>False
#
def msgqueue_send(msgType, payload=None):
	credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWD)
	parameters = pika.ConnectionParameters(
		host='localhost',
		port=5672,
		virtual_host=RABBITMQ_RVM_VHOST,
		credentials=credentials)
	try:
		connection = pika.BlockingConnection(parameters)
	except:
		ERROR("connect to server error %s,%s" % (str(parameters), str(credentials)))
		return False

	if (connection == None):
		ERROR("create connection to localhost error %s" % (str(parameters)))
		return True

	channel = connection.channel()
	properties = pika.BasicProperties(content_type='text/plain',
	                                  delivery_mode=1)

	channel.basic_publish(exchange=RABBITMQ_RVM_EXCHANGE,
	                      routing_key=routingkeys.get(msgType),
	                      body=build_payload(msgType, payload),
	                      properties=properties)

	connection.close()


if __name__ == '__main__':
	data = {
		"name": 100,
		"type": "henry",
	}
	msgqueue_send(5, data)
