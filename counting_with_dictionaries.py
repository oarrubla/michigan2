#most common name?
ccc = dict()
ccc["csev"]=1
ccc["cwen"]=1
print(ccc)
ccc["cwen"] += 1
print(ccc)

#si las "key" no existen en el diccionario, arroja un error
print("csev" in ccc)

counts = dict()
names = ["csev","cwen","csev","zquian","cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# the get method for dictionaries

if name in counts:
    x = counts[name]
else:
    x = 0

#linea para contar mas facilmente los elementos en un diccionario sin ser un look (porque es funcion build in)
x = counts.get(name,0)  #get(key,default) key es lo que quieres buscar, el cero es default y no se cambia. el cero es el valor inicial que se asigna a la key
print(x)


#get es para simplificar el contar en diccionarios
counts = dict()
names = ["csev","cwen","csev","zquian","cwen"]
for name in names:
    counts[name] = counts.get(name,0) + 1
print(counts)


#-------------------------------------------------------------------

#counting pattern
counts = dict()
print("Ingresa el texto: ")
line = input("")

words = line.split()
print("Words", words)

print("Counting.....")
for word in words:
    counts[word]=counts.get(word,0) + 1
print("Counts",counts)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#Define loops and dictionaries
counts = {"chuck":1,"Fred":42,"jan":100}
for key in counts:
    print(key,counts[key])


#Retrieving lists of keys and values
jjj={"chuck":1,"Fred":42,"jan":100}
print(list(jjj)) #aqui se convierte el diccionario en una lista donde solo conserva las keys
print(jjj.keys()) #imprime una lista directamente del diccionario con las llaves
print(jjj.values()) #imprime una lista directamente del diccionario con los valores
print(jjj.items()) #imprime todo el diccionario en forma de lista (key,value) = tuple

jjj={"chuck":1,"Fred":42,"jan":100}
for aaa,bbb in jjj.items(): #aaa itera en las llaves,bbb itera en los valores
    print(aaa,bbb)