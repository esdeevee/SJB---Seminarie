### Opgave

[Hier vind je een link naar een pdf van de opgave (Vlaamse  programmeerwedstrijd 2013).](https://github.com/vlaamseprogrammeerwedstrijd/opgaves/blob/master/2013/cat1/balans/balans.pdf)

Een balans is een soort weegschaal die enkel aangeeft of zij al dan niet in evenwicht is (aan elke zijde van de arm hangt dan een gelijk gewicht).

Je krijgt een reeks beschikbare gewichten en je moet een programma schrijven dat bepaalt of een balans met aan de ene zijde een bepaald testgewicht (in kilogram) in evenwicht kan gebracht worden door precies twee beschikbare gewichten aan de andere zijde van de balans te plaatsen. Stel dat de volgende gewichten beschikbaar zijn (in kilogram):

3 9 7 5 15

Wanneer er dan een testgewicht van 14 kg aan de ene zijde van de balans hangt, kunnen we deze in evenwicht brengen door de gewichten van 9 en 5 kilogram aan de andere zijde te plaatsen. Anderzijds kunnen we met die beschikbare gewichten de balans niet in evenwicht brengen wanneer er aan de ene zijde een testgewicht van 13 kilogram hangt. Ook voor bv. een testgewicht van 6 kilogram lukt dit niet aangezien we het beschikbare gewicht van 3 kilogram slechts eenmaal kunnen gebruiken.

### Invoer

De eerste regel bevat een getal n (1 ≤ n ≤ 250) en stelt het aantal opgaven voor. Daarna volgen de n opgaven. Elke opgave bestaat uit drie regels: eerst een regel met een getal t (1 ≤ t ≤ 1000). Dit stelt het aantal beschikbare gewichten voor. Dan volgt een regel met t gehele getallen, gescheiden door spaties. Dit zijn de beschikbare gewichten (in kilogram). In de invoer zullen alle gewichten verschillend zijn. Het maximale gewicht dat kan worden gebruikt bedraagt 10000 kg. Uiteindelijk komt er een regel met een getal k (1 ≤ k ≤ 20000) dat het testgewicht aangeeft.

### Uitvoer
De uitvoer bestaat uit n regels: één regel per opgave. Op elke regel staat eerst de waarde van het testgewicht, daarna een spatie, gevolgd door het woord "JA" of het woord "NEEN". Wanneer voor het testgewicht in kwestie de balans in evenwicht kan gebracht worden met twee van de beschikbare gewichten wordt "JA" afgedrukt, in het andere geval "NEEN".

### Voorbeeld
**Invoer:**

    5
    10
    1 2 3 4 5 6 7 8 9 10
    3
    5
    3 9 7 5 15
    13
    10
    1 2 3 4 5 6 7 8 9 10
    2
    5
    3 9 7 5 15
    14
    5
    3 9 7 5 15
    6    

**Uitvoer:**

    3 JA
    13 NEEN
    2 NEEN
    14 JA
    6 NEEN    
