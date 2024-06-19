def find_factors(num):
    factors=[]
    for i in range(1,num):
        if num%i==0:
            factors.append(i)
    return factors

print(find_factors(89))