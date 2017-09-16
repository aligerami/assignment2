def locate_larges(m):
    max=0
    position=[0,0]
    for i in range (0,len(m)):
        for j in range (0,len(m[0])):
            if(m[i][j]>max):
                max=m[i][j]
                position=[i,j]
    return position,max
def main():
    
    n= eval(input("Enter number of rows : "))
    m=[0]*n
    counter=0
    while counter<n:
        
        list= input("please enter the first row of first matrix like this 1,2,3 : ").split(",")
        m[counter]=[float(i) for i in list]
        counter+=1
    position,max=locate_larges(m)
    print("largest elemnt is ",max)
    print("The location of largest number is ",position)
    
main()
    
            
    