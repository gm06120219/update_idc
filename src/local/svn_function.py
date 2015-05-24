#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 利用系统SVN命令来导出文件

import os


def export(strUser, strPwd, strExportPath):
    d = "temp"
    os.system("mkdir %s" % d)
    strExec = "svn export '%s' --username %s --password %s --no-auth-cache %s" % (
        strExportPath, strUser, strPwd, d + '/' + strExportPath.split('/')[-1])
    print("cmd:%s" % strExec)

    nRet = os.system(strExec)
    print("nRet = %d" % nRet)

    return (0 == nRet)


def update(username, password, localPath):
    strExec = "svn up '%s' --username %s --password %s --no-auth-cache" % (
        localPath, username, password)
    print("cmd:%s" % strExec)

    nRet = os.system(strExec)
    print("nRet = %d" % nRet)

    return (0 == nRet)

