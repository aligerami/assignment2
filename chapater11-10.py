import random
def create_random_0_1_matrix():
    #m=[[0]*4 ]*4
    m=[]
    for i in range (0,4):
        m.append([])
        for j in range(0,4):
             m[i].append(random.randint(0,1))
    print (m)
    return m    
def find_max_row(m):
    max=0
    for i in range (0,4):
        s=0
        for j in range(0,4):
            s+=m[i][j]
        if(s>max):
            max=s
    return max

def find_max_column(m):
    max=0
    for i in range (0,4):
        s=0
        for j in range(0,4):
            s+=m[j][i]
        if(s>max):
            max=s
    return max

def main():
    test=create_random_0_1_matrix()
    print(test)
    print("max column is : ",find_max_column(test))
    print("max row is : ",find_max_row(test))
    
    
main()
    