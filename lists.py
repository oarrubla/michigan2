
#listas
print([1,24,76])
print(["red","yellow","blue"])
print(["red",24,98.6])
print([1,[5,6],7])
print([])

#lists and definite loops
friends = ["Joseph","Glenn","Sally"]
for friend in friends:
    print("Happy new year:",friend)
print("Done")

#looking inside lists
friends = ["Joseph","Glenn","Sally"]
print(friends[1])

#lists are mutable, strings are not.
fruit = "BANANA"
x=fruit.lower()
print(x)
lotto=[2,14,26,41,63]
print(lotto)
lotto[2]=99
print(lotto)

#How long is a lists?
greet = "Hello Bob"
print(len(greet))

x=[1,2,"joe",99]
print(len(x))

#Using the range function
print(range(4))
friends = ["joseph","Glenn","Sally"]
print(len(friends))

print(range(len(friends)))

#a tale of two loops------------------------------------------------

#imprime directamente lo que hay en la lista, pero no funciona para contar
friends=["joseph","Glenn","Sally"]
for friend in friends:
    print("Happy new year:",friend)

#este va por cada rango de la lista y permitiria contar si es necesario
# it is know as a countan loop (loop para contar)
#es un loop que itera en un rango de numeros
for i in range(len(friends)):
    friend=friends[i]
    print("Happy new year:", friend)
