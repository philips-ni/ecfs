# importing functools for reduce()
import functools
import string
 
# initializing list
lis = [ 1 , 3, 5, 6, 2, ]
 
# using reduce to compute sum of list
print ("The sum of the list elements is : ",end="")
print (functools.reduce(lambda a,b : a+b,lis))
 
# using reduce to compute maximum element from list
print ("The maximum element of the list is : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,lis))

def string_to_int(s):
    return functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.index(c),
        s[s[0] == "-":],0) * (-1 if s[0] == '-' else 1)
print(string_to_int("-101"))
print(string_to_int("101"))      
