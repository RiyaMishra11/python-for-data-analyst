# Strings:-
# string me sub stor kr shakteb hai number or charectors bhi.
# String ek text/data hota hai jo quotes ke andar likha jata hai.

# Example:-
# name = "Prashant"
# city = "Rajkot"
# course = "Btech"

# "Prashant"  --> String
# "Rajkot" --> String
# "Btech" --> String
# Python me hum single quotes ' ' ya double quotes " " dono use kar sakte hain.

#2. String ko print karna:-
name = "riya"
print(name)


# 3. String ko variable ke saath use karna
nmae = "srishti"
city = "maskanwa"
print (name)
print (city)


# 4. String Concatenation:-
# Concatenation ka matlab hai do ya zyada strings ko join karna.
# Python me + se strings join kar sakte hain.
first_name = "Tushar"
last_name = "Tiwari"
full_name = first_name +" " + last_name
print(full_name)


# 5. String Length — len():-
# Kisi string me kitn  characters hain, ye jaanne ke liye:(len()use karte hai):-
name = "gudiya_tiwari"
print(len(name))


# 6. String Indexing:-
#  Python string ke har character ko ek index number deta hai.
# Python me indexing 0 se start hoti hai, 1 se nahi.
name = "Maskanwa"
print(name[0])
print(name[3])


# 7. Negative Indexing:-
# Python me hum end se bhi characters access kar sakte hain.
name = "gonda"
print([-1])
print([-2])
print([-3])


# 8. String Slicing:-
# Slicing ka matlab hai string ka ek part nikalna.
name = "maskanwa"
print(name[0:2])
name = "riya mishra"
print (name[0:4])


# 9. Useful String Methods:-

# upper():-
# String ko uppercase me convert karta hai.
name = "prashant"
print(name.upper())


# lower():-
# String ko lowercase me convert karta hai.
name ="ARADHNA"
print (name.lower())



# title():-
# Har word ka first letter capital karta hai.
name = "anjali tiwari"
print(name.title())


# 10. strip():-
# Extra spaces remove karne ke liye bahut useful hai.
name = "  riya mishra   "
print(name.strip())


# 11. replace():-
# Ek text ko doosre text se replace karne ke liye:
city = "Delhi"
new_city = city.replace("Delhi","Noida")
print(new_city)


# 12. count():-
# Kisi character/word ki frequency count karne ke liye:
text = "banana"
print(text.count("a"))
# Ye concept later text/data analysis me useful hoga.


# 13. find():-
# String me kisi word/character ki position find karne ke liye:
text = "python"
print(text.find("t"))


# 💼 Real Data Analytics Example:-
# question:- Suppose dataset me city values hain:
city = "    noida    "
# Data clean karna

city = city.strip()
city = city. title()
print(city)
# ye simple example hai, lekin data cleaning me isi type ke operations bahut frequently use hote hain.


# 💻 Practice:-
# Part 1:-
name = " prashant mishra "
print(name)
print(len(name))

print(name.upper())
print(name.lower())
print(name.title())

print(name[0])
print(name[-1])


# Part 2:-
city = "    surat  "
print(city)
print(city.strip())
print(city.strip().title())


# Part:-
text = "I am learning Python"
print (text.count("Python"))
print(text.find("Python"))


# Challenge Question:-

# Name ko uppercase me print karo.
name = "riya mishra"
city = input("Noida ")
print("Name:", name.upper())

# City ko lowercase me print karo.
print("City:", city.lower())

# Name ki length print karo.
print("Name Length:", len(name))

# Name ka first character print karo.
print("First Character:", name[0])

# Name ka last character print karo.
print("Last Character:", name[-1])

# City ke extra spaces remove karo.
print("Clean City:", city.strip().title())
