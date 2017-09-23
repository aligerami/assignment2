import math
class TriangleError(RuntimeError):
    def __init__(self, m):
        RuntimeError.__init__(self)
        self.__m=m
        
    def __str__(self):
        return "this information is not for triangle. error message is :\n"+self.__m

class GeometricObject():
    def __init__(self,color="green",filled=True):
        self.__color=color
        self.__filled=filled
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
    def set_filled(self,filled):
        self.__filled=filled
    def is_filled(self):
        return  self.__filled
    def __str__(self):
        return "color: " + self.__color+" and filled: " + str(self.__filled)
    
class triangle(GeometricObject):
   
    def __init__(self,side1=1.0,side2=1.0,side3=1.0):
        self.__side1=side1
        self.__side2=side2
        self.__side3=side3
        self.validate_triangle()
   
    def validate_triangle(self):
        a=self.__side1
        b=self.__side2
        c=self.__side3
        angle_a=math.acos( (math.pow(a,2)-math.pow(b, 2)-math.pow(c, 2))/(-2*b*c))
        angle_b=math.asin( b*math.sin(angle_a)/a)
        angle_c=math.asin( c*math.sin(angle_a)/a)
        print("angle a",angle_a,"angle b ",angle_b,"angle c ",angle_c)

        if(angle_c+angle_b+angle_a!=180):
            print("Before raise error")
            raise TriangleError(" wrong input")
        
        
        
        
        
    
    def set_side1(self,side1):
        self.__side1=side1
    def get_side1(self):
        return self.__side1
        
    def set_side2(self,side2):
        self.__side2=side2
    def get_side2(self):
        return self.__side2
        
    def set_side3(self,side3):
        self.__side3=side3
    def get_side3(self):
        return self.__side3
    def get_area(self):
        return  math.sqrt((self.get_perimeter()*(self.get_perimeter()-self.get_side1())*
                (self.get_perimeter()-self.get_side2())*(self.get_perimeter()-self.get_side3())))
    def get_perimeter(self):
        return (self.__side1+self.__side2+self.__side3)/2
    def __str__(self):
        return "Triangle: side1 = " + str(side1) + " side2 = " + \
                str(side2) + " side3 = " + str(side3)

        
def main():
    print("before creating first triangle")
    t=triangle(1,2,3)
    print("after creating fist one")
    t1=triangle(2,2,2)
    print("after creating second one")

main()