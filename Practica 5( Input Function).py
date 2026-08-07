#Module 2: Input & Type Casting
#Topic 1: input() .
name = input("Enter your name : ")
print("My name is ",name)
city = input ("enter tour city")
print (city)
city=input ("enter your city")
print ("my city is ",city)

#Important Rule.
#input() hamesha String (str) return karta hai.
#Chahe user number hi kyu na likhe.
#Example:-
 age = input ("Enter age: ")
 print(type(age))

#📚 Topic 2: Type Casting
#Type Casting ka matlab hai:
#Ek data type ko doosre data type me convert karna.
#example:-
#(strint->integer)
#Short Form (Industry Standard)
age = int(input("Enter your age: "))

# Float Input
Salary = float (input("enter your salary: "))
print(Salary)
print(type(Salary))

#💼 Data Analytics Example
#Maan lo HR Department employee ki details enter kar raha hai.
name = input ("enter employee name: ")
age = int(input("enter employee age: "))
salary = float(input("enter employee salary: "))
print (name)
print (age)
print (salary)
