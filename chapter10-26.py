def merge(list1, list2):
    i=0
    j=0
    result=[]
    while i<len(list1) or j<len(list2):
        if(i+1>len(list1)):
               result.append(list2[j])
               j=j+1 
        elif(j+1>len(list2)):
                result.append(list1[i])
                i=i+1
        else:        
            print(i , j)
            if(list1[i]<list2[j] ):
                result.append(list1[i])
                i=i+1
            else:
                result.append(list2[j])
                j=j+1
        
    return result

def main():
    list1=[1,5,16,61,111]
    list2=[2,4,5,6]
    list1=input("insert list one like the example : 1,2,3,4,5 :").split(',')
    list2=input("insert list one like the example : 1,2,3,4,5 :").split(',')
    list1=[int(i) for i in list1]
    list2=[int(i) for i in list2]
    print(merge(list2,list1))

    
main()
            
    