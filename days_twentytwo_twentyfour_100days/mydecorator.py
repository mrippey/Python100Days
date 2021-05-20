from datetime import datetime

def this_is_your_wakeup(alarm_time):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = datetime.now().hour
            if current_time >= alarm_time:
                func()
            else:
                print('go back to sleep')
        return wrapper
    return my_decorator

if __name__ == "__main__":
@this_is_your_wakeup(21)
def hello():
    print('wake up')

hello()




import pandas as pd 
import json 

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        test = pd.read_json(func(*args, **kwargs))
        
        pd.set_option('max_colwidth', 0)
        
        print(test.head())
    return wrapper 

@my_decorator
def some_function():
    return 'Downloads/cars.json'  # from PyBites Challenge: https://codechalleng.es/bites/130/

if __name__ == '__main__':
    some_function()
