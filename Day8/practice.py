# #Timer decorator
# import time
# from functools import wraps

# def timer(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start = time.perf_counter()
#         result = func(*args,**kwargs)
#         end = time.perf_counter()
#         print(f"{func.__name__} is taking {start-end}s to run")
#         return result
#     return wrapper

# @timer
# def slow_call_api():
#     print(f"time taken is delay by 1.5 - {time.sleep(1.5)}")

# slow_call_api()

#################################################Logger##################################################


# import datetime
# from functools import wraps

# def logger(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         ts = datetime.datetime.now().strftime("%H:%M:%S")
#         print(f"[{ts}] calling | arg = {args}")
#         result = func(*args,**kwargs)
#         print(f"[{ts}] | result = {result}")
#         return result
#     return wrapper

# @logger
# def add(a,b):
#     return a+b

# add(3,7)


#####################################Retry Decorator###############################################

import time
from functools import wraps

def retry(max_attempts=3,delay=1.0):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
                    time.sleep(delay * (attempt + 1))  # backoff
            raise RuntimeError(f"{func.__name__} failed after {max_attempts} attempts")
        return wrapper
    return decorator

@retry(max_attempts=3,delay=1.0)
def call_api():
    raise ConnectionError("timeout")

call_api() 