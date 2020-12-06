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

simple script to find which ports serve web content on a web site through an authenticated http proxy such as squid http proxy<br>
can probably be done with a regular port scanner (such as nmap) through a proxy, but this helped us on a ctf<br>
during which we couldn't<br>
in order to divert attention away from  my shoddy programming I spruced it up with an ascii art banner and some colours and put it up here<br>
<br>
enjoy<br>
<br>
requires requests and termcolor<br>
<br>
usage:<br>
python3 squidchoker.py [proxy username] [proxy password] [proxy domain] [proxy port] [domain to be scanned] [port on which to begin scanning]<br>

example:<br>
python3 squidchoker.py admin password domain.com 3128 domain.com 1337<br>
