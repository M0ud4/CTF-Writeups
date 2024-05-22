"""
1-The vun in this task is that we can determine the first key block by xoring the first block of the 
plaintext with the first block of the ciphertext.
2-Key then is getting updated by sha256 digest , so basically we are reusing the same key , only
updating it by sha256 digest for each new block.
                
                --->Skill Issue<---
"""
from Crypto.Util.number import *
from pwn import xor
from hashlib import sha256
plaintext=b'Great and Noble Leader of the Tariaki, ,I am writing to you' 
plaintext=(plaintext[:32])
#flag contains 7 blocks of 32 bytes each
flag='fd94e649fc4c898297f2acd4cb6661d5b69c5bb51448687f60c7531a97a0e683072bbd92adc5a871e9ab3c188741948e20ef9afe8bcc601555c29fa6b61de710a718571c09e89027413e2d94fd3126300eff106e2e4d0d4f7dc8744827731dc6ee587a982f4599a2dec253743c02b9ae1c3847a810778a20d1dff34a2c69b11c06015a8212d242ef807edbf888f56943065d730a703e27fa3bbb2f1309835469a3e0c8ded7d676ddb663fdb6508db9599018cb4049b00a5ba1690ca205e64ddc29fd74a6969b7dead69a7341ff4f32a3f09c349d92e0b21737f26a85bfa2a10d'
flag=bytes.fromhex(flag)

flag_blocks=[]
for i in range(0, len(flag), 32):
    flag_blocks.append(flag[i:i+32])

key_blocks=[]
key_blocks.append(xor(plaintext,flag_blocks[0]))
for i in range(1,7):
    key_blocks.append(sha256(key_blocks[i-1]).digest())
    
for x,y in zip(key_blocks,flag_blocks):
    print(xor(x,y),end='')
    

