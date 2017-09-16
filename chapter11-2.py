def sumMajorDiagonal(m):
    sum=0
    for i in range (0,len(m)):
        sum+=m[i][i]
    
    return sum

print(sumMajorDiagonal(m))
        