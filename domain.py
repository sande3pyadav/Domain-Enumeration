import requests
import sys 

def love(domain,wordlist):
   f = open(wordlist,'r').read()   
   var = f.splitlines()
   for dir in var:
       
       domains=f"https://{domain}/{dir}.php"
       #print(domains)
       try:
           re = requests.get(domains)
           
           if re.status_code==404:
               pass
           else:
               print(domains)
       except:
           pass
    
    
    
domain=sys.argv[1]
wordlist=sys.argv[2]

love(domain,wordlist)
