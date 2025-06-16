# For int
def pallindrome(x):
    y = 0
    x1= x
    while x > 0:
        y = y*10 + (x%10)
        x = x//10
    if x1 == y:print(1)
    else:print(0)
    print(y)


x =121
pallindrome(x)

# For arrays / List
def pallindrome_2(x:list):
    if x ==x[::-1]:
        print(1)
    else:
        print(0)

pallindrome_2(['a','e','u'])
pallindrome_2([1,2,1])
pallindrome_2([1,2,1,2])


# Pallindrome for Strings
def pallindrome_3(s:str):
    left = 0 
    right = len(s) - 1
    pallindrome = 1
    while left < right:
        if s[left] != s[right]:
            pallindrome = 0
            break

        left += 1
        right -= 1

    print(pallindrome)

pallindrome_3("aeoea")


