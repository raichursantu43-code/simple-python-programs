def decorator_name(func):
    def wrapper():
        print("namaskara")
        func()
        print("take care")
    return wrapper

@decorator_name
def intro():
    print("i am santu")

intro()


def decorator_name(func):
    def wrapper():
        print("hello")
        func()
        print("take care")
    return wrapper

@decorator_name
def intro():
    print("santu")
intro()

def show_result(func):
    def wrapper(a, b):
        print("result: ", end="")
        func(a, b)
    return wrapper

@show_result
def add(a,b):
    print(a+b)
add(1,2)

def logger(func):
    def wrapper(a, b):
        print(f"function'{func.__name__}'is being called")
        func(a, b)
    return wrapper
@logger
def add(a, b):
    print(a+b)

@logger
def sub(a, b):
    print(a-b)

add(10,10)
sub(100,10)


def login_required(func):
    def wrapper():
        print("checking if user is logged in...")
        func()
    return wrapper
@login_required
def view_profile():
    print("ravi's profile opened")
view_profile()     