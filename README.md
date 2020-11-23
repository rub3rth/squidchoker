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

simple script to find which ports serve web content on a web site through an authenticated http proxy such as squid http proxy
can probably be done with a regular port scanner (such as nmap) through a proxy, but this helped us on a ctf
during which we couldn't
in order to divert attention away from  my shoddy programming I spruced it up with an ascii art banner and some colours and put it here
enjoy


usage:
python3 squidchoker.py <proxy username> <proxy password> <proxy domain> <proxy port> <domain to be scanned> <port on which to begin scanning>
example:
python3 squidchoker.py admin password domain.com 3128 domain.com 1337
