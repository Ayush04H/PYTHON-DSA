def armstrong(x:int):
    x1 = x
    y = 0
    while x>0:
        rem = x%10
        y += (rem**3)
        x = x//10

    if y == x1:print(1)
    else:print(0)
        




armstrong(153)
armstrong(1534)
armstrong(1)
armstrong(370)
armstrong(371)
armstrong(407)