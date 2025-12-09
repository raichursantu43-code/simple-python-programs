#1   find the area of triangle

base = float(input("enter the length of the base of the triangle: "))
height=float(input("enter the height of the triangle: "))
area = 0.5 * base * height
print(f"the area of the triangle is: {area}")

#2    write a program to swap two veriables
a = input ("enter the value of first variable (a):")
b = input ("enter the value of second variable (b):")
print(f"original values :a = {a},b={b}")
temp=a
a=b
b=temp
print(f"swapped values: a={a},b={b}")


# cheak even or odd
num = int(input("enter a number: "))
if num % 2==0:
    print("even")
else:
    print("odd")


