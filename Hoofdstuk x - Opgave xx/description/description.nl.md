Binnen het ISBN-10 (International Standard Book Numbering) systeem dat tot eind 2006 gebruikt werd, kreeg elk boek een unieke code toegewezen die bestaat uit 10 cijfers. De eerste 9 daarvan geven informatie over het boek zelf, terwijl het laatste louter een controlecijfer is dat dient om foutieve ISBN-10 codes te detecteren.

Indien $$x_1, \ldots, x_9$$ de eerste 9 cijfers van een ISBN-10 code voorstellen, dan wordt het controlecijfer $$x_{10}$$ als volgt berekend: \[x_{10} = (x_1+ 2x_2+ 3x_3+ 4x_4+ 5x_5+ 6x_6+ 7x_7+ 8x_8+ 9x_9)\!\!\!\!\mod{11}\] Het controlecijfer $$x_{10}$$ kan m.a.w. de waarden 0 tot en met 10 aannemen. Gevraagd wordt om een programma te schrijven dat het controlecijfer berekent op basis van de eerste negen cijfers van een ISBN-10 code.

Invoer
Negen natuurlijke getallen $$x_1, \ldots, x_9$$ ($$0 \leq x_1, \ldots, x_9 \leq 9$$), elk op een afzonderlijke regel. Deze stellen de eerste negen cijfers van een gegeven ISBN-10 code voor.

Uitvoer
Eén regel die een natuurlijk getal bevat: het controlecijfer dat correspondeert met de gegeven cijfers van een ISBN-10 code. Zorg ervoor dat dit natuurlijk getal geen voorloopnullen heeft.

Voorbeeld
Invoer:

9
9
7
1
5
0
2
1
0