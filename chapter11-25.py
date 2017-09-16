def is_markov_matrix(m):
    for i in range (0,len(m)):
        sum=0
        for j in range (0,len(m[0])):
            if(m[i][j]<0):
                return False
            sum+=m[j][i]
        if(sum!=1):
            return False
    return True

            
def main():
    m=[0]*3
    m=[[0.15 ,0.875 ,0.375],[0.55, 0.005 ,0.225],[0.30 ,0.12 ,0.4]]
    list= input("please enter the first row of first matrix like this 1,2,3 :").split(",")
    m[0]=[float(i) for i in list]
    list=input("please enter the second row of first matrix like this 1,2,3 :").split(",")
    m[1]=[float(i) for i in list]
    list=input("please enter the third row of first matrix like this 1,2,3 :").split(',')
    m[2]=[float(i) for i in list]

    print(is_markov_matrix(m))
    
main()