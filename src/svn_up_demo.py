#!/usr/bin/env python
# -*- coding: utf-8 -*-

#利用系统SVN命令来更新

import os

def UpdateSvn(strUser, strPwd, strUpPath):
        strExec = "svn up '%s' --username %s --password %s --no-auth-cache" %(strUpPath, strUser, strPwd);
        print("cmd:%s" %strExec);

        nRet = os.system(strExec);
        print("nRet = %d" %nRet);

        return (0 == nRet);

if "__main__" == __name__:
        bUp = UpdateSvn('user', 'pwd', '/Users/gm/vlintech_svn/sandbox');

        if bUp:
                print("svn up succ!");
        else:
                print("svn up failed!");