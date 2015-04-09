#!/usr/bin/env python
# -*- coding: utf-8 -*-

#文件解析

import os
import json
import math



"""parse config.json"""
def readconfig(url):
	if url == '':
		print "null"
# 		file_object = open('config.json')
# try:
#      all_the_text = file_object.read()
# finally:
#      file_object.close()


# # print all_the_text


# decodejson = json.loads(all_the_text)
# svr = decodejson['svr']
# program_list = decodejson['program']
# program_list_leng = len(program_list)

# if program_list_leng>0:
# 	for i in range(0,program_list_leng):
# 		print program_list[i]['name']
# 		print program_list[i]['url']
# 	pass

readconfig('')
