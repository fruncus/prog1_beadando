def translator(text):
    listed=text.split(" ")
    english=[]
    pig=[]
    nyelv=' '
    for veg in listed:
        if veg[-2]=='a' and veg[-1]=='y':
            nyelv='piglatin'
        else:
            nyelv='angol'

    if nyelv=='piglatin':
        for i in listed:
            helyes=i[-3]+i[:-3]
            english.append(helyes)
        english[0]=english[0].capitalize()
        for i in english:
            print(i, end=" ")
    else:
        for i in listed:
            string=i[1:]+i[0].lower()+"ay"
            pig.append(string)
        pig[0]=pig[0].capitalize()
        for i in pig:
            print(i, end=" ")



phrase=input("write something: ")
print("translated: ")
translator(phrase)