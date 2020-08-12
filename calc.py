
from division import divide
from multiply import multiply
from Add import add
from Subtraction import subtract

#addition - Ayush
#subtraction- Keerthana
#multiplication - SOmanshu
#division - Arjun


print("Guide for choosing operations--------------------")
print("1-- Addition")
print("2-- subtraction")
print("3-- multiplication")
print("4-- division")
ch=int(input('Enter choice:  '))
a=int(input("first number:  "))
b=int(input("second number:  "))

if(ch==1):
    print(add(a,b))
elif(ch==2):
    print(subtract(a,b))
elif(ch==3):
    print(multiply(a,b))

elif(ch==4):
    print(divide(a,b))

else:
    print("PLease enter a valid Choice")
