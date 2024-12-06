from random import randint
import csv

def letter_tellen(woord, invoerletter):
    aantal = 0

    for letter in woord:
        if letter == invoerletter:
            aantal = aantal + 1

    uitvoer = 'De letter ' + str(invoerletter) + ' komt ' + str(aantal) + ' keer voor in ' + str(woord) + '.'
    return(uitvoer)


# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()


with open('woordenlijst.csv') as woordenlijst:
    lijst = csv.reader(woordenlijst, delimiter=',')
    for woord in lijst:
        # woord is een lijst, dus eerst omzetten naar string
        woord = str(woord[0])
        keuze = randint(0, 5)
        if keuze: # kies een letter die voorkomt
            index = randint(0, len(woord)-1)
            letter = woord[index]
            with open('0.in', 'a') as f:
                f.write(str(woord))
                f.write('\n')
                f.write(str(letter))
                f.write('\n')
            with open('0.out', 'a') as f:
                f.write(letter_tellen(woord, letter))
                f.write('\n')
        else: # kies een willekeurige letter die niet voorkomt
            alfabet = 'abcdefghijklmnopqrstuvwxyz'
            while True:
                index = randint(0, len(alfabet)-1)
                letter = alfabet[index]
                if letter not in woord:
                    break
            with open('0.in', 'a') as f:
                f.write(str(woord))
                f.write('\n')
                f.write(str(letter))
                f.write('\n')
            with open('0.out', 'a') as f:
                f.write(letter_tellen(woord, letter))
                f.write('\n')
