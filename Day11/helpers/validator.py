def is_vaild_email(email):
    if ("@" in email) and ("." in email):
        return True
    else:
        return False

def is_valid_phone(phone):
    if len(phone)==10:
        return True
    else:
        return False
    

if __name__ == "__main__":
    print(is_vaild_email("vhari@gmail.com"))   # True
    print(is_vaild_email("vharigmail.com"))    # False
    print(is_valid_phone("9876543210"))        # True
    print(is_valid_phone("12345"))     