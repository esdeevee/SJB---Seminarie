### Inleiding

We maken in deze opgave gebruik van de irrationale functie

$$
\mathsf{f(x) = \sqrt{x-2}.}
$$



### Opgave

Schrijf een functie `interpreteer_f()` die één parameter verwacht. Deze parameter stelt een x-waarde voor.
* Als x een nulpunt is van de functie, geeft `interpreteer_f()` dit aan.
* Als x tot het domein van f behoort maar geen nulpunt is, geeft `interpreteer_f()` de functiewaarde voor x, afgerond op twee cijfers na de komma.
* Als x niet tot het domein van f behoort, geeft `interpreteer_f()` dit ook aan.

Kijk naar de voorbeelden voor de precieze uitvoer die verwacht wordt.

**Opgelet!** Het automatische evaluatiesysteem van Dodona raakt in de war als je - behalve je functiedefinitie - ook een hoofdprogramma schrijft. Schrijf dus niet meer code dan gevraagd!

### Voorbeeld

**Invoer:**

    > interpreteer_f(2)

**Uitvoer:**

    2 is een nulpunt van f(x)

**Invoer:**

    > interpreteer_f(-4.5)

**Uitvoer:**

    -4.5 behoort niet tot dom f

**Invoer:**

    > interpreteer_f(10.37)

**Uitvoer:**

    f(10.37) = 2.89
