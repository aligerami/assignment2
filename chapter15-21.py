import math
def binary_to_decimal(binery_string):
    if(len(binery_string)>1):
        return int(math.pow(2,len(binery_string)-1))*int(binery_string[:1])+binary_to_decimal(binery_string[1:])
    return int(math.pow(2,len(binery_string)-1))*int(binery_string[:1])

binary_string=input("Enter binary number :")

print(" decimal value is ",binary_to_decimal(binary_string))