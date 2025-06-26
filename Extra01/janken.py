import random

janken={0:"ジャンケン",1:"グー",2:"チョキ",3:"パー"}

def game():
    print("ジャンケン")
    win = "あなたの勝ちです"
    lose = "あなたの負けです"
    user = janken[0]
    pc = janken[0]
    while user==pc:
        ran = random.randint(1,3)
        pc=janken[ran]
        pcmes = "pcは"+janken[ran]+"です"
        me = input("1グー,2チョキ,3パー")
        me = int(me)
        user = janken[me]
        usermes = "userは"+janken[me]+"です"
        print(pcmes)
        print(usermes)
    if user == pc:
       print("あいこ")
    elif user == "グー":
        if pc == "チョキ":
           print(win)
        else:
           print(lose)
    elif user == "チョキ":
        if pc == "パー":
           print(win)
        else:
           print(lose)
    elif user == "パー":
        if pc == "グー":
           print(win)
        else:
           print(lose)
game()







