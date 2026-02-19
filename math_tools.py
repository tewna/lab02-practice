#mathtools 

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def is_even(n):
    return n % 2 == 0

def subtract(a,b):
    return a-b

def max_of_three(a,b,c):
    return max(a,b,c)

def is_palindrome(s):
    ans = ''
    for i in s:
        if i != ' ':
            ans += i
    if ans == ans[::-1]:
        return True
    else:
        return False

def find_min(numbers):
    min_num = 0  #just for now
    for i in range(len(numbers)):
        if i==0:
            min_num = numbers[i]
        elif numbers[i]<= min_num:
                min_num = numbers[i]

    return min_num

def remove_duplicates(items):
    newlist = []
    for i in items:
        if i not in newlist:
            newlist.append(i)
    return newlist

        