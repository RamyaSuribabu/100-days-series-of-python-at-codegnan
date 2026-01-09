"""
#if number is zero print like the "entered number is zero"
num=int(input())
if num==0 :
    print("entered num is 0")
print("program done")
"""
#--------------------------------------

#check if number is zero or not
#approach 1
"""
n=int(input("enter a number"))
if n!=0 :
    print("number is not a zero")
else:
    print("number is zero")
    """

# approach2

"""
n=int(input("enter a number"))
if n==0 :
    print("number is a zero")
else:
    print("number is not a  zero")
"""
#------------------------------------------



#checking if the entered number is positive or negative
"""num=int(input("enter a number"))
if num>-1  :
    print(num,"positive number")
else :
    print(num,"negative number")
print("program done")"""


#checking if the number is even or odd
"""num=int(input("enter a number"))
if num%2==0:
    print(num," is even ")
else :
    print(num,"is odd")
print("program done")"""

# checking if the number is positive even or positive odd
#approach1
"""n=int(input("enter a number"))
if n>-1 :
    if  n%2==0 :
        print("num is positive even number")
    else :
        print("num is positive odd number")
elif  n<=-1 :
    if  n%2==0 :
        print("num is negative  even number")
    else:
        print("num is negative odd number")
"""
#approach2
"""
n=int(input("enter a number"))
if n>-1  and n%2==0 : #we can take if n>=0 
        print("num is positive even number")
elif n>-1  and n%2==1 :   # we can take n>=0 and n%2!=0
        print("num is positive odd number")
elif n<=-1 and  n%2==0 :   # #we can take if n<0 
        print("num is negative  even number")
elif n<=-1 and  n%2==1 :    # we can take n<0 and n%2!=0
        print("num is negative odd number")

# we  don't have to write the last elif statement directly we can write the else statement
statement with negative odd number
"""

























