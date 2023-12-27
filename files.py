xfile = open("C:\github\michigan2\Carta Admisión MinTIC 2024-1.txt")
count = 0
for linea in xfile: #en un for loop cada linea es independiente de la otra linea
    print(linea)
    count += 1
    print("linrs numero:", count)
print("Total de lineas:", count)


print("-----------------------------")

xfile = open("C:\github\michigan2\Carta Admisión MinTIC 2024-1.txt")
inp = xfile.read() #pone todo como en un solo string
print(len(inp))
print(inp[:20])

print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


#loop para buscar que la linea comience por una palabra e imprimirla
fhand = open("C:\github\michigan2\Carta Admisión MinTIC 2024-1.txt")
for line in fhand:
    if line.startswith("Que"):
        print(line) #agrega una nueva linea al finalizar el print y este se suma con el "enter" al finalizar cada linea

#para corregir la linea extra se debe de hacer lo siguiente
fhand = open("C:\github\michigan2\Carta Admisión MinTIC 2024-1.txt")
for line in fhand:
    line = line.rstrip() #elimina el ultimo enter de la linea
    if line.startswith("Que"): #si comienza con la palabra que, imprimir
        print(line)


print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")


fhand = open("C:\github\michigan2\Carta Admisión MinTIC 2024-1.txt")
for line in fhand:
    line = line.rstrip() 
    if not line.startswith("Que"): #si no comienza con la palabra que, no lo imprima
        continue
    print(line)


print("ccccccccccccccccccccccccccc")

fname = input("Enter the file name: ")
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()
count = 0
for line in fhand:
    if line.startswith("Que"):
        count += 1
print("There were",count,"subject line in",fname)

