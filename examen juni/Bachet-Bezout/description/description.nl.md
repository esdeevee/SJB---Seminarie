### Opgave

BELANGRIJK: schrijf de namen van alle groepsleden in een eerste lijn commentaar.

Als alles goed is, heeft minstens één iemand in je team Opgave 6 gemaakt van Hoofdstuk 2.3. Het algoritme van Euclides is een bijzonder snel algoritme om de grootste gemene deler van twee getallen te berekenen. In deze opgave gaan we dit algoritme wat veralgemenen.

De stelling van Bachet-Bézout garandeert dat de grootste gemene deler van twee getallen $a$ en $b$ geschreven kan worden als een lineaire combinatie van $a$ en $b$. Men kan bewijzen dat er voor elke $a$ en $b$ (niet allebei gelijk aan nul) gehele getallen $l$ en $m$ bestaan zodat $ggd(a,b) = l*a + m*b$. Deze $l$ en $m$ zijn niet uniek.

Kijk op het uitgedeelde blad om te weten te komen hoe je de getallen $l$ en $m$ kan berekenen. Zorg dat je het algoritme goed onder de knie hebt voor je het begint te implementeren. 

Pas je programma voor het algoritme van Euclides nu aan. Je programma vraagt nog altijd twee natuurlijke getallen. Het berekent nog altijd de grootste gemene deler van die twee getallen. Maar nu berekent je programma ook de getallen $l$ en $m$. Je programma toont de resulterende lineaire combinatie.


### Voorbeeld

**Invoer:**

    Geef een eerste natuurlijk getal: 735
    Geef een tweede natuurlijk getal: 1239


**Uitvoer:**

    -16 * 1239 + 27 * 735 = 21
    
    
**Invoer:**

    Geef een eerste natuurlijk getal: 529288119948
    Geef een tweede natuurlijk getal: 421368530150


**Uitvoer:**

    64878223649 * 529288119948 + -81494631335 * 421368530150 = 2
