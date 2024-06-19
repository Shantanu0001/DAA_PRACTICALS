a=int(input("Enter the first no. : "))
b=int(input("Enter the second no. : "))

if (a>b):
    min=a
else:
    min=b

while(1):
    if(min%a==0 and min%b==0):
        print("LCM is : ",min)
        break
    min=min+1
    