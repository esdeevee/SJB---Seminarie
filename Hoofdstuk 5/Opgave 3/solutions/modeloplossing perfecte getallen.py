# we vragen aan de gebruiker een natuurlijk getal
grens = int(input("Geef een natuurlijk getal: "))

# we overlopen alle getallen van 1 tot en met de ingevoerde grens
for getal in range(1, grens + 1):
    
    # lijst om alle echte delers van het getal op te slaan
    delers = []
    
    # we zoeken alle echte delers van 'getal'
    # een echte deler is een getal dat:
    # - het getal deelt zonder rest
    # - kleiner is dan het getal zelf
    for i in range(1, getal):
        if getal % i == 0:
            # als i een deler is, voegen we die toe aan de lijst
            delers.append(i)
    
    # we berekenen de som van alle echte delers
    som = 0
    for deler in delers:
        som += deler
    
    # als de som gelijk is aan het getal zelf → perfect getal
    if som == getal:
        
        # we bouwen een mooie tekst op zoals in het voorbeeld
        # bv: 6 = 1 + 2 + 3
        tekst = str(getal) + " = "
        
        for j in range(len(delers)):
            tekst += str(delers[j])
            
            # we voegen " + " toe tussen de getallen, maar niet na het laatste
            if j < len(delers) - 1:
                tekst += " + "
        
        # we printen het resultaat
        print(tekst)
