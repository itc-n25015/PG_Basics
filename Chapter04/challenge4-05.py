a = input("type a number:")
b = input("type another:")
a = float(a)
b = float(b)
try:
    print(a / b)
except ZeroDivisionError:    
    print("エラー")








