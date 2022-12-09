#VARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLES
# 1.variables
a = "12"
b = 13
c = 14.0
print(a)
print(b)
print(c)

# 2.casting
d = int(5)
e = float(5.0)
f = str("5")
print(d/2)
print(e/2)
print(int(f)/2)    #casting string to int to be divided

# 3.casting
g =int(5)
h =int(8.0)
i =int("7")
print(g)
print(h)  #without 0 because int
print(i)  #without brackets because int

# 4. strings
hello = "Hello, world!"
print(hello)
print(len(hello))
print(hello[0])
#Assign last 5 characters of the string to the new variable and print.
helloNew = hello[8:]
print(helloNew)

print(hello.upper())
print(hello.count("o"))
#Split string into two separate words and print each separately
helloDivided = hello.split()
print(helloDivided[0])
print(helloDivided[1])

# 5.
name = "John"
age = "30"
text = "Hello, my name is {}, I'm {}"
print(text.format(name,age))


#OPERATORSOPERATORSOPERATORSOPERATORSOPERATORSOPERATORSOPERATORSOPERATORSOPERATORSOPERATORSOPERATORS
# 1.
x = 5
y = 7
x = x+y
print(x)

# 2.
ten = 10
tenS = "10"
tenO = ten/0
tenOO = tenS/0
print(tenO)    #ZeroDivisionError: division by zero - division is prohibited
print(tenOO)   #TypeError: unsupported operand type(s) for /: 'str' and 'int' - different types

# 3.


# 4.
x1 = 5
x1 += 3
print(x)

# 5.


#CONDITIONALSCONDITIONALSCONDITIONALSCONDITIONALSCONDITIONALSCONDITIONALSCONDITIONALSCONDITIONALS
# 1.
int1 = 44
int2 = 33
if int1>int2:
    print("Yes this is True")

# 2.
x2 = 551
y2 = 55
if x2>y2:
    print("x is bigger than y")
elif x2==y2:
    print("x and y are equal")
elif x2<y2:
    print("y is bigger than x")

# 3.
world = "The world is mine"
if "mine" in world:
    print("Yes this is True")

#COLLECTIONSCOLLECTIONSCOLLECTIONSCOLLECTIONSCOLLECTIONSCOLLECTIONSCOLLECTIONSCOLLECTIONSCOLLECTIONS
# 1.
difList = ["string", 5, 10.5, False, True]
print(difList)
print(difList[1:-1])
print(len(difList))

difList.append("added")
print(difList)

difList.insert(1,123)
print(difList)

difList[2] = "changed"
print(difList)

difList[2:4] = ["inserted"]
print(difList)

difList.remove("inserted")
print(difList)

difList.pop(2)
print(difList)

# 2.
firstList = ["first", 2, 12.23]
secondList = [False, True]

firstList.append(secondList)  #second list was inserted  into first like separate list
print(firstList)

firstList.extend(secondList)  #second list was added to the end like another elements
print(firstList)
