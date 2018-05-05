i=999
j=999
while i>99:
    while j>99:
        number=i*j
        number_string=str(number)
        k=int(len(number_string))/2
        for e in range(int(k)):
            for f in range (int(len(number_string))-1,int(k),-1):
                if number_string[e]==number_string[f]:
                    flag=True
                    continue
                else:
                    flag=False
                    break
        if flag==True:
            print(number)
            exit()
    i-=1
    j-=1

