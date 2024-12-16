def patroon(n):
    uitvoer = ''
    
    # de eerste lijn bestaat uit n keer de letter X
    uitvoer += (n * 'X') + '\n'

    # n is even
    if n%2 == 0:
        # nu komen er lijnen die die de diagonalen opstellen
        for i in range(int(n/2 - 1)):
            uitvoer += (i+1)* '.' + 'X' + (n-4-i*2)* '.' + 'X' + (i+1)* '.' + '\n'

        for i in range(int(n/2 - 2), -1, -1):
            uitvoer += (i+1)* '.' + 'X' + (n-4-i*2)* '.' + 'X' + (i+1)* '.' + '\n'

    else:
        # nu komen er lijnen die die de diagonalen opstellen
        for i in range(int((n-1)/2 - 1)):
            uitvoer += (i+1)* '.' + 'X' + (n-4-i*2)* '.' + 'X' + (i+1)* '.' + '\n'

        uitvoer += int((n-1)/2) * '.' + 'X' + int((n-1)/2) * '.' + '\n'

        for i in range(int((n-1)/2 - 1), 0, -1):
            uitvoer += (i)* '.' + 'X' + (n-i*2-2)* '.' + 'X' + (i)* '.' + '\n'
        
    # de laatste lijn bestaat uit n keer de letter X
    uitvoer += (n * 'X')


    return(uitvoer)


# wis alle gegevens in in.csv
f = open("0.in", "w")
f.truncate()
f.close()
# wis alle gegevens in out.csv
f = open("0.out", "w")
f.truncate()
f.close()


for i in range(3, 33):
    with open('0.in', 'a') as f:
        f.write(str(i))
        f.write('\n')
    with open('0.out', 'a') as f:
        f.write(patroon(i))
        f.write('\n')
        f.write('\n')
    
