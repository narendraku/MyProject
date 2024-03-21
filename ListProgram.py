#list of String
l =["red","green","blue"]


#list of mixed data type
l1 = [1,"yello",1.5,(10+5j),True]

#List Constructor
#Convert string to List
l2 =list("abc")
#['a', 'b', 'c']

#convert tuple to list
l3 = list((1,2,3,4))
#[1, 2, 3, 4]

#Nested List
l4 = ['aa','sd',['uv',['hsd','cc'],'bb'],'ss']
#['aa', 'sd', ['uv', ['hsd', 'cc'], 'bb'], 'ss']

#accesse individual iteam in list
l5 = ['red','blue','green','yellow','white']
l5[0]
#red
l5[4]
#white

#python will rise an IndexError if you use index that exceeds the number of items in list
#l5[7]
#IndexError: list index out of range

#Negative indexing count index backward from end of the list L5[-1] refers to last the iteams.
l5[-1]
#white
l5[-3]
#green

#access individual items in a nested list using multiple indexes.
l6 = ['aa','sd',['uv',['hsd','cc'],'bb'],'ss']
print(l6[0][0])
print(l6[0][1])
print(l6[1][0])
print(l6[1][1])
print(l6[0])
print(l6[1])
print(l6[2])
print(l6[3])
print(l6[3][0])
'''a
a
s
d
aa
sd
['uv', ['hsd', 'cc'], 'bb']
ss
s'''

# Note all methods in list are
'''
append()	Adds an item to the end of the list
insert()	Inserts an item at a given position
extend()	Extends the list by appending all the items from the iterable
remove()	Removes first instance of the specified item
pop()	Removes the item at the given position in the list
clear()	Removes all items from the list
copy()	Returns a shallow copy of the list
count()	Returns the count of specified item in the list
index()	Returns the index of first instance of the specified item
reverse()	Reverses the items of the list in place
sort()	Sorts the items of the list in place'''