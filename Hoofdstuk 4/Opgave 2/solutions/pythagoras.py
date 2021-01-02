from math import sqrt

def pythagoras(a, b):
  c = sqrt(a**2 + b**2)
  return(c)

a = eval(input("Geef de lengte van de eerste rechthoekszijde: "))
b = eval(input("Geef de lengte van de tweede rechthoekszijde: "))
print("De schuine zijde heeft een lengte van", pythagoras(a,b))
