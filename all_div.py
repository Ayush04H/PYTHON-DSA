def all_div(n:int):
    divisors = []
    for i in range(1,n+1):
        if n <=0:
            print("[]")
        if n%i == 0:
            divisors.append(i)

    print(divisors)


def all_div_2(n:int):
    divisors = []
    for i in range(1,(n//2)+1):
        if n <=0:
            break
        if n%i == 0:
            divisors.append(i)
    if n <=0:
        print("[]")
    else:
        divisors.append(n)
        print(divisors)

def all_div3(n:int):
    divisors = []
    for i in range(1,int(n**(1/2)+1)):
        if n % i == 0:
            divisors.append(i)
            if n//i != i:
                divisors.append(n//i)

    print(divisors)
all_div(19)
all_div_2(19)
all_div3(15)
all_div3(36)
        