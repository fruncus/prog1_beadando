def translator(text):
    listed=text.split(" ")
    pig=[]
    for i in listed:
        string=i[1:]+i[0].lower()+"ay"
        pig.append(string)
    pig[0]=pig[0].capitalize()
    for i in pig:
        print(i, end=" ")



phrase=input("írj egy mondatot:")
print("Pig latinul:")
translator(phrase)