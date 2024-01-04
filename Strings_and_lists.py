#to split a string 
#.split breaks a string into parts and produces a lists of strings
abc="Whit three words"
stuff=abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

#para acceder a cada uno de los elementos en la lista
for i in stuff:
    print(i)

line = "A lot                      of spaces"
etc = line.split()
print(etc)

#split(). cuando no hay nada en parentesis divide por espacios en los string
line = "First;Second;third"
thing = line.split()
print(thing)
print(len(thing))

#split() divide dependiendo lo que tenga en los parentesis
thing = line.split(";")
print(thing)
print(len(thing))


#From sthephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("From "):continue
    words = line.split()
    print(words[2])

line = "From sthepen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008"
words = line.split()
print(words)

#The double split pattern
#From sthepen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008
words = line.split()
email = words[1]
print(email)
pieces = email.split("@")
print(pieces)