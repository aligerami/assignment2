def sum_digit(a,sum):
    if a>10:
        sum=sum+a%10
        return sum_digit(a//10,sum)
    else:
        return sum+a
    
number=int(input("Enter the integer : "))
print("The sum of digits is ",sum_digit(number,0))


    