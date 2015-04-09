# -*- coding: UTF-8 -*-
# 从svn repos里 获取当天的日志

import pysvn
import time
SVNURL = "https://www.vlinsys.net/svn/sandbox/"
#SVNURL = "E://riag//work//HMI-Contrib"
g_LogList = []
TodayTime =  time.strftime("%Y-%m-%d", time.localtime()) 
Repos_NUM = 0


def print_reposinfo(reposInfo):
    ReposComitTime = time.strftime("%Y-%m-%d", time.localtime(reposInfo.date)) ;
    print reposInfo.author
    print ReposComitTime
    print reposInfo.message.encode("cp936")
    print reposInfo.revision.number
def getTody_log() :
    global g_LogList
    g_LogList = [] 
    client = pysvn.Client()
    revision_start=pysvn.Revision( pysvn.opt_revision_kind.head )
    
    bContinue = True
    while bContinue :
        
        LogList = client.log(SVNURL, revision_start, limit=10) ;
        print "LogList: %s" % (TodayTime)
        Number = LogList[len(LogList)-1].revision.number
        
        revision_start = pysvn.Revision( pysvn.opt_revision_kind.number, Number )
        
        for LogInfo in LogList:
            LogTime = time.strftime("%Y-%m-%d", time.localtime(LogInfo.date))
            print LogTime
            if LogTime==TodayTime:
                print LogInfo
                g_LogList.append(LogInfo) ;
            else:
                bContinue = False ;
            
        if len(g_LogList)==0:
            break ;
    
    
def WritLog():
    f = open("./ChangLog.txt", "wb") ;
    
    print g_LogList
    Text = "%s 修改日志/r/n/r/n" % (TodayTime)
    f.write(Text) ;
    
    for Log in g_LogList :
        Text = "%s : " % (Log.author.ljust(15) )
        f.write(Text ) ;
        f.write( Log.message.encode("cp936") ) ;
        f.write("/r/n")
        
    if len(g_LogList) == 0:
        f.write("没有修改日志")
        
    f.close()
        
if __name__ == '__main__':
    getTody_log()
    WritLog()