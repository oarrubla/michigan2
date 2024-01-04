#List can be slicend using:

t=[9,41,12,3,74,15]
print(t)
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

#list methods
x=list()
print(type(x))
print(dir(x))

#building a list from scratch
stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)
stuff.append("cookie")
print(stuff)

#is something in a list?
some = [1,9,21,10,16]
print(9 in some)
print(14 in some)
print(20 not in some)

#lists are in order
friends = ["Joseph","Glenn","Sally"]
friends.sort()
print(friends)
print(friends[1])

#built in functions and lists
nums = [3,41,12,9,74,15]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))


#este loop solo mantiene 1 numero en memoria
total=0
count=0
while True:
    inp = input("Enter a number:" )
    if inp == "done":break
    value = float(inp)
    total += value
    count += 1
average = total/count
print("Average:",average)


#este loop tiene todos los numeros en memoria mientras calcula
#con numeros grandes requiere mas memoria
#escala en base a los numeros que tiene la lista
numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":break
    value = float(inp)
    numlist.append(value)
average = sum(numlist)/len(numlist)
print("Average",average)
