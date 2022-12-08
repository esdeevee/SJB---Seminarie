### Inleiding

Wanneer je in het spelletje **Risk** met je legers een naburig leger aanvalt, volgt een spelletje met dobbelstenen tot één van de legers volledig uitgeroeid wordt. Het aantal beschikbare dobbelstenen hangt af van de rol die je speelt tijdens een aanval.

* 🅰, de aanvaller, beschikt over drie dobbelstenen;
* 🆅, de verdediger, beschikt over twee dobbelstenen.

### Aanvallen

Nadat beide spelers hun dobbelstenen geworpen hebben, sorteren ze eerst de dobbelstenen van groot naar klein.

* 🅰 ⚅ ⚁ ⚀
* 🆅 ⚄ ⚂

Vervolgens vergelijken beide spelers de dobbelsteen met het hoogste aantal ogen. In dit geval wint de aanvaller want 6 is groter dan 5. De verdediger verliest één leger.

* 🅰 ⚅ ⚁ ⚀
* 🆅 ⚄ ⚂

Ten slotte vergelijken beide spelers de dobbelsteen met het op één na hoogste aantal ogen. In dit geval wint de verdediger want 3 is groter dan 2. De aanvaller verliest één leger.

* 🅰 ⚅ ⚁ ⚀
* 🆅 ⚄ ⚂

In dit voorbeeld verliezen zowel de aanvaller als de verdediger een leger.

### Gelijke stand

Er is een speciaal geval bij het vergelijken van de dobbelstenen: bij een gelijk aantal ogen verliest de aanvaller altijd. In de volgende aanval verliest de aanvaller twee legers.

* 🅰 ⚄ ⚄ ⚃
* 🆅 ⚄ ⚄

### Opgave

Het is de bedoeling dat je het resultaat van een aanval bij Risk berekent. Doe dit stapje voor stapje:

* Schrijf een functie `tweede_hoogste()` die drie natuurlijke getallen inleest. Deze getallen stellen de drie dobbelstenen voor van de aanvaller. De uitvoer van deze functie is het op één na hoogste getal van deze drie.
* Schrijf vervolgens een functie `bereken_verlies()` die vijf natuurlijke getallen inleest. De eerste drie getallen stellen de drie dobbelstenen van de aanvaller voor. De twee laatste getallen stellen de dobbelstenen van de verdediger voor. De uitvoer van deze functie is het aantal legers dat de aanvaller verliest bij deze aanval.

**Opgelet!** Het automatische evaluatiesysteem van Dodona raakt in de war als je - behalve je functiedefinitie - ook een hoofdprogramma schrijft. 

### Voorbeeld

**Invoer:**

    > tweede_hoogste(5, 3, 5)

**Uitvoer:**

    5

**Invoer:**

    > bereken_verlies(2, 6, 5, 2, 2)

**Uitvoer:**

    0

**Invoer:**

    > bereken_verlies(4, 1, 4, 2, 5)

**Uitvoer:**

    1

**Invoer:**

    > bereken_verlies(5, 2, 1, 5, 4)

**Uitvoer:**

    2
