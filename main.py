#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import config
import ssh

# read config
content_json = config.readconfig('temp.json')

# get server & program list
try:
    svr = content_json['svr']
    print svr
    program_list = content_json['program_list']
    print program_list
    program_list_leng = len(program_list)
    pass
except Exception, e:
    print "exception"
    sys.exit()

print '\nSSH to server ' + svr + '.\n'

# get input
username = raw_input("SSH username:")
password = raw_input("SSH password:")

# test ssh server
ssh.ssh_cmd(svr, username, password, 'ls /home/' + username)


# if __name__ == '__main__':
