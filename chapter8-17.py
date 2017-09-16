import math
class point:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
    def distance(self,point):
        return math.sqrt( math.pow(self.__x-point.get_x(),2)+math.pow(self.__y-point.get_y(),2))
    def is_nearby(self,point):
        return self.distance(point)<5
    def __str__(self):
        return "("+str(self.__x)+","+str(self.__y)+")"
    
def main():
    x1=int(input("enter x1: "))
    y1=int(input("enter y1: "))
    x2=int(input("enter x2: "))
    y2=int(input("enter y2: "))
    p1=point(x1,y1)
    p2=point(x2,y2)
    print(p1) 
    print(p2.distance(p1)) 
    print(p2.is_nearby(p1)) 
    
main()