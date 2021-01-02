woord_1 = input("Geef een eerste woord: ")
woord_2 = input("Geef een tweede woord: ")

uitvoer = ""

for letter in woord_2:
  if letter in woord_1 and uitvoer == "":
    uitvoer = uitvoer + letter
  elif letter in woord_1 and not(letter in uitvoer):
    uitvoer = uitvoer + ", " + letter
print("De woorden", woord_1, "en", woord_2, "hebben de volgende letters gemeenschappelijk:", uitvoer)
