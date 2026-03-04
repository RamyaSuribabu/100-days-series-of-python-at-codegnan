import addition
import subtraction
from  multiplication import mul
from devision import div




choice=int(input())
if choice==1:
    print("addition of 2 numbers",addition.add(a,b))
if choice==2:
    print("subtraction of 2 numbers",subtraction.sub(a,b))
if choice==3:
    print("division of 2 numbers",div(a,b))
if choice==4:
    print("multiplication of 2 numbers",mul(a,b))

