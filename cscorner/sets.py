google={'apple','ms','oracle'}
yahoo={'tcs','ibm','apple'}
print(google, yahoo)
print(list(google.union(yahoo) ))

#set operations
#union
set1={1,2,3}
set2={4,5,6}
union_set=set1 | set2
print(union_set)

#intersectiom
set1={1,2,3}
set2={4,5,2,6}
union_set=set1 & set2
print(union_set)

sets={1,2,3,4,5,6,7,8}
sets.pop()
print(sets)   #remove random element





