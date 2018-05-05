from datetime import datetime
from math import sqrt

def nthprim(n):
    prim=13
    i=6
    while i<n:
        prim+=1
        flag=True
        osztok=2
        if prim%2!=0:
            j=3
            while j<(sqrt(prim)+1):
                if prim%j!=0:
                    j+=1
                else:
                    flag=False
                    break
        else:
            flag=False
        if osztok==2 and flag==True:
            i+=1
    return prim

start = datetime.now()
print(nthprim(10001))
print (datetime.now()-start)