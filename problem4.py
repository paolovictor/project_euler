'''
Created on 12/01/2011

@author: Paolo
'''

def is_palindrome(i):
    string = str(i)
    for i in range(0, len(string)/2):
        if string[i] != string[len(string) - i - 1]:
            return False
    return True

three_digit = [(i * 100) + (j * 10) + n for i in range(1,10) for j in range(0,10) for n in range(0, 10)]
print max((i * j for i in three_digit for j in three_digit if is_palindrome(i * j)))