mylist = list (range(11))
newlist=[]
for i in mylist:
    newlist.append(i**2)
    print(newlist)


mylist = list(range(101))
newlist=[]
for i in mylist:
    if i%2==0:
       newlist.append(i**2)
print(newlist)

mylist =[1,2,3,4,5,6]
newlist = [i**3 for i in mylist if i%2 !=0]
print(newlist)


squares_list =[]
for x in range (11):
    if i%2==0:
        squares_list.append(i**2)
print(squares_list)        

[(i,j) for i in range(3) for j in range(3) if i==j]

paragraph = ['there was a fox.','it was abrown in colour.']

for sentence in paragraph:
     
    for word in sentence.split():
        print(word)
