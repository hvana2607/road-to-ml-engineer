from functools import wraps
from datetime import datetime
def log_action(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        result = func(*args,**kwargs)
        with open("expenses.log","a") as log:
            log.write(f"[{datetime.now().strftime(f'%d %m %Y %H %M %S ')}] : {func.__name__} just ran \n")
            
        return result
    return wrapper

def handle_errors(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        try:
            result = func(*args,**kwargs) 
        except Exception:
            print("A friendly error function crashed") 
        else:
            return result
    return wrapper
