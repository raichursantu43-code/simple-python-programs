square_number = lambda a : a**2
print(square_number(10))

a= lambda : 3
print(type(a),a())

a=lambda x : x**2
print(a(8)) 

x='python is and powerful language'
a= lambda s:s.split()
print(a(x))

def a_plus_b_formulae(a,b):
    return (a**2+b**2+2*a*b)
print(a_plus_b_formulae(3,5))

a_plus_b_formulae=lambda a,b : a**2+b**2+2*a*b
print(a_plus_b_formulae(3,5))

doubleit=lambda x : x**2
ml=list(range(11))
doubleit(ml)

mylist=[2,4,5]
square=lambda a : a**2
print(square(mylist)) 


