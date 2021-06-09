### Opgave

[Hier vind je een link naar een pdf van de opgave (Vlaamse  programmeerwedstrijd 2014).](https://github.com/vlaamseprogrammeerwedstrijd/opgaves/blob/master/2014/cat1/eendjes/eendjes.pdf)

Let op: de opgave is sterk gebaseerd op deze vraag, maar ik heb er iets aan moeten aanpassen. De opgave is wat je op Dodona terugvindt!

Eendjes vissen is een gekend spel van op de kermis. De eendjes komen een per een voorbij en de speler kan er een aantal uit vissen. Elk eendje heeft als waarde een geheel getal tussen 1 en 5. In deze opgave wordt een variant op het klassieke eendjes vissen beschouwd. De speler ziet op- voorhand de waarden van alle eendjes die voorbij komen en moet per spel vier opeenvolgende eendjes selecteren om een zo hoog mogelijke score te behalen. Bijvoorbeeld, uit de reeks bestaande uit 10 eendjes met waarden

5 2 4 1 1 5 4 4 3 2

moet de speler de vier eendjes vanaf positie 6 vissen om de hoogste score te behalen (5 + 4 + 4 + 3 = 16).

### Invoer
De eerste regel van de invoer bevat een geheel getal 1 ≤ n ≤ 200 dat het aantal testgevallen aangeeft – dus het aantal keer dat er gespeeld wordt. Per spel komen er steeds 13 eendjes voorbij (dit is anders dan in de VPW-opgave). Per geval volgens dan telkens 13 regels met op elke regel één enkel geheel getal dat de waarde van het eendje voorstelt. Alle waarden van de eendjes zijn gehele getallen gelegen tussen 1 en 5.


### Uitvoer
Per spel moet de positie worden gevonden van het eerste van vier opeenvolgende eendjes die samen de hoogste score geven. Als meerdere beginposities dezelfde score als resultaat geven dan wordt de eerste van deze beginposities gegeven. De uitvoer bestaat uit evenveel regels als er spelen zijn. Elke regel bevat het nummer van de beste beginpositie.


### Voorbeeld
In onderstaand voorbeeld wordt er 2 keer gespeeld.

**Invoer:**

    2
    5
    2
    4
    1
    1
    5
    4
    4
    3
    2
    4   
    1
    4
    2
    4
    4
    5
    2
    1
    3

**Uitvoer:**

    6
    4
