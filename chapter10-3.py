raw_input= input("please enter list of number with like 3,4,5,6,7,8 :") 
list_input=[int(x) for x in raw_input.split(',')]
result=[0]*100
for i in range (0,len(list_input)):
    result[list_input[i]]+=1

for i in range (0,len(result)):
    if(result[i]!=0 and result[i]!=1):
        print(i ," occurs ",result[i] , "times")
    elif( result[i]==1):
        print(i ," occurs ",result[i] ,"time")
        
    
