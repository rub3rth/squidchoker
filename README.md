                        _     __     
      _________ ___  __(_)___/ /     
     / ___/ __ `/ / / / / __  /      
    (__  ) /_/ / /_/ / / /_/ /       
    /____/\__, /\__,_/_/\__,_/        
            / /         __            
      _____/ /_  ____  / /_____  _____
     / ___/ __ \/ __ \/ //_/ _ \/ ___/
    / /__/ / / / /_/ / ,< /  __/ /    
    \___/_/ /_/\____/_/|_|\___/_/  

# squidchoker
simple python script to find ports serving web content through a http proxy (credentials required) such as squid http proxy<br>
can probably be done with a regular port scanner (e g nmap with proxy chains), but this helped us out in a ctf<br>
during which we couldn't so I thought I'd share<br>
in order to divert attention away from  my shoddy programming I spruced it up with an ascii art banner and some colours<br>
<br>
enjoy<br>
## installation
clone the repo and install dependencies<br>
```git clone https://github.com/rub3rth/squidchoker```<br><br>
```cd squidchoker```<br><br>
```pip3 install -r requirements.txt```
## example usage
```python3 squidchoker.py [proxy username] [proxy password] [proxy domain] [proxy port] [domain to be scanned] [port on which to begin scanning]```
<br><br>
```python3 squidchoker.py admin password domain.com 3128 domain.com 1337```
## demo

