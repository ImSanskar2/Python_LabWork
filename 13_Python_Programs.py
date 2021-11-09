#Q.1)Display float no with 2 decimal places using print()
val = float(input("Enter Any Number: "))
format_float = "{:.2f}".format(val)
print(format_float)
Enter any number: 7.8
7.80

#Q.2)Takes 2 integer nos and return their product.
val1=2
val2=4
def prod(x,y):
  return x*y
print(prod(val1,val2))
8

#Q.3)Write a Python program to get the volume of a sphere with radius 10.
pi = 3.1415
r= 10
V= 4.0/3.0*pi* r**3
print('The Volume Of The Sphere Is:-',V)
The Volume Of The Sphere Is:-  4188.66667
  
#Q.4)Accept two nos from the user and multiply them.
val1=int(input("Enter No.:- "))
val2=int(input("Enter No.:- "))
def prod(x,y):
  return x*y
print(prod(val1,val2))
Enter No.:- 4
Enter No.:- 9
36

#Q.5)Write a Python program that accepts an integer (a) and computes the value of a+aa+aaa.
a=int(input("Enter Any Integer No.:-"))
print(a+(a*a)+(a*a*a))
Enter Any Integer No.:-5
155

#Q.6)Write a Python program to calculate the length of a string
string="Sanskar Bandi"
print(len(string))
13

#Q.7)Write a Python program to parse a string to Float & Integer
a = "1200"
b = int(a)
c = float(a)

print(type(b))
print(b)

print(type(c))
print(c)
<class 'int'>
1200
<class 'float'>
1200.0

#Q.8)Given 2 integer nos return their sum. If the sum is greater than 100, then return their product.
val1=14
val2=99
def prod(x,y):
  return x*y
def sum(x,y):
  return x+y
sum=sum(val1,val2)
if(sum>100):
  print("Product:-",prod(val1,val2))
else:
  print("Sum:-",sum)
  Sum:-113
    
#Q.9)Write a Python program to calculate the sum of 3 given nos, if the values are not - equal then return 4 times of their sum
a=10
b=6
c=8

def sum(x,y,z):
  return x+y+z
sum=sum(a,b,c)
if(a==b and a==c):
  print("Sum:-",sum)
else:
  print("Sum:-",sum*4)
  sum : 96
    
#Q.10)A shop will give discount of 50% if the cost of purchased quantity is more than 10000. Ask user for quantity suppose, one unit will cost 100. Judge and print total cost for user.
quantity=int(input("Enter Quan. Of Item:"))
price=quantity*100
if(price>10000):
  print("Total Price Is :-",(price/100)*50)
else:
 print("Total Price Is :-",price)   
  Enter Quan. Of Item:110
Total Price Is:-5500.0
  
#Q.11)To check whether a no is divisible by 8 and 12 or not.
a=int(input("Enter Any No.:-"))
if(a%8==0 and a%12==0):
  print("{0} Number Is Divisible By 8 And 12".format(a))
else:
  print("{0} Number Is Not Divisible By 8 And 12".format(a)) 
  Enter Any No.:-36
36 Number Is Not Divisible By 8 And 12  


#Q.12)To check whether a given no is even or odd.
num = int(input("Enter A Number To Check Even Or Odd:- "))
if (num % 2) == 0:
   print("{0} Is Even Number".format(num))
else:
   print("{0} Is Odd Number".format(num))
Enter a number to check even or odd:- 56
56 is Even Number


#13.Write a program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer. Calculate percentage and grade according to following:
Percentage >= 90% : Grade A
Percentage >= 80% : Grade B
Percentage >= 70% : Grade C
Percentage >= 60% : Grade D
Percentage >= 40% : Grade E
Percentage < 40% :  Grade F'''
phy=int(input("enter physics marks :"))
chem=int(input("enter chemistry marks :")) 
bio=int(input("enter biology marks :"))
math=int(input("enter marhematics marks :"))
comp=int(input("enter computer marks :"))
per = (phy + chem + bio + math + comp) / 5.0
print("Percentage = ", per)
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
  enter physics marks :60
enter chemistry marks :30
enter biology marks :25
enter marhematics marks :54
enter computer marks :64
Percentage =  46.6
Grade E
