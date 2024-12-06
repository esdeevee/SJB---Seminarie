woord = input('Geef een woord: ')
invoerletter = input('Geef een letter: ')

aantal = 0

for letter in woord:
    if letter == invoerletter:
        aantal = aantal + 1

print('De letter ' + invoerletter + ' komt ' + str(aantal) + ' keer voor in ' + woord + '.')
