#basic problem to check a number is positive,negative or zero

"""
num=int(input())
if num==0:
    print("entered number is zero")
elif num>0:
    print("entered number is positive number")
else :
    print("entered number is negative number")
"""
# finding the biggest number among 2 numbers
"""
num1=int(input())
num2=int(input())
num3=int(input())
if num1>num2 and num1>num3 :
    print(num1,"is greater than",num2 ,"and",num3)
elif num2>num1 and num2>num3 :
    print(num2,"is greater than",num1, "and",num3)
elif num3>num2 and num3>num1 :
    print(num3,"is greater than",num2 ,"and" ,num1)
else:
    print("all are equal ")
"""
#finding whether the number is 5's factor or not
"""
num=int(input())
if num%5==0 :
    print(num," has 5 as  factor ")
else :
    print(num,"have not  5 as factor ")
"""
#finding whether the number contains  5 or 3 as their   factor or not
#approach1
"""
num=int(input())
if num%5==0 :
    if num%3==0:
        print(num," have 5 &3  as  factors ")
    else :
        print(num," have only 5 as a factor")
elif num%3==0 :
    if num%5==0:
        print(num," have 5 &3  as  factors ")
    else :
        print(num," have only 3 as a factor")
else :
    print(num,"does not have 5 &3 as factors ")
"""
#approach 2
"""
num=int(input())
if num%5==0  and num%3==0:
        print(num," have 5 &3  as  factors ")
elif num%5==0:
        print(num," have only 5 as a factor")
elif num%3==0:
        print(num," have only 3 as a factor")
else :
    print(num,"does not have 5 &3 as factors ")

"""







    
