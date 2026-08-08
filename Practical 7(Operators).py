#Operators in Python
#Operators Python me calculation, comparison aur decision-making ke liye use hote hain.

#1. Arithmetic Operators:-
#Arithmetic operators mathematical calculations ke liye use hote hain.
# (Addition ➕ ) , (Subtraction ➖) , (Multiplication ✖️ ) , (Division ➗ ) ,(Modulus/Remainder %) , (Floor Division // )  , (Power **)


# ➕ Addition :-
a = 20
b = 15
result = a + b
print(result)


# ➖ Subtraction :-
a = 40
b = 30
result =  a - b
print (result)


# ✖️ Multiplication :-
a = 10
b = 40
result = a * b 
print (result)


# ➗ Division 
a = 10 
b = 50
result = a / b
print (result)
# Note:- Python / ka result generally float deta hai.
# 10 / 2 = 5.0 (float matln decimal value deta hai).


#  %  Modulus/Remainder :-
#  % remainder deta hai.
result = 10 % 3
print (result)

# Data Analytics connection:- Modulus ka use kabhi-kabhi rows ko groups me divide karne, even/odd check karne aur cyclic calculations me hota hai.



# // Floor Division :-
result = 10 // 3
print (result)


# ** Power :-
result = 2 ** 3
print (result)

# matlab 2*2*2 = 8


#💼 Data Analytics Example :-

# Question :- Ek Shop me price = 500 and Quantity = 4 hai.
#  to total sales kitna ho ga ?.
# Answer :-
price = 500
quantity = 4
total_sales = price * quantity
print (total_sales)


# 2. Comparison Operators.
# Comparison operators do values ko compare karte hain.
# Aur result hamesha:- (True or False ) me dete hai.
# Comparison Operators are:- (Equal to == ) , (Not equal to !=) , (Greater than >) , (Less than <) , (Greater than or equal to >=) , (Less than or equal to <=).


# (Equal to == ):-
age = 20
print (age == 20)


# (Not equal to !=) :-
age = 35
print (age != 40)


# (Greater than >) :-
marks = 60
print (marks < 50)



# (Less than >) :-
marks = 60
print (marks > 50)


# (Greater than or equal to >= ) :-
marks = 60
print (marks >= 50)



# (Less than or equal to <= ) :-
marks = 100 
print (marks >= 50)


# 3.Logical Operators :- 
# Python me 3 main logical operators hain:
# Logical Operators are ( and , or , not ).


# and Operators me dono conditions True honi chahiye.
age = 22
salary = 40000
print (age> 18 and salary >30000)


# or Operators me Koi bhi ek condition True ho to result True. 
age = 22 
salary = 20000
print (age >18 0r salary > 30000)


# not Operators me True ko False aur False ko True kar deta hai.
is_student = True
print (not is_student)


# 💻 Practice 1 :-
# Arithmetic Operators:-
a = 20 
b = 6

print ("Addition:" , a + b)
print ("Subtraction:" , a - b)
print ("Multiplication:" , a * b)
print ("Division:" , a / b)
print ("Modules:" , a % b)
print ("Floor Division:" , a // b)
print ("Power:" , a**2)


# 💻 Practice 2 :-
# Comparison Operators:-
print (age == 22)
print (age != 22)
print (age > 18 )
print (age < 19 )
print (age >= 22 )
print (age <= 20 )


