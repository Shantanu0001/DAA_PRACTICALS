import math

def check_armstrong(num):
    num_string=str(num)
    sum=0

    for i in num_string:
        i=int(i)
        sum+=i*i*i

    if sum==num:
        print("Number is armstrong.")
    else:
        print("Number is not armstrong.")

check_armstrong(370)
