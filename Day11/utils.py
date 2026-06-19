def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def divide(a,b):
    try:
        c= a/b
        return c
    except ZeroDivisionError as e:
        return None
def multiply(a,b):
    return a*b

if __name__ == "__main__":
    print(f"add two numbers {add(2,4)}")
    print(f"substract two numbers {subtract(4,7)}")
    print(f"divide {divide(9,0)}")
    print(f"multiply 2 numbers{multiply(2,4)}")
    