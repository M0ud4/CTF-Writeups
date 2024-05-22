from pwn import *
import re
from time import sleep

def knapsack(v, w, n, W):
    # Initialize a DP array with zero values
    V = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build table V[][] in bottom-up manner
    for i in range(1, n + 1):
        for wx in range(W + 1):
            if w[i - 1] <= wx:
                V[i][wx] = max(V[i - 1][wx], v[i - 1] + V[i - 1][wx - w[i - 1]])
            else:
                V[i][wx] = V[i - 1][wx]
    
    return V[n][W]

r = remote('94.237.53.103', 53096)
sleep(0.3)
count = 0

while count < 100:
    print(f'Count: {count}')
    conn = r.recv().decode()
    print(conn)
    if 'Test' in conn:
        reg = re.findall(r'\n\d+.*', conn)
        for i in range(len(reg)):
            reg[i] = str(reg[i].strip('\n'))
        
        n, c = map(int, reg[0].split())
        ww = []
        vv = []
        for j in range(1, len(reg)):
            row = reg[j].split(' ')
            ww.append(int(row[0]))
            vv.append(int(row[1]))

        x = str(knapsack(v=vv, w=ww, n=n, W=c))
        r.sendline(x)
        sleep(1.5)
        count += 1

r.interactive()
