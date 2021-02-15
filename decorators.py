#1 Functions are objects

def add_five(num):
    print(num + 5)
'''
print(add_five)
results in <function add_five at 0x...>
'''

#2 Functions within functions

def add_five(num):
    def add_two(num):
        return num + 2
    num_plus_two = add+two(num)
    print(num_plus_two + 3)

'''
add_two(7) -> name_error: add_two is not defined. It is declared in the
scope of add_five function
'''
#add_five(10)

#3 Returning functions from functions

def get_math_function(operation): # + or -
    def add(n1, n2):
        return n1 + n2
    def sub(n1,n2):
        return n1 - n2
    if operation == '+':
        return add
    elif operation == '-':
        return sub
'''
add_f = get_math_function('+')
-> <function get_math..> 
sub_function = get_math_function('-')
print(sub_function(4,6))
'''

#4 Decorating a function, decorators !!!

def title_decorator(print_name):
    def wrapper():
        print("CEO:")
        print_name()
    return wrapper

@title_decorator
def print_name():
    print("Sergiu")
'''
--the long way--
decorated_function = title_decorator(print_name) #call the decorator
decorated_function()

--the short way--
@title_decorator

'''
#print_name()

#5 Decorators w/ Parameters
#in order to accept arguments and use the @wrapper, 
#add *args, **kwargs to pass in any of the arguments that we will pass later
def title_decorator(print_name):
    def wrapper(*args, **kwargs):
        print("CEO:")
        print_name(*args, **kwargs)
    return wrapper

@title_decorator
def print_name(name, age):
    print(name + " you are "+ str(age))

print_name("Sergiu",19)