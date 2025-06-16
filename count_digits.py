def count_digit(x):
    i = 0 
    while x>0:
        x = x//10
        i+=1

    print(i)

count_digit(123456789)