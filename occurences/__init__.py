import math

def findOccurences(source,matchChar):
    """Assumes source is a string and matchChar is a matchCharacter
    return number of occurences"""
    occurence = 0
    for char in source:
        if char==matchChar: occurence+=1
    return occurence

def isPrime(number):
    """assumes number is an integer finds
    if it is also prime"""
    if number==2: return True
    for factor in range(2,int(math.sqrt(number))+1):
        if isDivisible(number,factor): return False
    return True

def isDivisible(number,factor):
    """finds if the number is divisble by factor 
    returns a boolean"""
    return number%factor==0

def multiply(factor1, factor2):
    if factor1>factor2: return multiply(factor2, factor1)
    Sum=0
    for i in range(0,factor1):
        Sum=Sum+factor2
    return Sum

def recursive(factor1, factor2):
    if factor1>factor2: return recursive(factor2, factor1)
    if factor1==1: return factor2
    return recursive(factor1-1,factor2)+factor2

def factorial(n):
    if n <=2: return n
    return n*factorial(n-1)

def fibonacci(n):
    if n<=1: return n
    return fibonacci(n-1)+fibonacci(n-2)

def palindrome(string):
    """check if string is a palindrome"""
    if string=='':return True
    if string[0]==string[-1]: return palindrome(string[1:-1])
    return False

def perfectCube(nCube):
    cube = False
    for integer in range(int(abs(nCube)**(1/3))+2): 
        if integer**3==abs(nCube):
            cube = True
            break
    return cube

def biggestOdd(list1):
    bigOdd = 0
    for integer in list1:
        if(integer%2==1 and (bigOdd==0 or integer>bigOdd)):
            bigOdd = integer
    return bigOdd

def biggestBuried(s):
    s+=' '
    list1 =[]
    string =''
    for i in s:
        if i.isdigit():
            string+=i
        else:
            if string=='':  pass
            else:   list1.append(int(string))
            string=''            
    if list1:
        string=max(list1)
    else:
        string=0
    return string

def binary(x):
    if x ==0:
        return '0'
    if x == 1:
        return '1'
    return binary(x//2)+binary(x%2)

