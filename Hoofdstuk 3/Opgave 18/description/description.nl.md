### Opgave

Schrijf een programma dat vraagt om twee woorden. Druk alle letters af die de woorden gemeen hebben. Je mag hoofdletters beschouwen als verschillend van kleine letters, maar iedere letter mag niet meer dan één keer gerapporteerd worden. Zo hebben de strings peer en een bijvoorbeeld slechts één letter gemeen, namelijk de letter e.


### Voorbeeld

**Invoer:**

    Geef een eerste woord: seminarie
    Geef een tweede woord: De Vusser

**Uitvoer:**

    De woorden seminarie en De Vusser hebben volgende letters gemeenschappelijk: e, s, r


Je zal voor deze opgave waarschijnlijk een nieuw commando nodig hebben. Probeer volgende code en de bijhorende uitvoer te begrijpen voor je aan deze opgave begint:

    string = "seminarie"
    print("i" in string)
    print("t" in string)
    print("I" in string)

    True
    False
    False
