import numpy as np

# primek=[1]
# p=1
# while len(primek)<10002:
#     p+=1
#     osztok=0
#     for i in range(1,p+1):
#         if p%i==0:
#             osztok+=1
#     if osztok==2:
#         primek.append(p)
# print(primek[10001])

# prim=[]
# for p in range (2,10002):
#     k=p
#     for i in range (k+1,10002):
#         if i%k!=0:
#             prim.append(i)
# prim.append(1)
# print(prim)

# prime=set(range(2,10002))
# for p in range (2,10002):
#     k=p
#     while k<10002:
#         k = k + p
#         prime.discard(k)
# print(prime|{1})
# print(len(prime))



prim=4
i=2
while i<10001:
    prim+=1
    flag=True
    osztok=2
    if prim%2!=0:
        j=2
        while j<((prim//2)+1):
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