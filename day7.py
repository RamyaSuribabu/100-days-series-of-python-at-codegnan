#attendence management system
#approach 1
"""
n=int(input("enter number of students in the class"))
present_count =0
absent_count =0
for roll_number in range(1,n+1):
    print("enter",roll_number," is present or not" )
    status=input(" select the following options 1 or 2 \n 1.present \n 2. absent")
    #check status
    if status == '1' :
        present_count += 1
    elif status =='2' :
        absent_count  += 1
    else:
        print("please select either 1 or 2 options")
print("total students in the class",n)
print("no of students present",present_count)
print("no of students absent ",absent_count)
percentage =(present_count/n)*100

print("attendence report",percentage)
"""
#approach 2
"""
n=int(input("enter number of students in the class"))
present_count =0
absent_count =0
roll_number = 1 #initialization
while roll_number <= n : # condition 
    print("enter",roll_number," is present or not" )
    status=input(" select the following options 1 or 2 \n 1.present \n 2. absent")
    #check status
    if status == '1' :
        present_count += 1
        roll_number  += 1 #incrementation 
    elif status =='2' :
        absent_count  += 1
        roll_number  += 1
    else:
        print("please select either 1 or 2 options")
print("total students in the class",n)
print("no of students present",present_count)
print("no of students absent ",absent_count)
percentage =(present_count/n)*100

print("attendence report",percentage)
"""
