from math import ceil

def karatsuba(x,y):
    """Karatsuba to multiply 2 big numbers in a more efficient manner"""
     x_str, y_str = str(x), str(y)
    if len(x_str)==1 or len(y_str)==1:
        return x*y
    else:
        ndiv2=ceil(max(len(str(x)),len(str(y))))
        a= x // 10**(ndiv2) #in large number this int(y / 10**(ndiv2)) would cause lose in precision 
        #print(a)
        b= x % 10**(ndiv2)
        #print(b)
        c= y // 10**(ndiv2)
        #print(c)
        d= y % 10**(ndiv2)
        #print(d)
        
        ac=karatsuba(a,c)
        #print(ac)
        bd=karatsuba(b,d)
        #print(bd)
        prod=karatsuba(a+b,c+d)
        #print(prod)
        
        xy= ac* 10**(2*ndiv2) + (prod-ac-bd)*10**ndiv2 + bd
        return xy
       
karatsuba(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627)

from math import ceil

def karatsuba(num1, num2):
    num1Str = str(num1)
    num2Str = str(num2)
    if (num1 < 10) or (num2 < 10):
        return num1*num2

    maxLength = max(len(num1Str), len(num2Str))
    splitPosition = maxLength / 2
    high1, low1= int(num1Str[:-splitPosition]), int(num1Str[-splitPosition:])
    high2, low2= int(num2Str[:-splitPosition]), int(num2Str[-splitPosition:])
    z0 = karatsuba(low1, low2)
    z1 = karatsuba((low1 + high1), (low2 + high2))
    z2 = karatsuba(high1, high2)

    return (z2*10**(2*splitPosition)) + ((z1-z2-z0)*10**(splitPosition))+z0
    

a = 3141592653589793238462643383279502884197169399375105820974944592 
b = 2718281828459045235360287471352662497757247093699959574966967627
karat = karatsuba(a, b)
trad = a * b
print(karat)
print(trad)
print(karat == trad)

#############################################################################################

## dom's version
from math import ceil
def karatsuba(x,y):
    x_str, y_str = str(x), str(y)
    if len(x_str)==1 or len(y_str)==1:
        return x*y
    else:
        block_length = ceil(max(len(x_str)/2,len(y_str)/2)
        a, b = int(x_str[:block_length]), int(x_str[block_length:])
        c, d = int(y_str[:block_length]), int(y_str[block_length:])
        return a*c* 10**(2*block_length) + ((a+b)*(c+d)-a*c-b*d)*10**block_length + b*d

a = 3141592653589793238462643383279502884197169399375105820974944592 
b = 2718281828459045235360287471352662497757247093699959574966967627
karat = karatsuba(a, b)
trad = a * b
print(karat)
print(trad)
print(karat == trad)
