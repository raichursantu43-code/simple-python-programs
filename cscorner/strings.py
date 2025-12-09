sub='pythonsql'
print(sub.upper(),sub.lower(),sub.swapcase())  #case functions

sub='   python  '
print(sub.lstrip(),sub.rstrip(),sub.strip())   #strip functions

sub='###python$$$'
print(sub.lstrip('#'))
print(sub.rstrip('$'))

sub='#python#sql#'
print(sub.strip('#'))

sub='python 3.10.1'
print(sub.isalpha())
print(sub.isnumeric())

#split function
sub='python,sql,aws,snow,adf'
print(sub.split(','))

print(len(sub.split(',')))

first_name="jhon"
last_name="doe"
full_name=first_name + "  " + last_name 
print(full_name)

greeting="hello !" * 3
print(greeting)

x="    hello   "
print(x.strip())

x="hello"
print(x.upper())

x="hello world"
print(x.replace("world","python"))

#indexing
s="python"
print(s[2])
print(s[5])

#slicing
x="python programming"
print(x[0:4])
print(x[ :6])

my_list=[1,2,3,4]
print( 3 in my_list)

