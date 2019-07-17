import time
import subprocess
import os
import socket
def restart():
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        lst = localtime.split(' ')
        if (lst[3] == '11:14:00'):
            subprocess.call(['shutdown','/r','/t','7'])
def shutdown():
    while True:
        localtime = time.asctime(time.localtime(time.time()))
        lst = localtime.split(' ')
        if (lst[3] == '18:40:00'):
            subprocess.call(['shutdown','/s','/t','7'])
def get_ip():
    print(socket.gethostbyname(socket.gethostname()))

def erase_dir():
    del_dir = 'C:/Users/DCPRIC~1/AppData/Local/Temp'
    file_list = [f for f in os.listdir(del_dir)]
    for i in file_list:
        print(i)
        os.remove(os.path.join(del_dir,i))
def erase_temp():
    del_dir = 'C:/Users/DCPRIC~1/AppData/Local/Temp'
    p = subprocess.Popen('del /S /Q /F %s\\*.*'%del_dir,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    p_tup = p.communicate()
    p_c = p.returncode
    if p_c == 0:
        print('cleaned')
    else:
        print('error')

get_ip()
# s = 'santhosh'
# print(s[1:])