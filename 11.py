from datetime import datetime
import math

start = datetime.now()
prim=13
i=6
while i<10001:
    prim+=1
    flag=True
    osztok=2
    if prim%2!=0:
        j=3
        while j<(math.sqrt(prim)+1):
            if prim%j!=0:
                j+=1
            else:
                flag=False
                break
    else:
        flag=False
    if osztok==2 and flag==True:
        i+=1

print(prim)
print (datetime.now()-start)