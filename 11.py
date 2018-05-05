from datetime import datetime
from math import sqrt


def nthprim(n):
    start = datetime.now()
    l=[2,3,5,7,11,13]
    prim=13
    i=6
    while i<n:
        prim+=1
        flag=True
        for j in l:
            if j<(sqrt(prim)+1):
                if prim%j!=0:
                    continue
                else:
                    flag=False
                    break
        if flag==True:
            l.append(prim)
            i+=1
    print(datetime.now() - start)
    return prim


def nthprims(n):
    start = datetime.now()
    prim=13
    i=6
    while i<n:
        prim+=1
        flag=True
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
        if flag==True:
            i+=1
    print(datetime.now() - start)
    return prim


# print(nthprim(10001))
print(nthprims(10001))
