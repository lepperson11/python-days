# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == "__main__":
#     app.run()

import time

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()
        results = function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}s")
        return results
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()