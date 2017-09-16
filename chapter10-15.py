def is_sort(list):
    temp=list[0]
    for i in list:
        if i<temp :
            return False;
        else:
            temp=i
    return True


def main():
    list=[1 ,1 ,3 ,4, 4, 5 ,7 ,9 ,10,30 , 11]
    #list=input("please enter list of number like example 1,2,2,4,5,5 :").split(",")
    list=[float(i) for i in list]
    print(is_sort(list))

main()

