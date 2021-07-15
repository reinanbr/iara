import time as tm,time,sys,os,psutil,socket
from collections import namedtuple
# -*- coding: utf-8 -*-



__cpu_show__ = False

#data
def date(base='%d/%m/%Y %H:%M:%S'):
  from datetime import datetime as dt
  dt = dt.now()
  return dt.strftime(base)

def ram():
  r_max = float(round(psutil.virtual_memory().total/(1024**3),3))
  r_per = float(psutil.virtual_memory().percent)
  r_use = round(r_max*r_per/100,3)
  r_ping = round(time.process_time()*100,1)
  r_ = namedtuple('ram',['use','max','per','ping'])
  return r_(r_use,r_max,r_per,r_ping)

def Printing_info_system():
    print('=+='*18)
    print(f'diretorio: {os.getcwd()}')
    print(f'system Platform: {os.uname().sysname}')
    #print(f'Platform Version: {os.uname().version}')
    print(f'Machine: {os.uname().machine}')
    print(f'RAM: {ram()[0]} GB / {ram()[1]} GB ({ram()[2]}% used)')
    #print(f'RAM Used: {psutil.virtual_memory().percent}%')
    print(f'PING CPU: {round(time.process_time()*100,1)}ms') 
    #print(f'vel. process: {round(1/time.process_time(),3)} app/s')
    print(f'data: {date().split()[0]}')
    print(f'hora: {date().split()[1]}')
    print('=+='*18)



import platform,socket,re,uuid,json,psutil,logging

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return json.dumps(info)
    except Exception as e:
        logging.exception(e)

#print(json.loads(getSystemInfo()))



#criar pastas
def mkdir(path):
	os.mkdir(path)



#salvando arquivos
def save_file(var,path,code='utf-8',a='w'):
    with open(path,a,encoding=code) as _file:
      puts('salvando variavel...')
      _file.write(str(var))
      puts('variavel salva!')



