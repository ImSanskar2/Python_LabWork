>>> list=[]
>>> list=[1,2,3]
>>> list1=[22,"Hello",3.6]
>>> list1
[22, 'Hello', 3.6]
>>> list1=[22,"Hello",[22,3.6]]
>>> list1
[22, 'Hello', [22, 3.6]]
>>> print(list1[-1:1])
[]
>>> list1.append(4)
>>> list1
[22, 'Hello', [22, 3.6], 5]
>>> list1.append([1,4])
>>> list1.append(4)
>>> list1
[22, 'Hello', [22, 3.6], 5, [22, 5], 5]
>>> list1[2]='r'
>>> list1
[22, 'Hello', 's', 5, [22, 5], 5]
>>> list1.append(1,2,3)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list1.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
>>> list1.extend([1,2,3])
>>> list1
[1, 'hello', 'r', 4, [1, 4], 4, 1, 2, 3]
>>> list1 + (1,2,3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list1 + (1,2,3)
TypeError: can only concatenate list (not "tuple") to list
>>> list1 + [1,2,3]
[22, 'Hello', 's', 5, [22, 5], 5, 22, 23, 24, 22, 23, 24]
>>> print(["sanskar"]*3)
['sanskar', 'sanskar', 'sanskar']
>>> list1.insert(3,"sanskar bandi")
>>> list1
[22, 'Hello', 's', 'sanskar bandi', 5, [22, 5], 5, 22, 23, 24]
>>> list
[1, 2, 3]
>>> list=[1,3,4]
>>> list[1:1]=[9,93,44]
>>> list
[1, 9, 93, 44, 3, 4]
>>> list[1:3]=[9,93,44]
>>> list
[1, 9, 93, 44, 44, 3, 4]
>>> list.remove(44)
>>> list
[1, 9, 93, 44, 3, 4]
>>> list.pop()
4
>>> list
[1, 9, 93, 44, 3]
>>> list.clear()
>>> list
[]
>>> list=[11,3,4,2,5,6,4,5]
>>> list.count(4)
2
>>> 
