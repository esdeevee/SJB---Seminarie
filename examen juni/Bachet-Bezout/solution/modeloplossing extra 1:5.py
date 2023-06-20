# lees twee natuurlijke getallen in
getal_1 = int(input('Geef een eerste natuurlijk getal: '))
getal_2 = int(input('Geef een tweede natuurlijk getal: '))

# je moet weten welk van deze getallen het grootste is
grootste = max(getal_1, getal_2)
kleinste = min(getal_1, getal_2)

def ggd(getal_1, getal_2):
    # je moet weten welk van deze getallen het grootste is
    grootste = max(getal_1, getal_2)
    kleinste = min(getal_1, getal_2)
    # blijf herhalen
    while True:
        if kleinste == 0:
            # als kleinste gelijk is aan nul, is de ggd gelijk aan grootste
            GGD = grootste
            # onderbreek de while-lus
            break
        else:
            # ggd(grootste, kleinste) = ggd(kleinste, rest)
            rest = grootste % kleinste
            quotient = grootste // kleinste
            grootste = kleinste
            kleinste = rest

    return GGD

def Bezout_Bachet(getal_1, getal_2):
    # je moet weten welk van deze getallen het grootste is
    grootste = max(getal_1, getal_2)
    kleinste = min(getal_1, getal_2)
    
    p = 1
    q = 0
    aantal = 1
    
    # blijf herhalen
    while True:
        # ggd(grootste, kleinste) = ggd(kleinste, rest)
        rest = grootste % kleinste
        quotient = grootste // kleinste
        m = quotient * p + q
        #print(grootste, kleinste, rest, m, p, q)
        grootste = kleinste
        kleinste = rest
      
        if grootste % kleinste == 0:
            # als kleinste een deler is van grootste, is de ggd gelijk aan kleinste
            ggd = kleinste
            m = m * (-1)**aantal
            #print(ggd, m * (-1)**aantal)
            # onderbreek de while-lus
            break
      
        else:
            q = p
            p = m
            aantal +=1

    return m

GGD = ggd(getal_1, getal_2)
m = Bezout_Bachet(getal_1, getal_2)
l = int((int(GGD) - m*min(getal_1,getal_2))/max(getal_1,getal_2))
uitvoer = str(l) + ' * ' + str(max(getal_1,getal_2)) + ' + ' + str(m) + ' * ' + str(min(getal_1,getal_2)) + ' = ' + str(GGD)
print(uitvoer)
