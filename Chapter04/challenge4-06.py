def f(n): 
    """
    :Chapter04-1.
    """
    return n ** 2 
f(3) 
result = f(3)
   
print(result) 

print("apple")
"""
Chapter04-2.
"""
def f(a,b,c, j=3, s=10):
    """
    Chapter04-3.
    """
    return a * b / c + j * s + a
result = f(2,4,7)
print(result)

def jihoon(i):
    return i / 2
def shinyu(y):
    return y * 4
"""
Chapter04-4.
"""
x = jihoon(6)
y = shinyu(x)
print(y)

a = input("type a number:")
b = input("type another:")
a = float(a)
b = float(b)
try:
    print(a / b)
    """
    Chapter04-5.
    """
except ZeroDivisionError:
    print("エラー")
