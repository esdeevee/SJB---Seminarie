n = eval(input("Geef een natuurlijk getal: "))

som = 0
a = 1
b = 1
#print(a)
#print(b)

while True:
  c = a+b
  if c < n:
    a = b
    b = c
    # print(c)
    if(c%2 == 0):
      som = som + c
  else:
    break

print(som)
