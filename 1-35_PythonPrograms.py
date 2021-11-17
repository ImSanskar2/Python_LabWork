#1.Display float number with 2 decimal places using print()
val = float(input("Enter Any Number:"))
format_float = "{:.2f}".format(val)
print(format_float)

#2.Takes two integer numbers and  return their product.
val1=5
val2=2
def prod(x,y):
  return x*y
print(prod(val1,val2))

#3.Write a Python program to get the volume of a sphere with radius 10.
pi = 3.14159265358
r= 10
V= 4.0/3.0*pi* r**3
print('The Volume Of The Sphere Is:',V)

#4.Accept two numbers from the user and multiply them together.
val1=int(input("Enter Number: "))
val2=int(input("Enter Number: "))
def prod(x,y):
  return x*y
print(prod(val1,val2))

#5.Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.
a=int(input("Enter Any Integer Number:"))
print(a+(a*a)+(a*a*a))

#6.Write a Python program to calculate the length of a string
string="Sanskar Bandi"
print(len(string))

#7.Write a Python program to parse a string to Float & Integer
a = "800"
b = int(a)
c = float(a)
print(type(b))
print(b)
print(type(c))
print(c)

#8.Given two integer numbers return their sum. If the sum is greater than 100, then return their product.
val1=6
val2=87
def prod(x,y):
  return x*y
def sum(x,y):
  return x+y
sum=sum(val1,val2)
if(sum>100):
  print("Product:",prod(val1,val2))
else:
  print("Sum:",sum)
  
#9.Write a Python program to calculate the sum of three given numbers, if the values are not - equal then return four times of their sum
a=6
b=3
c=6

def sum(x,y,z):
  return x+y+z
sum=sum(a,b,c)
if(a==b and a==c):
  print("Sum:",sum)
else:
  print("Sum:",sum*4)

#10.A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("Enter Quantity Of Item:"))
price=quantity*100
if(price>10000):
  print("Total Price Is:",(price/100)*50)
else:
  print("Total Price Is:",price)
 
#11.To check whether a number is divisible by 8 and 12 or not.
a=int(input("Enter Any Number:"))
if(a%8==0 and a%12==0):
  print("{0} Number Is Divisible By 8 And 12".format(a))
else:
  print("{0} Number Is Not Divisible By 8 And 12".format(a))

#12.To check whether a given number is even or odd.
num = int(input("Enter A Number To Check Even Or Odd:- "))
if (num % 2) == 0:
   print("{0} Is Even Number".format(num))
else:
   print("{0} Is Odd Number".format(num))

'''13.Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F'''

phy=int(input("Enter physics marks :"))
chem=int(input("Enter chemistry marks :")) 
bio=int(input("Enter biology marks :"))
math=int(input("Enter marhematics marks :"))
comp=int(input("Enter computer marks :"))
per = (phy + chem + bio + math + comp) / 5.0
print("Percentage=", per)

if(per >= 90):
  print("Grade A");
elif(per >= 80):
  print("Grade B");
elif(per >= 70):
  print("Grade C");
elif(per >= 60):
  print("Grade D");
elif(per >= 40):
  print("Grade E");
else:
  print("Grade F")

#14.Take input of age of 3 people by user and determine oldest and youngest among them.
person1 = int(input("Enter age of person 1:"))
person2 = int(input("Enter age of person 2:"))
person3 = int(input("Enter age of person 3:"))

if person1 > person2 and person1 > person3:
    print("Person 1 is oldest")
elif person2 > person1 and person2 > person3:
    print("Person 2 is oldest")
elif person3 > person1 and person3 > person2:
    print("Person 3 is oldest")

if person1 < person2 and person1 < person3:
    print("Person 1 is youngest")
elif person2 < person1 and person2 < person3:
    print("Person 2 is youngest")
elif person3 < person1 and person3 < person2:
    print("Person 3 is youngest")
    
'''15.Write a program to input electricity unit charges and calculate total electricity bill according to the given condition:
For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill'''
unit = int(input("Enter units of electricity:"))
if(unit<=50):
  bill=unit*0.50
  totalbill=bill+(bill/100)*20
  print("Electricity bill is: ",totalbill)
elif(unit<=150):
  bill=unit*0.75
  totalbill=bill+(bill/100)*20
  print("Electricity bill is:",totalbill)
elif(unit<=250):
  bill=unit*1.20
  totalbill=bill+(bill/100)*20
  print("Electricity bill is:",totalbill)
elif(unit>250):
  bill=unit*1.50
  totalbill=bill+(bill/100)*20
  print("Electricity bill is:",totalbill)
  
#16. A student will not be allowed to sit in exam if his/her attendence is less than 80%.
#Take following input from user
#Total Number of classes held
#Total Number of classes attended. And print percentage of class attended. Is student is allowed to sit in exam or not.
a=int(input("Number of classes held:"))
b=int(input("Number of classes attended:"))
percentage=b/a*100
if percentage>=80:
        print("The student is allowed to sit in the exam hall")
else:
        print("The student is not allowed to sit in the exam hall")
    
#17. Calculate income tax for the given income by adhering to the below rules
# Taxable Income        Rate (in %)
# First Rs.10,0000         0
# Next Rs. 10,0000       10
# The remaining           20
income=int(input("Enter income:"))
if (income <= 100000):
  tax = 0
elif (income <= 200000):
  tax = (income*10)/100
else :
  tax = (income *20)/100
print("You owe", tax, "Rupees in tax!")

#18. Program to find digital sum of a given Number
#    ex: n=123  Digital sum----->1+2+3=6
def getsum(n):
  sum=0
  num = str(n)
  for i in num:
    sum = sum + int(i)
  return sum
  
n=int(input("Enter the number:"))
print(getsum(n))

#19. Program to find the digital product of a given number
#    ex: n=43   Digital product ----->4*3=12
def getProduct(n):
  product = 1
  num = str(n)
  for i in num:
    product = product * int(i)
  return product
  
n=int(input("Enter the number:"))
print(getProduct(n))

# 20.Find the sum of the series 3 +33 + 333 + 3333 + .. n terms
n=int(input("Enter the range of number:"))
sum=0
p=3
for i in range(1,n+1):
    sum += p
    p=(p*10)+3
print("The sum of the series=",sum)

#21.Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
    
 #22. Program to reverse a given Number.    ex: n=123   Reversed no is 321
n = 3241
rev = 0
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10
print(rev)

#23.Program to check whether a given number is a palindrome or not
def reverseDigits(num) :
	rev_num = 0;
	while (num > 0) :
		rev_num = rev_num * 10 + num % 10
		num = num // 10	
	return rev_num
def isPalindrome(n) :
	rev_n = reverseDigits(n);
	if (rev_n == n) :
		return 1
	else :
		return 0
n = 121	
if isPalindrome(n) == 1 :
  print("Is", n, "a Palindrome number? ->", True)
		
else :
  print("Is", n, "a Palindrome number? ->", False)
  
#24.Program to check whether a given number is an Armstrong number or not.
num = int(input("Enter a number:"))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
    
#25.Program to find factorial of a given number.
fact=1
n=5
while(n!=0):
    fact=fact*n
    n=n-1

print("fact",fact)

#26)Program to find whether a given number is a strong number or not.
 # e.g. n=145
 # 1!+4!+5!==145
def factorial(d):
   if(d==1 or d==0):
      return 1
   return d*factorial(d-1)
def isStrong(n):
   num=n
   sm=0
   while(n>0):
      digit=n%10
      sm=sm+factorial(digit)
      n=n//10
   if(sm==num):
      return True
   else:
      return False
print("Input a number")
a=int(input())
print(isStrong(a))

#27. Program to find whether a given number is a unique number. For example, 20, 56, 9863, 145, etc. are the unique numbers
#while 33, 121, 900, 1010, etc. are not unique numbers
visited = [0,0,0,0,0,0,0,0,0,0];
num=20
while (num):
  if visited[num % 10] == 1:
    break;
  visited[num % 10] = 1;
  num = (int)(num / 10);

if num == 0:
  print("Number is unique");
else:
  
  #28)Program to find whether a given number is a perfect number or not.
def perfect_number(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n
print(perfect_number(6))

#29)Program to find whether a given number is a prime number or not.
num = 11
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
  
else:
    print(num, "is not a prime number")
    
'''30)Print downward Half-Pyramid Pattern with Star(asterisk)
* * * * *  
* * * *  
* * *  
* *  
*'''
rows = 5 
for i in range(rows + 1, 0, -1):    
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")
    
# 31)Print  following pattern: 
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999
for i in range(10):
    print(str(i) * i)
    
'''32)Print  following pattern: 
1
12
123
1234
12345
123456
1234567
12345678
123456789'''
for i in range(1,9+1):
    for j in range(1, i+1):
        print(j, end="")
    print()
    
'''33)Print following pattern: 
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH'''
    
#34)Write a Python program to calculate the length of a given string.
str = "Sanskar"
print(len(str))

#35.Write a Python program to get a single string from two given strings, separated by a space and swap the first characters of each string.
#Sample String : 'abc', 'xyz' 
#Expected Result : 'xbc ayz'
str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")
 
x=str1[0:1]
 
str1=str1.replace(str1[0:1],str2[0:1])
 
str2=str2.replace(str2[0:1],x)
 
print("Your first string has become:",str1)
print("Your second string has become:",str2)
