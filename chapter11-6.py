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

print(multiple_matrix(m1,m2))

def main():
    t1=[0]*3
    list= input("please enter the first row of first matrix like this 1,2,3 :").split(",")
    t1[0]=[float(i) for i in list]
    list=input("please enter the second row of first matrix like this 1,2,3 :").split(",")
    t1[1]=[float(i) for i in list]
    list=input("please enter the third row of first matrix like this 1,2,3 :").split(',')
    t1[2]=[float(i) for i in list]
    t2=[0]*3
    list= input("please enter the first row of second matrix like this 1,2,3 :").split(",")
    t2[0]=[float(i) for i in list]
    list=input("please enter the second row of second matrix like this 1,2,3 :").split(",")
    t2[1]=[float(i) for i in list]
    list=input("please enter the third row of second matrix like this 1,2,3 :").split(',')
    t2[2]=[float(i) for i in list]

    print(multiple_matrix(t1,t2))
    
main()
    