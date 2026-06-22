# class ValueNotProvided(Exception):
#     pass
# class ValueIncorrectProvided(Exception):
#     pass

# def add(*args):
#     args = list(args)
#     return sum(args)

# def sub(*args):
#     args = list(args)
#     result=args.pop(0)
#     for i in args:
#         result -= i
#     return result

# def multiply(*args):
#     args = list(args)
#     result=1
#     for i in args:
#         result = i*result
#     return result

# def divide(*args):
#     args = list(args)
#     try:
#         result=args.pop(0)
#         for i in args:
#             result = result/i
#         return result
#     except IndexError as e:
#         raise ValueNotProvided(f"No value provided")
#     except TypeError as e:
#         raise ValueIncorrectProvided(f"String is passed")


# def calculate(*args):
#     args = list(args)
#     f_name = args.pop(0)
#     args = tuple(args)
#     if f_name == "add":
#         return add(*args)
#     elif f_name == "sub":
#         return sub(*args)
#     elif f_name == "multiply":
#         return multiply(*args)
#     elif f_name == "divide":
#         try:
#             return divide(*args)
#         except ValueNotProvided as e:
#             return str(e)
#         except ValueIncorrectProvided as e:
#             return str(e)
            
#     else:
#         return f"You entered invalide function name {f_name}. Please enter correct one."

# print(calculate("divide", "x", 2))
    

# def greet_her(greet):
#     def greet_hello():
#         return f"hello {greet}"
#     return greet_hello

# hello = greet_her("harika")
# hello2 = greet_her("someone_else")
# print(hello())
# print(hello2())



# def fib(n):
#     for i in n:
#         a=[0,1]
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         a.append((len(a)-1) + (len(a)-2))
#         return a
    
     
# def memoize(func):
#     cache ={}
#     def wrapper(n):
#         if n in cache:
#             return cache[n]
#         result = func(n)
#         cache[n] = result
#         return result
#     return wrapper

# fast_fib = memoize(fib)

# print(fast_fib(30))

# # Q1. Write make_greeter(greeting) that returns a function. 
# # The returned function takes a name and prints "{greeting}, {name}!". 
# # Test: hi = make_greeter("Hello") → hi("Vhari") → Hello, Vhari!

# def make_greeter(greeting):
#     def name_greet(name):
#         return f"{greeting}, {name}!"
#     return name_greet
    
# hi = make_greeter("Hello")
# print(hi("Vhari"))

# # Q2. Write make_multiplier(n) that returns a function which multiplies any number by n. 
# # Test: triple = make_multiplier(3) → triple(7) → 21

# def make_multiplier(n):
#     def multiplier(m):
#         return n*m
#     return multiplier

# triple = make_multiplier(3)
# print(triple(7))

# # Q3. Write counter() that returns a function. 
# # Every time you call that returned function, it returns the next count starting from 1.
# # Test: c = counter() → c() → 1, c() → 2, c() → 3

# def counter():
#     i = 0
#     def count():
#         nonlocal i
#         i += 1
#         return i
#     return count

# c = counter()
# print(c())  # → 1
# print(c())  # → 2
# print(c())  # → 3

# #make_power(exp) → returns a function that raises any number to exp

# def make_power(exp):
#     def power(exp1):
#         return (exp1 ** exp)
#     return power

# square = make_power(2)
# print(square(5))   # → 25

# cube = make_power(3)
# print(cube(3))
    
# #make_between(min_val, max_val) → returns a function that checks if a number is between min and max.

# def make_between(min_val, max_val):
#     def check_num(num):
#         if num in range(min_val,max_val):
#             return True
#         else:
#             return False
#     return check_num

# check = make_between(1, 10)
# print(check(5))   # → True
# print(check(15))  # → False
# print(check(1))   # → True


# #################################################################################################

# #Q6 — apply(func, value) → calls func(value) and returns the result.

# def apply(func, value):
#     return func(value)

# def double(n):
#     return n * 2

# print(apply(double, 5))   # → 10
# print(apply(double, 3))   # → 6

# #Q7 — apply_twice(func, value) → applies func to value, then applies func to that result.

# def apply_twice(func, value):
#     return func(func(value))

# print(apply_twice(double, 3))  # → 12
# # because: double(3) = 6, then double(6) = 12

# #Q8 — last one! my_filter(lst, condition) → returns only items where condition(item) is True.

# def my_filter(lst, condition):
#     result = []
#     for i in lst:
#         if condition(i):
#             result.append(i)
#     return result

# print(my_filter([1,-2,3,-4,5], lambda x: x > 0))  # → [1, 3, 5]
# print(my_filter([10,25,3,50,7], lambda x: x > 10)) # → [25, 50]


# Q1 — Basic try/except
# Write a function safe_divide(a, b) that divides a by b. 
# If b is 0, print "Error: cannot divide by zero" and return None. 
# Otherwise return the result.

def safe_divide(a, b):
    try:
        c=a/b
    except ZeroDivisionError:
        print("Error: cannot divide by zero")
        return None
    else:
        return c
    
print(safe_divide(10, 2))   # → 5.0
print(safe_divide(10, 0))   # → Error: cannot divide by zero → None
