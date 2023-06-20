aantal_hoger_dan_25 = 0
aantal_hoger_dan_30 = 0
aantal_hittegolven = 0

for i in range(31):
    temperatuur = int(input('Geef een temperatuur: '))
    
    if temperatuur >= 30:
        aantal_hoger_dan_30 += 1
        aantal_hoger_dan_25 +=1
        #print(i, temperatuur, aantal_hoger_dan_25, aantal_hoger_dan_30)
    
    elif temperatuur >= 25:
        aantal_hoger_dan_25 +=1
        #print(i, temperatuur, aantal_hoger_dan_25, aantal_hoger_dan_30)
    
    elif temperatuur < 25 and aantal_hoger_dan_25 >= 5 and aantal_hoger_dan_30 >= 2:
        aantal_hittegolven += 1
        aantal_hoger_dan_25 = 0
        aantal_hoger_dan_30 = 0
        #print(i, temperatuur, aantal_hoger_dan_25, aantal_hoger_dan_30)
        #print('Hittegolf!', '\n')
    else:
        aantal_hoger_dan_25 = 0
        aantal_hoger_dan_30 = 0
        #print('\n')
    
    if i == 30 and aantal_hoger_dan_25 >= 5 and aantal_hoger_dan_30 >= 2:
        aantal_hittegolven += 1
        #print('Hittegolf!')
        #print('\n')
    
        
print(aantal_hittegolven)

