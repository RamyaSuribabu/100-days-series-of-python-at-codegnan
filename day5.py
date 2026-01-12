"""
n=int(input())
if n%2==0:
    if n>-1:
        print("number is +ve even number")
    else:
        print("number is -ve even number")
else:
    if n>-1:
        print("number is +ve odd number")
    else:
        print("number is -ve odd number")
"""
# to check the numbers in a list whether they are even or odd
"""listt=[2,1,3,4,6,6,5,0]
for i in listt:
    if i%2==0:
        print(i," is even")
    else:
        print(i,"is odd")
else:
    print("program done")
"""


"""
listt=[2,1,-3,4,6,-6,5,0]
for i in listt:
    if i>0 :
        print(i," is +ve ")
    else:
        print(i,"is -ve")
else:
    print("program done")
"""
#printing 1 to 20 numbers using range functions
for i in range(1,21,1):
    print(i)
