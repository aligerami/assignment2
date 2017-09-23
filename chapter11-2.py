def sumMajorDiagonal(m):
    sum=0
    for i in range (0,len(m)):
        sum+=m[i][i]
    return sum

def main():
    m=[0]*4
    list=input("Enter a 4-by-4 matrix row for row 1:").split(" ")
    m[0]=[float(i) for i in list]
    list=input("Enter a 4-by-4 matrix row for row 2:").split(" ")
    m[1]=[float(i) for i in list]
    list=input("Enter a 4-by-4 matrix row for row 3:").split(" ")
    m[2]=[float(i) for i in list]
    list=input("Enter a 4-by-4 matrix row for row 4:").split(" ")
    m[3]=[float(i) for i in list]
    
    print("\nSum of the elements in the major diagonal is:", sumMajorDiagonal(m))
main()