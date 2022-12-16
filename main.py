
#VARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLESVARIABLES
# 1.variables
a = "12"
b = 13
c = 14.0
print(a is b) #false because is not equal
print(b is c) #false because is not equal
print(b is c) #false because is not equal

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
j = int(5)
k = float(5.0)
l = str("5")
print(j>k) #False because j==k
print(j>l) #TypeError: '>' not supported between instances of 'int' and 'str'
print(j<k) #False because j==k
print(j==k) #True because j==k
print(j==l) #False because float != string
print(k==l) #False because float != int
print(j!=k) #False because j==k
print(j!=l) #True because int != string
print(k!=l) #False because string != int

# 4.
x1 = 5
x1 += 3
print(x)

# 5.
onion = "Onion"
tomato = "Tomato"
print(onion>tomato) #quantity of the symbols is bigger in "tomato", so False
print(onion<tomato) #quantity of the symbols is bigger in "tomato", so True
print(onion==tomato) #quantity of the symbols is bigger in "tomato", so false
print(onion!=tomato) #quantity of the symbols is bigger in "tomato", so false
vegetables = onion+tomato
print(vegetables)

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
# 1. List
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

# 2. List
firstList = ["first", 2, 12.23]
secondList = [False, True]

firstList.append(secondList)  #second list was inserted  into first like separate list
print(firstList)

firstList.extend(secondList)  #second list was added to the end like another elements
print(firstList)

# 3. Dictionary
diction = {
    "name":"John",
    "surename":"Deere",
    "age": 25
}
print(diction["name"],diction["age"])
print(diction.keys())
print(diction.values())

diction["age"] = 33
print(diction.values())

diction["maritalStatus"] = "married"
print(diction["name"], diction["maritalStatus"])

diction["children"] = ["Paul", "Jack", "Freddie"]
print(diction["name"], diction["children"])

del diction["age"]  # 1st method

diction.pop("age")  # 2nd method
print(diction)

# 4. Tuples
tuple = ("first","second", "third", 1, 2, 3, True, False, 10.1, 11.2, 12.3)
print(tuple)
print(tuple[-4:])
print(tuple.index("third"))

anotherTuple = ("next", "super", "best")
print(tuple+anotherTuple)

(one, two, three, *four) = tuple
print(one)
print(two)
print(three)
print(four)

#LOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPSLOOPS
# 1.
loopList = ["orange", "apple", "banana", "cherry"]
for x in loopList:
    print(x)

for x in loopList:
    if x=="apple":
        print(x)

for x in loopList:
    print(x)
    print(len(x))

# 2.
for x in range(2,100):
    print(x)

# 3.
m = 0
while m < 16:
    print(m)
    m = m+1

# 4.
n = 3
while n < 34:
    print(n)
    n = n+1

# 5.
loopListList = ["orange", "apple", "banana", "cherry"]
def litPrint():
    for x in loopListList:
        print(x)
        if x=="banana":
            break
litPrint()

def litPrint2():
    for x in loopListList:
        if x!="banana":
            print(x)

litPrint2()


#FUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONSFUNCTIONS
# 1.
def privet():
    print("Hello, world")
privet()

# 2.
def nameSurname(name,surname):
    text1 ="Hello, my name is {} {}"
    print(text1.format(name, surname))

nameSurname("Peter", "Jackson")

nameSurname(surname="Peterson", name="Jack")

# 3.
def models(*models):
    print("The first car models is",models[0])

models(1,2,3,4,5,6,7,8,9)

# 4.
def person(**personal):
    print(personal["age"],personal["name"])

person(surname="Doe", age=45, cat=True, name="John")

# 5.
def print_person_info(name, surname, maritalStatus="unknown",*age):
        print(name,surname,age,maritalStatus)

print_person_info("Bob","Dylan","married",55)


# 6.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial(6)


#LAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDALAMBDA
# 1.
l_list = [1,2,3,4,5]
o=6
multi_list = list(map(lambda n:n*o, l_list))
print(multi_list)

# 2.
odd_list =list(map(lambda p:p%2==0,l_list))
print(odd_list)

# 3.
import datetime
today = datetime.datetime.today()
year = lambda x : x.year
month = lambda y : y.month
day = lambda z: z.day

print(year(today))
print(month(today))
print(day(today))


# 4.
double_list =list(map(lambda x: x*2,l_list))
print(double_list)



#COMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSIONCOMPREHENSION

# 1.
numbers_list = [1, -2.0, 3, -4.34, 5]
negative_list = [int(x) for x in numbers_list if x<0]

print(negative_list)

# 2.
string_list = ["string", "mediumstring", 'longstring', "hugestring"]
lenght_list = [x for x in string_list if len(x) == 10]

print(lenght_list)

# 3.
thirteen_list = [3, 26, 34, 39, 56]
divisible_list = [x for x in thirteen_list if x%13==0]

print(divisible_list)

# 4.
name_list = ["Jack", "john", "Paul", "sean"]


