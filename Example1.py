### 🎯 Practice Exercise 1

#1. Create a variable `score = 85`
#2. Write an if statement that prints "Passed!" if score is >= 60
#3. Create a variable `balance = 1000`
#4. Write an if statement that prints "Sufficient funds" if balance > 500

score=85
if score>=60:
    print("Passed!")
balance =1000
if balance>500:
    print("Sufficient funds")


## 🎯 Practice Exercise 2

#1. Create a variable `password = "secret123"`
#2. Check if password equals "secret123", print "Access granted" or "Access denied"
#3. Create a variable `temperature = 10`
#4. Print "Warm" if temperature > 20, otherwise print "Cold"

password = "secret123"
if password == "secret123":
    print("Access granted")
else:
    print("Access denied")

temperature=10
if temperature>20:
    print("Warm")
else:
    print("Cold") 


### 🎯 Practice Exercise 3

#1. Create a variable `time = 14` (24-hour format)
#2. Print "Good morning" (5-12), "Good afternoon" (12-17), "Good evening" (17-21), "Good night" (21-5)
#3. Create a BMI calculator that classifies: Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), Obese (>=30)

time=14
if 5 <= time <12:
      print("Good morning")
elif 12 <= time <17:
    print("Good afternoon")
elif 17 <= time <21:
    print("Good evening")
else:
     print("Good night")

bmi=14
if bmi < 18.5:
      print("Underweight")
elif 18.5 <= bmi <24.9:
    print("Normal")
elif 25 <= bmi <29.9:
    print("Overweight")
else:
     print("Obese")


### 🎯 Practice Exercise 4

#1. Compare two numbers and print which is larger
#2. Check if a number is between 10 and 20 (inclusive)
#3. Check if two strings are equal (case-sensitive)

num1=15
num2=20
if num1 > num2:
    print("num1 is larger")
elif num2 > num1:
    print("num2 is larger")
else:
     print("Both numbers are equal")

number = 15
if 10 <= number <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is not between 10 and 20")

str1="Hello"
str2="Hello"

if str1 == str2:
    print("Strings are equal")
else:
    print("Strings are not equal")


### 🎯 Practice Exercise 5

#1. Check if a number is between 10 and 20 (inclusive) using `and`
#2. Check if a character is a vowel (a, e, i, o, u) using `or`
#3. Write a login system: correct username AND correct password
#4. Check if it's a weekend (Saturday or Sunday) AND weather is good (not raining)

num = 15
if num >= 10 and num <= 20:
    print("Number is between 10 and 20")
else:
    print("Number is not between 10 and 20")

ch='a'
if ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a' or ch == 'a':
    print("Vowel")
else:
    print("Not vowel")

uname="admin"
pwd="1234"
if uname == "admin" and pwd == "1234":
    print("Login Successfully")
else:
    print("Login Failed")

day="Saturday"
israining= False
if(day == "Saturday" or day == "Sunday") and not israining:
    print("Raining")
else:
    print("Not Raining")


### 🎯 Practice Exercise 6

#1. Check if a username is in a list of registered users
#2. Check if 'python' appears in a sentence (case-insensitive)
#3. Verify if required fields ('name', 'email', 'phone') exist in a dictionary
#4. Check if a number is NOT in a list of blocked numbers

users = ["lakshmi", "prasanna", "satram"]
uname = "prasanna"
if uname in users:
    print("User Exists")
else:
    print("User not Exists")

sentence = "I am lakshmi prasanna satram"
if "prasanna" in  sentence.lower():
    print("Found in sentence")
else:
    print("Not Found in sentence")


data = {"name": "lakshmi", "email": "laxmi_2741@yahoo.co.in", "phone": "8886144644"}

if "name" in data and "email" in data and "phone" in data:
    print(f"Required fields exist in data")
else:
    print(f"Required fields not exist in data")

blockednums = [111, 222, 333]
num=222
if num  not in blockednums :
    print(f"num is not in blocked nums")
else:
    print(f"num is in blocked nums")



#🎯 Practice Exercise 7
#1.Create two lists with same values and check with == and is
#2.Create a variable and assign it to another, check with is
#3.Check if a variable is None
#4.Demonstrate difference between == and is with strings

# Example 1: is vs ==
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2:", list1 == list2)  
print("list1 is list2:", list1 is list2) 

a=20
b=a
print("a is b:", a is b) 


value = None
if value is None:
    print("No value provided")

str1="test"
str2="test"

print("str1 == str2:", str1 == str2)  
print("str1 is str2:", str1 is str2) 

str3="".join(["te","st"])
print("str1 == str3:", str1 == str3) 
print("str1 is str3:", str1 is str3) 



#🎯 Practice Exercise 8
#Check if a list is empty without using len()
#Check if a string has content (not empty)
#Write validation: name must not be empty AND age must not be 0
#Check if a dictionary has any items



#🎯 Practice Exercise 9
#Check if a number is between 1 and 100 using chained comparison
#Check if three numbers are in ascending order
#Validate age is between 18 and 65 (inclusive) using chained comparison
#Check if temperature is in comfortable range (18-25°C)



#🎯 Practice Exercise 10
#Use ternary to assign "Positive" or "Negative" based on a number
#Find minimum of two numbers using ternary operator
#Set discount to 10% if purchase > 100, else 0%
#Convert boolean to "Yes"/"No" string using ternary



#🎯 Practice Exercise 11
#Check if number is positive, then check if it's even or odd
#Login system: check username first, then password
#Discount calculator: check if customer is VIP, then check purchase amount
#Rewrite one nested if using logical operators