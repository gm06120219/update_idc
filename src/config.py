#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 文件解析

import os
import json
import math


"""parse config.json"""


# return a json data
def readconfig(url):
	# check url
	if url == '':
		file_object = open('config.json')
	else:
		file_object = open(url)

	# read content
	try:
		content = file_object.read()
		content_json = json.loads(content)
		pass
	finally:
		file_object.close()
	return content_json

# test
# json = readconfig('config.json')
# print json