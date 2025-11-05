def dec(func):
    def wrapper(*args,**kwargs):
        print('Decorator is working 1')
        func(*args,**kwargs)
    return wrapper

def sed(n):
    def dec2(func):
        def wrapper(*args,**kwargs):
            print('Decorator is working 2')
            for _ in range(n):
                func(*args,**kwargs)
        return wrapper
    return dec2

@sed(3)
@dec
def say_hello(name):
    print(f'Hello {name}')

say_hello('Dadakhon')