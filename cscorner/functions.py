def greet():
    print('hello,good morning')


greet()
greet()

def marriage(boy,girl):
    print(f'boy is {boy}')
    print(f'girl is {girl}')
    print(f'{boy} ,married {girl}')

marriage('chandan','chandana')
marriage('chandan','sneha')

def tables(num):
    for i in range(1,11):
        print(f'{num}x{i}={num*i}')

tables(5)
tables(6)
tables(7)