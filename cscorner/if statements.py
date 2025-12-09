n=10
if n==10:
    print(n)
print('n is 10')

n=10
if n==10:
    print(n)
    print('end of the program')

    n=4
    if n%2==0:
        print('n is even')   #remainder 0

n=5
if n%2==0:
    print('n is even') 

# ifelse
n=5
if n%2==0:
    print('n is even')
    
else:
    print('n is odd')


time=20
if time==20:
    print("its time for dinner")

time=18
if time==20:
    print("itd time for dinner")
else:
    print("its not time for yet.")

#if,elif,else
time=15
if time==8:
    print("its time for breakfast")

elif time ==13:
    print("its time to lunch")

elif time ==20:
    print("its time for dinner")

else:
    print("its not time to lunch")

age=19
if age>=18:
    print("you are elgeble to vote ")
else:
    print("you are not elgeble to vote ")

#and operator
age=16
has_studentid=True
if age<18 and has_studentid:
    print("you are elgeble to discount")
else:
    print("you are not elgeble")

#nested if statements
day="saterday"
is_raining=false

if day=="saterday" or "sunday":
   if not is raining:
       print("lets visit mysure")
    else:
       print("lets stay home")
else:
    print("lets weekday,wait fora weeekend")