def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다")
        return None
    else:
        return a / b