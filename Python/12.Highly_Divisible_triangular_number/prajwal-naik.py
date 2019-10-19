# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 21:15:50 2019

@author: Prajwal
"""

def isPrime(n):
    if(n==1):
        return 0
    elif(n<4):
        return 1
    elif(n%2==0):
        return 0
    elif(n<9):
        return 1
    elif(n%3==0):
        return 0
    else:
        r=n**0.5
        f=5
        while(f<=r):
            if((n%f==0) or (n%(f+2)==0)):
                return 0
            f+=6
        return 1
    
    
if __name__=='__main__':
    n=3
    Dn=2
    cnt=0
    n1=0; Dn1=0; exponent=0;
    P=200
    primearray=[]
    idx=0
    candidate=1
    candidate += 1
    if (isPrime(candidate)):
        primearray.append(candidate)
        idx+=1
    while(idx<P):
        candidate += 1
        if (isPrime(candidate)):
            primearray.append(candidate)
            idx+=1
    while(cnt<=500):
        n+=1
        n1=n
        if(n1%2==0):
            n1/=2
        Dn1=1
        for i in range(0, P):
            if(primearray[i]*primearray[i] > n1):
                Dn1 *= 2
                break
            
            exponent=1
            while ( n1% primearray[i] == 0):
                exponent+=1
                n1/=primearray[i]
            if(exponent>1):
                Dn1*=exponent
            if(n1==1):
                break
        cnt=Dn*Dn1
        Dn=Dn1
    print(int((n*(n-1))/2))
    
        
       
    
    
        