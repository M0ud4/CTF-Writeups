from pwn import * 
import re

p=process('./casino')
wiw=b'[ ** WELCOME TO ROBO CASINO **]\n     ,     ,\n    (\\____/)\n     (_oo_)\n       (O)\n     __||__    \\)\n  []/______\\[] /\n  / \\______/ \\/\n /    /__\\\n(\\   /____\\\n---------------------\n[*** PLEASE PLACE YOUR BETS ***]\n> [ * CORRECT *]\n> [ * CORRECT *]\n> [ * INCORRECT * ]\n[ *** ACTIVATING SECURITY SYSTEM - PLEASE VACATE *** ]\n'
x=(re.findall(rb'\[ \* CORRECT \*\]',wiw))
print(len(x))
for i in range(256):
    payload=('HTB{'+chr(i)) #cheese the flag char by char
    p.sendline(payload)
    response=p.recv()
    x=re.findall(rb'\[ \* CORRECT \*\]',response) 
    if len(x)==len(payload):
        s=chr(i)
        print(s)
        break
    p.close()
    p=process('./casino')
#HTB{r4nd_1s_v3ry_pr3d1ct4bl3}
    
    

        
    
