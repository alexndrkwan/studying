print("Hello World")
name = input("What's your name ") #storing name into variable 'name'
print("Hello " + name + "!")
print(2.234 + 4) #numbers no quotations, % is remainder also called mod 3 % 4 3 cant go into 4 so left w 3, numers can alo be stored as variables
print(str(5) + " my favorite number") #use str function to combine strings together
#use abs to create absolute number , pow will power it so pow(3, 2) 3 to the power of 2
#sqrt square root of anumber, also floor is the lower number, ceil is the higher number, max/min higher of two number or lower
#round funct to round a number 3.2 to 3
#in python import external code from math import * // to access floor/ceil
store_name = input("Enter Your name: ")
phrase = "Giraffe Academy"
print(phrase.replace("Giraffe","Elephant")) #places giraffe
print(phrase.upper().isupper()) #multiple .
friends = ["joe", "mom"]
friends.insert(1, "kelly")
friends.append("crazyy")
print(friends)
print(friends.index("kelly"))
friends.sort()
#you can also copy list, or reverse list etc instead of just sort
coordinates = (4,5)

#immutable = tuples cant be changed or modified, no elements etc
def sayhi(name): #want parameters to pass into the function make it more official, give info into ( )
    print("Hello " + name)

print("Top")
sayhi("Steve") #calling the function right here inside paramter is steve so steve is placed instead of name
print("Bottom") #goes in order top to down name lower case for function and two or more words use _

def cube(num: object) -> object:
    return num*num*num #howev need return statement in order to pass info through it, returns whatever value in right
    #give value back whatever called this function when it reads return

result = cube(3) #return will also break the function

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3

print (max_num(3, 4, 5))

monthConversions = {
    "jan" : "January",
    "feb": "February",
    "mar": "March",
    "apr": "April",
    "may": "May",
} #dictionary use curly
usermonth = input("What month? ")
usermonth=usermonth.lower()
print(monthConversions.get(usermonth)) #use .get or use []
i = 1
while i <=10: #as long as this true while keep looping with this condition
    print(i)
    i += 1 #i = i + 1 shorthand, goes gack and checks condition

print("done with loop")

friends = ["Jim", "karen", "kevin"]
for index in friends:

    def translate(phrase):
        translation = ""
        for letter in phrase:
            if letter in "AEIOUaeiou":
                translation = translation + "g"
            else:
                translation = translation + letter
        return translation
print(translate(input("enter a phrase")))
try: #use try when there are options that are wrong, protect program.
    number = int(input("Enter a number: "))
    print(number) #break program if it isnt number in real world problem not good
except ZeroDivisionError as err: #this might catch anything wrong in the program so this is helpful. so maybe value = 10/0 will maybe break program...
    print(err)# so this will help it print out invalid instead of breaking program
except ValueError:
    print("invalid input")
#employees.txt he inserts a file into python read the employees inside of file... open file inside python
#special command open() abs path to file or relative or just name  employees.txt are in same directory so can do "employees.txt", "r" diff modes
#r is just to read the files and not nmodify it at all , w = write to change file... a = append, add new info not change tho
#r + = read and write power of reading and writing...
#.readline function .readlines puts them in a list
#module is external to be imported into python , goog list of python modules with correct version
#huge list of python modules that access within python already written in python

#classes sometimes we ccant define some things in a name
class Student:
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
