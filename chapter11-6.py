def multiple_matrix(a, b):
    result=len(a)*[0] 
    result= [[0 for x in range(len(a))] for y in range(len(a[1]))]
    for i in range (0,3):
        for j in range (0,3):
            for k in range (0,3):
             result[i][j]+= a[i][k]*b[k][j]
    
    return result

m1= [[1,2,3],
    [4.0 ,5.0, 6.0],
    [7,8,9]]
m2= [[0.0 ,2.0, 4.0],   
    [ 1.0, 4.5, 2.2],  
    [1.1 ,4.3,5.2]]


def main():
    m1=[0]*3
    m2=[0]*3
    list= input("Enter matrix1: ").split(" ")
    for i in range (0,3):
       m1[i]= [float(i) for i in list [i*3:(i+1)*3+1]]
        
    list=input("pEnter matrix2: ").split(" ")
    for i in range (0,3):
       m2[i]= [float(i) for i in list [i*3:(i+1)*3+1]]
    
    m3= multiple_matrix(m1,m2)

    for i in range (0,3):
        for j in range (0,3):
            if(j==2 and i==1):
                print("{:3.2f}".format(m1[i][j]),end="  *")
            else:
                print("{:3.2f}".format(m1[i][j]),end="   ")
        print("",end=" ")
        for k in range(0,3):
            if(k==2 and i==1):
                print("{:3.2f}".format(m2[i][j]),end=" = ")
            else:
                print("{:3.2f}".format(m2[i][j]),end="   ")
        print("",end=" ")
        for l in range(0,3):
            print("{:.2f}".format(m3[i][j]),end=" ")
        print("")
             
    
main()

    