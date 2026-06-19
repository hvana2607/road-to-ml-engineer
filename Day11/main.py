from utils import add, subtract, divide, multiply
from config import APP_NAME, VERSION, MAX_RETRIES, DEBUG, AUTHOR


# print(f"add two numbers {add(2,4)}")
# print(f"substract two numbers {subtract(4,7)}")
# print(f"divide {divide(9,0)}")
# print(f"multiply 2 numbers{multiply(2,4)}")



print("=" * 40)
print(f"App     : {APP_NAME}")
print(f"Version : {VERSION}")
print(f"Author  : {AUTHOR}")
print(f"Retries : {MAX_RETRIES}")
print(f"Debug   : {DEBUG}")
print("=" * 40)
print("App started successfully!")


from helpers.formatter import make_title,pad_left
from helpers.validator import is_vaild_email,is_valid_phone

print(make_title("AI Engineer"))
print(pad_left("Vhari", 20))

# test validator
print(is_vaild_email("vhari@gmail.com"))   # True
print(is_vaild_email("vharigmail.com"))    # False
print(is_valid_phone("9876543210"))        
print(is_valid_phone("12345"))      