numbers = [3, 28, 24, 7, 6]

while True:
    answer = input("数字を入力するか、ｑで終了します:")
    if answer == "q":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか、ｑで終了します:")
    if answer in numbers:
        print("正解")
    else:
        print("不正解")

