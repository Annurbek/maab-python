#task 1
def check(func):
    def web(a,b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            print("Denominator can't be zero")
    return web

@check
def div(a, b):
    return a / b
print(div(4,0))

