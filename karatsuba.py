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
def karatsuba(x,y):
    x_str,y_str=str(x),str(y)
    if len(x_str)==1 or len(y_str)==1:
        return x*y
    else:
        block_length=ceil( max(len(x_str)/2,len(y_str)/2)  )
        
        a,b = int(x[:block_length]),int(x[block_length:])
      
        b= x % 10**(ndiv2)

        c= y // 10**(ndiv2)

        d= y % 10**(ndiv2)

        
        ac=karatsuba(a,c)
        #print(ac)
        bd=karatsuba(b,d)
        #print(bd)
        prod=karatsuba(a+b,c+d)
        #print(prod)
        
        xy= ac* 10**(2*ndiv2) + (prod-ac-bd)*10**ndiv2 + bd
        return xy
    

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
