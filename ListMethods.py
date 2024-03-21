L =['a','b','c','d','e','f','g']

#slicing start from n-th item and end before m-th item.
L[2:5]
#['c', 'd', 'e']

L[0:2]
#['a', 'b']

# -1 always refer as last item.
L[3:-1]
#['d', 'e', 'f']


L1 = ['red','blue','green','purple']

#replace an existing element with a new value by assigning the new value to the index.
L1[1]='black'
L1[-1]='violet'
#['red', 'black', 'green', 'violet']

#Add iteam using append()
L1.append('silver')
#['red', 'black', 'green', 'violet', 'silver']

#If you want to insert an item at a specific position in a list, use insert() method. 
L1.insert(1,'yellow')
#['red', 'yellow', 'black', 'green', 'violet', 'silver']

L2 = ['green','blue','red']

#combining lists using extend() method
L2.extend([1,2,3])
#['green', 'blue', 'red', 1, 2, 3]

#Alternatively we can use +/+= operator 
L2 + [4,5]
#['green', 'blue', 'red', 1, 2, 3, 4, 5]

L2 += [6,7]
L2
#['green', 'blue', 'red', 1, 2, 3, 6, 7]

#Remove an item by index we can use pop()
L2.pop(1)
#remove blue from list

#If you don't need remove value use del statement
del L[1]
#delete red from list item

#if you want to delete item using value
L2.remove(3)
L2
#['green', 'red', 1, 2, 6, 7]

#To remove multiple value use del keyword with slice index
del L2[1:3]
L2
#['green', 2, 6, 7]

#Remove all Items using clear() method
L2.clear()
#print empty list

#The replication operator * repeats a list a given number of times.
L3 =['red']
L3 = L3*3
L3
['red','red','red']

#To find nuber of item in list use len()
len (L3)
#3

#Check if item exists in a list

Colors = ['red','blue','green']

if 'blue' in Colors:
    print('yes')

if 'yellow' not in Colors:
    print('yes')

#Iterate value through list
for Color in Colors:
    print(Color)
'''
red
blue
green
'''

#combine the range() and len() functions.
values = [1,2,3,4,5]

for i in range(len(values)):
   values[i] = values[i] * 2

print(values)    