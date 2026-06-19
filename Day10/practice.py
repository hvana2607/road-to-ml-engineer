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



def fib(n):
    for i in n:
        a=[0,1]
        if n == 0:
            return 0
        if n == 1:
            return 1
        a.append((len(a)-1) + (len(a)-2))
        return a
    
     
def memoize(func):
    cache ={}
    def wrapper(n):
        if n in cache:
            return cache[n]
        result = func(n)
        cache[n] = result
        return result
    return wrapper

fast_fib = memoize(fib)

print(fast_fib(30))



