import random
def draw_a_chessboard(list):
    for i in range (0,len(list)):
        for j in range (0,len(list[i])):
            print("|",end="")
            if(list[i][j]==1):
                print("Q",end="")
            else:
                print(" ",end="")
        print("|")
        
def eight_queen():
    chessboad=8*[0]
    for i in range (0,8):
      chessboad[i]=8*[0]
    i=0
    while i<8:
        i+=1
        x=random.randint(0,7)
        y=random.randint(0,7)
        if(chessboad[x][y]==1):
            i=i-1
        chessboad[x][y]=1
        #print(i,"x is:",x," y is:",y)
    return chessboad

def is_solved(list): 
    for i in range(0,len(list)):
        for j in range (0,len(list[i])):
            if(list[i][j]==1):
                    print('i ',i, " j ",j)
                    for k in range(0,len(list)):
                        if(list[i][k] == 1 and k!=j):
                            return False;
                        if(list[k][j]==1 and k!=i):
                            return False
                        if(j+k<8 or j-k>0) and (i+k<8 or i-k>0): 
                            if(list[k+i if(k+i)<len(list) else i-k][k+j if(k+j)<8 else j-k]==1 and k!=0):
                                print ("i is",k+i if(k+i)<len(list) else i+k-8)
                                print("j is",k+j if(k+j)<8 else j+k-8)
                                print('i ',i, " j ",j," k ",k)
                                draw_a_chessboard(list)
                                return False
                            
    return True
def main():
    flag=True
    while flag:
        print("*****************")
        board=eight_queen()
        if(is_solved(board)):
           draw_a_chessboard(board)
           print("heeell")
           flag=False
       
list=[[0,0,0,1,0,0,0,0],
      [0,1,0,0,0,0,0,0],
      [0,0,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,1],
      [0,0,0,0,0,1,0,0],
      [1,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,1,0]
    ]      
 
print(is_solved(list))
print(list[-2][2])

#main()