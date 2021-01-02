def aantaldagen(jaar, maand):
  lijst_31 = ["januari", "maart", "mei", "juli", "augustus", "oktober", "december"]
  lijst_30 = ["april", "juni", "september", "november"]
  if(maand in lijst_31):
    aantal_dagen = 31
  elif(maand in lijst_30):
    aantal_dagen = 30
  elif(maand == "februari"):
    if jaar % 400 == 0:
      aantal_dagen = 29
    elif jaar % 100 == 0:
      aantal_dagen = 28
    elif jaar % 4 == 0:
      aantal_dagen = 29
    else:
      aantal_dagen = 28
  return(aantal_dagen)

jaar = eval(input("Geef een jaartal: "))
maand = input("Geef een maand: ")
print(maand, jaar, "heeft", aantaldagen(jaar, maand), "dagen")
