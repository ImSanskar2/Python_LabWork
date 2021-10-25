>>> (lambda x: x*3)(4)
12
>>> (lambda x: x*3)([4])
[4, 4, 4]
>>> li=[1,2,3,4]
>>> l=filter(lambda x: x%2==0,li)
>>> print(list(l))
[2, 4]
>>> l=map(lambda x: x*x,li)
>>> list(l)
[1, 4, 9, 16]
>>> l=list(map(lambda x: x+2,li))
>>> print(l)
[3, 6, 11, 18]
>>> name=["Sanskar","Sairaj","Utkarsh","Jay"]
>>> last_name=["Bandi","Raghuwanshi","Odhekar","Dubey"]
>>> l=list(map(lambda x,y:x+" "+y,name,last_name))
>>> print(l)
['Sanskar Bandi','Sairaj Raghuwanshi','Utkarsh Odhekar','Jay Dubey']
