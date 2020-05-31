import math

def karatsuba(x,y):
    """Karatsuba to multiply 2 big numbers in a more efficient manner"""
    if len(str(int(x)))==1 or len(str(int(y)))==1:
        return x*y
    else:
        n=max(len(str(x)),len(str(y)))
        ndiv2=math.ceil(n/2)
        a= x // 10**(ndiv2)  #in large number this int(y / 10**(ndiv2)) would cause lose in precision 
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
