num=[]
i=100
j=100
while i<1000:
    while j<1000:
        number=i*j
        number_string=str(number)
        ch=number_string[0]
        ch2=number_string[:-1]
        if ch==ch2:
            flag=True
        else:
            flag=False
        if flag==True:
            ch+=1
            ch2-=1
    i+=1