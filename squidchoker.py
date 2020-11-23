#!/usr/bin/env python3

import requests
import sys
from termcolor import colored 

banner='''                        _     __     
      _________ ___  __(_)___/ /     
     / ___/ __ `/ / / / / __  /      
    (__  ) /_/ / /_/ / / /_/ /       
   /____/\__, /\__,_/_/\__,_/        
           / /         __            
     _____/ /_  ____  / /_____  _____
    / ___/ __ \/ __ \/ //_/ _ \/ ___/
   / /__/ / / / /_/ / ,< /  __/ /    
   \___/_/ /_/\____/_/|_|\___/_/  '''

print(" ")
print(colored(banner, "green"))
print(" ")
print(colored("            PORT SNIPER", "yellow",attrs=['blink']))
print(" ")

def chokethesquid(): 
 
    username=str(sys.argv[1]) 
    password=str(sys.argv[2]) 
    sqdomain=str(sys.argv[3]) 
    squidport=str(sys.argv[4]) 
    webdomain=str(sys.argv[5])
    portnumber=int(sys.argv[6]) 
 
    squidproxy={'http': 'http://{}:{}@{}:{}'.format(username,password,sqdomain,squidport)} 
    r = requests.get("http://{}:{}".format(webdomain,portnumber), proxies=squidproxy) 
 
    while r.status_code != 200 & portnumber < 65535: 
 
        portnumber +=1 
 
        print(colored("Attempting","cyan"),colored("squid choke","magenta"),colored("on this port:","cyan"),colored(">>","white"),colored("{}","yellow").format(portnumber),colored("<<","white"), end='\r') 

        if portnumber < 65535: 
            r = requests.get("http://{}:{}".format(webdomain,portnumber), proxies=squidproxy) 
            if r.status_code == 200: 
                print(colored("\nSquid successfully choked!\nWeb server found on this port:", "green"),colored("\n>>>>>>","red", attrs=['blink']),colored("{}","green").format(portnumber),colored("<<<<<<","red", attrs=['blink'])) 
                print(" ")
        else: 
                print(colored("\nNothing found!","red")) 
                break 

chokethesquid() 
