import math

def sod(number):
    num_digits=int(math.log10(number))+1
    divisor=10 ** (num_digits-1)
    sum=0

    while divisor > 0:
        digit=number//divisor
        sum+=digit
        number%=divisor
        divisor//=10
    print(sum)

sod(567898)