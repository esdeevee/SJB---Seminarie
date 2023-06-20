from random import randint
import csv

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


print(ggd(1239, 735))

# wis alle gegevens in 0.in
f = open('0.in', 'w')
f.truncate()
f.close()

# wis alle gegevens in 0.out
f = open('0.out', 'w')
f.truncate()
f.close()

for j in range(10):
    for i in range(10):
        a = randint(10**(2+j), 10**(3+j))
        b = randint(10**(2+j), 10**(3+j))
        with open('0.in', 'a') as f:
            f.write(str(a))
            f.write('\n')
            f.write(str(b))
            f.write('\n')
        m = Bezout_Bachet(a, b)
        l = int((int(ggd(a,b)) - m*min(a,b))/max(a,b))
        with open('0.out', 'a') as f:
            uitvoer = ''
            uitvoer = str(l) + ' * ' + str(max(a,b)) + ' + ' + str(m) + ' * ' + str(min(a, b)) + ' = ' + str(ggd(a,b))
            f.write(uitvoer)
            f.write('\n')
                
