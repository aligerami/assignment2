import random
import copy
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

    row=[]
    column=[]
    queen_number=0
    start=0
    chessboad=[0]
    while  queen_number!=8:
    #if True:
        queen_number=0
        chessboad=8*[0]
        row.clear()
        column.clear()
        print("************************************")
        for l in range (0,8):
            chessboad[l]=8*[0]
        for i in range (0,8):
            for j in range (0,8):
              print("i is ",(i+start)%8," j is ",j)
              print("check : ",check_queen_in_board(chessboad,(i+start)%8,j))

              if  check_queen_in_board(chessboad,(i+start)%8,j):  
                  chessboad[(i+start)%8][j]=1
                  row.append(j)
                  column.append((i+start)%8)
                  queen_number=queen_number+1
                  break
                  print(" queen i is ",(i+start)%8," j is ",j)
        start=1+start
        print("start is",start)
    return chessboad

def is_solved(list): 
    for i in range(0,len(list)):
        for j in range (0,len(list[i])):
            if(list[i][j]==1):
                    for k in range(0,len(list)):
                        if(list[i][k] == 1 and k!=j):
                            return False;
                        if(list[k][j]==1 and k!=i):
                            return False
                        if(j+k<8 and i+k<8):
                            if(list[k+i][k+j]==1 and k!=0):
                                return False
                        if(j-k>=0 and i+k<8):
                            if(list[k+i][j-k]==1 and k!=0):
                              return False
    return True
def check_queen_in_board(list,i,j):
    temp=  copy.deepcopy(list)
    temp[i][j]=1
    print(temp)
    draw_a_chessboard(temp)
    return is_solved(temp)
    return True
def main():
    flag=True
    print("*****************")
    board=eight_queen()
    draw_a_chessboard(board)
    if(is_solved(board)):
        draw_a_chessboard(board)
    
       
list=[[0,0,0,1,0,0,0,0],
      [0,1,0,0,0,0,0,0],
      [0,0,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,1],
      [0,0,0,0,0,1,0,0],
      [1,0,0,0,0,0,0,0],
      [0,0,1,0,0,0,0,0],
      [0,0,0,0,0,0,1,0]
    ]      
#print(check_queen_in_board(list,2,0))
#print(is_solved(list))

main()