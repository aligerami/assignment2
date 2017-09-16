class location():
    def __init__(self,m):
        self.__m=m
        self.__max=0.0
        self.__row=-1
        self.__column=-1
        for i in range (0,len(m)):
            for j in range (0,len(m[0])):
                #print("i ",i," j ",j, " max ",self.__max)
                if self.__max< m[i][j]:
                    self.__max=m[i][j]
                    self.__column=i
                    self.__row=j
    def __str__(self):
        return "The location of the largest element is "+str(self.__max)+\
        " at   ("+str(self.__column)+","+ str(self.__row)+" )"
    
def main():
    size=(input("Enter the number of rows and columns in the list like this 2,3 :").split(","))
    m=[0]*int(size[0])
    counter=0
    while counter<int(size[0]):
        temp=input("Enter rows separated by space ").split(" ")
        m[counter]=[float(i) for i in temp]
        counter+=1
    l = location(m)
    print(l)
        
        
        
        

main()