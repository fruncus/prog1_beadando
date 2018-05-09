def palindrome(n):
    lista=[]
    for i in range(999,n,-1):
        for j in range(999,n,-1):
            number=i*j
            number_string=str(number)
            k=len(number_string)/2
            kozepe=int(k)
            eleje=number_string[0:kozepe]
            vege=number_string[kozepe:]
            vege_visszafele=vege[::-1]
            if eleje==vege_visszafele:
                lista.append(number)
    max=lista[0]
    for i in lista:
        if i>max:
            max=i
    return max

print("the largest palindrome made from the product of two 3 digit numbers is",palindrome(99))
