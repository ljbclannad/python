#最简单的装饰器
def decorator(func):
    def wrapper():
        print("wrapper")
        func()
    return wrapper


@decorator
def greet():
    print('hello world')

# greet = decorator(greet)

greet()

#带有多个参数的装饰器
def argsDecorator(func):
    def wrapper(*args,**kwargs):
        print("args Wrappers")
        func(*args,**kwargs)
    return wrapper;   


@argsDecorator
def argsGreet(name,age):
    print(name + "---"+age)

argsGreet("Liu","33")

#带有自定义参数的装饰器
def repeat(num): 
    def my_decorator(func): 
        def wrapper(*args, **kwargs): 
            for i in range(num): 
                print('wrapper of decorator') 
                func(*args, **kwargs) 
        return wrapper 
    return my_decorator
        
@repeat(4)
def greet(message): 
    print(message)


greet("hello")

#类装饰器
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello world")

example()
example()