import random

se={0:"星座",1:"山羊",2:"水瓶",3:"魚",4:"牡羊",5:"牡牛",6:"双子",7:"蟹",8:"獅子",9:"乙女",10:"天秤",11:"蠍",12:"射手"}

def seiza():
    m = input("何月生まれ？")
    d = input("何日生まれ？")
    m = int(m)
    d = int(d)
    mes = se[m]+"座です"
    mes1 = se[m+1]+"座です"
    if m == 1:
        if d < 20:
              print(mes)
        else:
              print(mes1)
    elif m == 2:
        if d < 19:
              print(mes)
        else:
              print(mes1)
    elif m == 3:
        if d < 21:
              print(mes)
        else:
              print(mes1)
    elif m == 4:
        if d < 20:
              print(mes)
        else:
              print(mes1)
    elif m == 5: 
        if d < 21:      
              print(mes)
        else:     
              print(mes1)
    elif m == 6: 
        if d < 22:      
              print(mes)
        else:     
              print(mes1)
    elif m == 7: 
        if d < 23:      
              print(mes)
        else:     
              print(mes1)
    elif m == 8: 
        if d < 23:      
              print(mes)
        else:     
              print(mes1)
    elif m == 9: 
        if d < 23:      
              print(mes)
        else:     
              print(mes1)
    elif m == 10: 
        if d < 24:      
              print(mes)
        else:     
              print(mes1)
    elif m == 11: 
        if d < 23:      
              print(mes)
        else:     
              print(mes1)
    elif m == 12: 
        if d < 22:      
              print(mes)
        else:     
              print(mes1)
seiza()








