def find_missing_number(l):
    num=len(l)+1

    total_sum=num*(num+1)//2
    a=sum(l)
    missing_number=total_sum-a

    return missing_number

l=[1,2,4,5,6]
print("The missing number is : ",find_missing_number(l))