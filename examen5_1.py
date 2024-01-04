han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    #print("Line:",line)
    wds = line.split() #convierte cada linea en una lista
    #print("Words",wds)

    #a las siguientes lineas se les conoce como guardian
    #Guardian
    #se usa para que no falle si hay listas vacias
    if len(wds) <1:
        continue

    """
    otra forma de hacer el guardian es con:
    if line == "":
        print("Skip Blank")
        continue
    """

    if wds[0] != "From": #si no se pone el guardian, falla al encontrar lineas en blanco
        #print("Ignore")
        continue
    print(wds[1])


print("-----------------------------------------------------------------")

han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    #guardian in a compound statement
    if len(wds) <1 or wds[0] != "From":
        continue
    print(wds[1])