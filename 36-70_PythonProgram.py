#36. Write a Python program to add 'polis' at the end of a given string (length should be at least 3).
#  If the given string already ends with 'polis' then add 'polisCS' instead.
#  If the string length of the given string is less than 3, leave it unchanged. 
#  Sample String : 'abc'
#  Expected Result : 'abcpolisCS' 
#  Sample String : 'Acropolis'
#  Expected Result : 'AcropolisCS'
def add_string(str1):
  length = len(str1)
  if length > 2:
    if str1[-5:] == 'polis':
      str1 += 'CSIT'
    else:
      str1 += 'polis'
  return str1
print(add_string('xy'))
print(add_string('xyz'))
print(add_string('Acropolis'))

#37)Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
#Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('Google.com'))

#38. Write a Python program to change a given string to a new string where the second and last chars have been exchanged.
def change_sring(str1):
      return str1[0:1]+str1[-1:] + str1[2:-1] + str1[1:2]
	  
print(change_sring('wxyz'))
print(change_sring('56789'))

#39)Write a Python program to remove the characters which have even index values of a given string.
def even_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2!= 0:
      result = result + str[i]
  return result

print(even_values_string('uvwxyz'))
print(even_values_string('Python'))

#40 .Write a Python program that takes input from the user and displays that input back in upper and lower cases.
str1=input("Enter string:")
print("In Upper:" ,str1.upper())
print("In Lower:" ,str1.lower())

#41)Write a Python program to count occurrences of a substring in a string.
str1 = 'School College School'
print()
print(str1.count("School"))
print()

#42)Write a Python program to lowercase first n characters in a string.
str1 = 'SANSKAR'
print(str1[:4].lower() + str1[4:])

#43)Write a Python program to remove spaces from a given string.
def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
    
print(remove_spaces("A C R O P O L I S"))
print(remove_spaces("S A N S K A R"))

#44)Write a Python program to move spaces to the front of a given string.
def move_Spaces_front(str1):
  noSpaces_char = [ch for ch in str1 if ch!=' ']
  spaces_char = len(str1) - len(noSpaces_char)
  result = ' '*spaces_char
  result = '"'+result + ''.join(noSpaces_char)+'"'
  return(result)

print(move_Spaces_front("Acropolis College:"))
print(move_Spaces_front("CSIT Branch:"))

#45)Write a Python program to find the maximum occurring character in a given string.
def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
 
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch
print(get_max_occuring_char("Acropolis"))
print(get_max_occuring_char("Sanskar"))

#46)Write a Python program to capitalize first and last letters of each word of a given string.
def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  
     
print(capitalize_first_last_letters("acropolis"))
print(capitalize_first_last_letters("sanskar"))

#47)Write a Python program to compute sum of digits of a given string.
def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit
     
print(sum_digits_string("AcropolisCI"))
print(sum_digits_string("CSIT51"))

#48)Write a Python function that takes a list of words and returns the length of the longest one.
def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["CS", "ACROPOLIS", "CSIT"])
print("\nLongest word:",result[1])
print("Length of the longest word:",result[0])

#49.Write a function x(n) for computing an element in the sequence xn=n^2+1. Call the function for n=4 and write out the result.
def x(n):
  return(n**2 + 1)
print(x(4))

#50. Take the following Python code that stores a string: ‘str = 'Y-tatata-acropolis: 0.8475'. Use find and string slicing to extract the portion 
#of the string after the colon character and then use the float function to convert the extracted string into a floating point number.
string = 'Y-tatata-acropolis: 0.8475'
col_pos = string.find(':')                  # Finds the colon character
number = string[col_pos + 1:]                 # Extracts portion after colon
confidence = float(number)                  # Converts to floating point number
print(confidence)

#51. Write a function that returns the middle value among three integers. (Hint: make use of min() and max()). Write code to test this function with different inputs.

def middleOfThree(a, b, c) :
	if a > b :
		if (b > c):
			return b
		elif (a > c) :
			return c
		else :
			return a
	else:
		if (a > c) :
			return a
		elif (b > c) :
			return c
		else :
			return b
a = 46
b = 24
c = 90
print( middleOfThree(a, b, c) )

#52.Write a function that computes the area of a rectangle. Then, write a second function that calls this function three times to compute the surface area of a rectangular solid.
def secondfun():
  for i in range(3):
    print(area(i+1,i+3))

def area(h,w):
  area=h*w
  return area
height=4
width=6
print(area(height,width))
secondfun()

#53.Create an outer function that will accept three parameters, a, b and c. Create an inner function inside an outer function that will calculate the
#addition of a, b and c. At last, an outer function will add 5 into addition and return it 
def num1(x,y,z):
  def num2(a,b,c):
    return a+b+c
  outer=num2(x,y,z)+5
  return outer
print(num1(5,4,5))

#54.Write a program to create a recursive function to calculate the product of numbers from 10 to 100.
def recur(n):
   if n == 10:
       return n
   else:
       return n*recur(n-1)
print("The product of numbers from 10 to 100 is:", recur(100))

#55.Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number:"))
print(factorial(n))

#56.Write a Python function to display all the multiples of  7 & 9 within the range 100 to 500.
nl=[]
for x in range(100, 501):
    if (x%7==0) and (x%9==0):
        nl.append(str(x))
print (','.join(nl))

#57.Write a Python function  to check whether the given integer is a prime number or not.
num = 27
flag = False
def prime(n):
  flag1=False
  if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag1 = True
            break
  return flag1
flag=prime(num)
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
    
#58. Write a Python function that checks whether a passed interger is armstrong or not.
n = int(input("Enter a number: "))
def armstrong(num):
  sum = 0
  temp = num
  while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
  return sum
summ=armstrong(n)
if n == summ:
   print(n,"is an Armstrong number")
else:
   print(n,"is not an Armstrong number")
    
#59. Program to return a function from another function.
def B():
	print("Inside the method B.")
def A():
	print("Inside the method A.")
	return B
returned_function = A()
returned_function()

#60. First, def a function, start_process, that takes one argument p. Then, if the start_process function receives an p equal to "Yes",
# it should return "Start Process" Alternatively, elif p is equal to "No", then the function should return "Start Process Aborted".
#  Finally, if start_process gets anything other than those inputs, the function should return "Sorry for the input".

def start_process(p):
  if p=="Yes":
    return "Start Process"
  elif p=="No":
    return "Start Process Aborted"
  else:
    return "Sorry for the input"
command= input("Enter a command:")
print(start_process(command))

#61. First, def a function called calculate_distance, with one argument (choose any argument name you like).
#   If the type of the argument is either int or float, the function should return the absolute value of the function input.
#   Otherwise, the function should return "No value". Check if it works calling the function with  9.6 and "what?".

def calculate_distance(argument):
  if type(argument) == int or type(argument) == float:
      return abs(argument)
  else:
      print("No value")
print("The absolute value:" ,calculate_distance(33.20))
calculate_distance("What?")

#62.Python program to display the sum of input (n) numbers using a list.

list1 = [61, 4, 91, 23, 67]
total=0
for i in range(0, len(list1)):
    total = total + list1[i]
print("Sum of all elements in given list:", total)

#63)Python program to insert a number to given position in a list.
print("Enter 10 Elements of List:")
nums = []
for i in range(10):
    nums.insert(i, input())
print("Enter an Element to Insert at End:")
elem = input()
nums.append(elem)
print("\nThe New List is:")
print(nums)

#64. Write the program that prompts the user for a list of numbers and prints out the maximum and minimum of the 
# numbers at the end when the user enters “done”. Write the program to store the numbers the user enters in a list and 
# use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.

my_list = []                     
while True:
    number = 0.0
    input_number = input('Enter a number:')
    if input_number == 'Done':
        break
    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()
    my_list.append(number)
if my_list:
    print('Maximum:', max(my_list) or None)
    print('Minimum:', min(my_list) or None)
    
#65.Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers.
my_list = []                     
while True:
    number = 0.0
    input_number = input('Enter a number: ')
    if input_number == 'Done':
        break
    try:
        number = float(input_number)
    except ValueError:
        print('Invalid input')
        quit()
    my_list.append(number)
if my_list:
    print('Maximum:', max(my_list) or None)
    print('Minimum:', min(my_list) or None)
    
#66.Python program to delete an element from a list by index which is given by the user.
print("Enter 10 Elements:")
arr = []
for i in range(10):
    arr.append(input())
print("\nEnter the Value to Delete:")
val = input()
arr.remove(val)
print(arr)

#67)Write a Python program to print a specified list after removing the 1st, 2nd and 5th elements.
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (1,2,5)]
print(color)

#68)Write a Python program to generate all sublists of a list.
from itertools import combinations
def sub_lists(my_list):
	subs = []
	for i in range(0, len(my_list)+1):
	  temp = [list(x) for x in combinations(my_list, i)]
	  if len(temp)>0:
	    subs.extend(temp)
	return subs
l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print("Original list:")
print(l1)
print("S")
print(sub_lists(l1))
print("Sublists of the said list:")
print(sub_lists(l1))
print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
print(sub_lists(l2))

#69)Write a Python program to find all the values in a list are greater than a given number.
list1 = [220, 330, 500]
list2 = [12, 17, 21]
print(all(x >= 200 for x in list1))
print(all(x >= 15 for x in list2))

#70)Python program to find the even numbers in a List.
list1 = [10, 21, 4, 45, 66, 93]
for num in list1:
    if num % 2 == 0:
        print(num, end=" ")
