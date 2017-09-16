
def buble_sort(list):
    temp=0
    temp2=0
    for i in range (0,len(list)):
        temp=list[i]
        for j in range  (0,len(list)-1-i):
            if(list[j]>list[j+1]):
                temp=list[j+1]
                list[j+1]=list[j]
                list[j]=temp
    return list
                
                
def main():
    list=[90,80,70,10,1,0]
    list=input("please enter list of number like example 1,2,2,4,5,5 :").split(",")
    list=[int(i) for i in list]
    print(buble_sort(list))

main()
