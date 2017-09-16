import math
def deviation(list):
    m=mean(list)
    sum=0
    for i in list:
        sum=sum+math.pow((i-m),2)
    print(" deviation is ",math.sqrt(sum/(len(list)-1)))
    return math.sqrt(sum/(len(list)-1))

def mean(list):
    sum=0
    for i in list:
        sum+=i
    print("mean is",sum/len(list))
    return sum/len(list)

def main():
    list=[1.9, 2.5, 3.7 ,2, 1, 6, 3, 4, 5, 2]
    list=input("please enter list of number like example 1,2,2,4,5,5 :").split(",")
    list=[float(i) for i in list]
    deviation(list)

main()
    
    