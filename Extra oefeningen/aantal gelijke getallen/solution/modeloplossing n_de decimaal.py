kommagetal = float(input('Geef een kommagetal: '))
n = int(input('Geef een natuurlijk getal: '))

# zorg dat het gezochte cijfer op de plaats van de eenheid komt
kommagetal = kommagetal * 10**n

# gebruik de absolute waarde, en beschouw hiervan alleen het gehele deel
kommagetal = int(abs(kommagetal))

# bereken het laatste cijfer van dit getal
cijfer = kommagetal % 10

# toon het cijfer
print(cijfer)
