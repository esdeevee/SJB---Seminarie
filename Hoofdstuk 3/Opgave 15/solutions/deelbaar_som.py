n = eval(input("Geef een natuurlijk getal: "))
som = 0

for i in range(n):
  if(i% 3 == 0 or i%5 == 0): 
    # print(i)
    som = som + i

print(som)
