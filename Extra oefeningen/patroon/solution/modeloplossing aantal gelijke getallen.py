a = int(input('Geef het eerste getal: '))
b = int(input('Geef het tweede getal: '))
c = int(input('Geef het derde getal: '))

if a == b and a == c:
    print(3)

elif a==b or b == c or a == c:
    print(2)

else:
    print(0)
