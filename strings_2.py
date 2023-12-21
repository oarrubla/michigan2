stuff = "Hello world"
print(type(stuff))
print(dir(stuff)) #aparece todo lo que puedes hacer con la clase string


#in para buscar dentro de un string
fruit = "banana"
print("n" in fruit)
print("m" in fruit)
print("nan" in fruit)
if "a" in fruit:
    print("Found it")

greet = "Hello Bob"
zap = greet.lower() #esta funcion/metodo lower crea una copia del string inicial y no lo modifica
print(zap)
print(greet)
print("Hi there".lower())
print(greet.upper()) #poner todo en mayusculas


#find() funcion para buscar algo en todo el string y arroja el index. si no existe arroja -1
fruit = "banana"
pos =fruit.find("na")
print(pos)
aa = fruit.find("z")
print(aa)

#search and replace
greet = "Hello Bob"
nstr = greet.replace("Bob", "Jane")
print(nstr)

nstr = greet.replace("o","X")
print(nstr)

#strtipping whitespaces - remover espacios en blanco
#lstrip() remueve isquierda, rstrip() remueve derecha, strip()remueve
greet = "     Hello Bob      "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

#Prefixes 
line = "Please have a nice day"
print(line.startswith("Please"))
print(line.startswith("p"))

#parsing and extracting
data = "From stephen.marquard@uct.ac.za Sat Juan 5 09:14:16 2008"
atpos = data.find("@") #desde aqui se hace el slicing
print(atpos)

sppos = data.find(" ",atpos) #hasta el espacio vacio se hace el slicing
print(sppos)

host = data[atpos+1 : sppos] #+1 para que no tome el @
print(host)


