import math
raw_input= input("please enter list of number with like 3,4,5,6,7,8 :") 
list_input=raw_input.split(',')

len=len(list_input)
temp=0
for i in range (0,math.ceil(len/2)):
    temp=list_input[i]
    list_input[i]=list_input[len-i-1]
    list_input[len-i-1]=temp

print("*********The Result is***********")
print (list_input)    