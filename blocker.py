from sys import platform
import time
from datetime import datetime as dt

redirect="127.0.0.1"
temp_host="hosts"
web_block_list=["Youtube.com","Facebook.com","Twitter.com"]

if platform == "linux" or platform == "linux2":
    host_path=r"/etc/hosts"
    #print("Im Here Linux")
   
elif platform == "darwin":
    host_path=r"/private/etc/hosts"
    #print("Im Here Mac")
    
elif platform == "win32":
    host_path=r"c:\windows\system32\drivers\etc\hosts"
    #print('Im Here Windows')   
    
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,10) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        print("Working hours...")
        #time.sleep(5)
        file=open(temp_host,'r+')
        content=file.read()
        #print(content)
        for websit in web_block_list:
            if websit in content:
                pass 
            else:
                file.write(redirect + "  " + websit + "\n")
        
    else:
        file=open(temp_host,'r+')
        content=file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in web_block_list):
                file.write(line)
        file.truncate() 
        print("Njoyy Time")
    time.sleep(5)


