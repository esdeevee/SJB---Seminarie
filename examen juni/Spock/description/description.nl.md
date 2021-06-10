### Context

Je kent wellicht wel het spelletje blad-steen-schaar, waarbij twee spelers eerst aftellen en daarna met de hand tegelijkertijd de vorm maken van een steen (een vuist), een schaar (twee uitgestoken vingers) of een blad (een vlakke hand). Hierbij verslaat de steen de schaar, de schaar het blad en het blad de steen. Indien beide spelers dezelfde keuze maken, dan wint geen van beiden.

Sam Kass en Karen Bryla bedachten een uitbreiding van dit klassieke spelletje, en noemden het blad-steen-hagedis-Spock-schaar (Rock, Paper, Scissors, Lizard, Spock). Het werkt volgens hetzelfde principe, maar er komen twee extra wapens bij: een hagedis (voorgesteld door met de hand een kousenpopachtige mond te vormen) en Spock (voorgesteld door de [Vulcaanse groet](http://nl.wikipedia.org/wiki/Vulcaanse_groet) uit de Star Trek reeks te maken). Hierdoor wordt de kans op een gelijkspel kleiner (van 1/3 naar 1/5). "Rock, Paper, Scissors, Lizard, Spock" komt een aantal keer voor in de heerlijke reeks [The Big Bang Theory](http://nl.wikipedia.org/wiki/The_Big_Bang_Theory_%28televisieserie%29).

Klik [hier](https://www.youtube.com/watch?v=iSHPVCBsnLw) of [hier](https://www.youtube.com/watch?v=x5Q6-wMx-K8) voor een scène uit The Big Bang Theory.

Bij een spelletje blad-steen-hagedis-Spock-schaar kiezen twee spelers een handgebaar, waarna ze beide hun keuze tegelijkertijd zichtbaar maken. De winnaar is diegene die de andere speler verslaat. De regels van blad-steen-hagedis-Spock-schaar zijn:

* schaar snijdt blad
* blad bedekt steen
* steen plet hagedis
* hagedis vergiftigt Spock
* Spock smelt schaar
* schaar onthoofdt hagedis
* hagedis eet blad
* blad weerlegt Spock
* Spock verdampt steen
* steen breekt schaar

Er zijn vijftien mogelijke combinaties van de vijf handgebaren. Elk handgebaar verslaat twee van de andere handgebaren en wordt verslagen door de andere twee handgebaren. De originele regels uit het spelletje blad-steen-schaar (steen verslaat schaar, schaar verslaat blad en blad verslaat steen) blijven behouden in het uitgebreide spelletje.

### Opgave

[Hier vind je een link naar een pdf van de opgave (Vlaamse  programmeerwedstrijd 2014).](https://github.com/vlaamseprogrammeerwedstrijd/opgaves/blob/master/2014/cat1/spock/spock.pdf)

Een spelletje bestaat uit een aantal opeenvolgende ronden `R`. Tijdens elke ronde maken 2 spelers tegelijk een zet. Voor elke ronde, bereken welke speler de ronde wint op basis van de regels zoals beschreven hierboven. Bij winst krijgt een speler 1 punt. Bij verlies en gelijkspel 0 punten. Gevraagd wordt om de eindscore (= het totaal aantal punten verdiend over de `R` ronden) van beide spelers af te drukken.

### Invoer

De eerste regel bevat een getal 1 ≤ `N` ≤ 1000 dat het aantal spellen aanduidt dat moet gespeeld worden. Elk spel wordt als volgt beschreven:
* de eerste regel bevat een getal 0 ≤ `R` ≤ 1000 dat het aantal ronden aanduidt.
* de tweede regel bevat de `R` zetten van speler 1, aangeduid als `R` opeenvolgende letters (zonder spaties).
* de derde regel bevat de `R` zetten van speler 2.

De zet van een speler wordt als volgt aangeduid:
* `H` voor **`H`**agedis;
* `S` voor **`S`**pock;
* `P` voor **`P`**apier;
* `C` voor S**`c`**haar;
* `T` voor S**`t`**een.

### Uitvoer
Voor elk spel worden drie getallen `i A B` afgedrukt op 1 regel, met een enkele spatie tussen. `i` is het volgnummer van het spel (te tellen vanaf 1). `A` is de totaalscore van speler 1. `B` is de totaalscore van speler 2.

### Voorbeeld
**Invoer:**

    2
    5
    HPTCS
    TPCSH
    1
    H
    H   

**Uitvoer:**

    1 1 3
    2 0 0
