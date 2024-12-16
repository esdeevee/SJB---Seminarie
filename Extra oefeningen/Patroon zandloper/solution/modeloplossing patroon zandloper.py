n = int(input('Geef de waarde van n: '))

# de eerste lijn bestaat uit n keer de letter Z
print(n * 'X')

# n is even
if n%2 == 0:
    # nu komen er n-2 lijnen die bestaan die de diagonaal opstellen
    for i in range(int(n/2 - 1)):
        print((i+1)* '.' + 'X' + (n-4-i*2)* '.' + 'X' + (i+1)* '.')

    for i in range(int(n/2 - 2), -1, -1):
        print((i+1)* '.' + 'X' + (n-4-i*2)* '.' + 'X' + (i+1)* '.')

else:
    # nu komen er n-2 lijnen die bestaan die de diagonaal opstellen
    for i in range(int((n-1)/2 - 1)):
        print((i+1)* '.' + 'X' + (n-4-i*2)* '.' + 'X' + (i+1)* '.')

    print(int((n-1)/2) * '.' + 'X' + int((n-1)/2) * '.')

    for i in range(int((n-1)/2 - 1), 0, -1):
        print((i)* '.' + 'X' + (n-i*2-2)* '.' + 'X' + (i)* '.')
    
# de laatste lijn bestaat uit n keer de letter Z
print(n * 'X')
