def extract_and_print(x:int):
    while x>0:
        print(x%10,end=" ")
        x = x//10

extract_and_print(1234)