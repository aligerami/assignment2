import math
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

class Triangle(GeometricObject):
   
    def __init__(self,side1=1.0,side2=1.0,side3=1.0):
        self.__side1=side1
        self.__side2=side2
        self.__side3=side3
    
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
    s1=float(input("Enter first Side of Triangle: "))
    s2=float(input("Enter second Side of Triangle: "))
    s3=float(input("Enter third Side of Triangle: "))
    
    color=input("Enter color of Triangle: ")
    filled=int(input("Enter 1 if Triangle is filled and 0 if it's not: "))
    t=Triangle(s1,s2,s3)
    t.set_color(color)
    t.set_filled(filled==1)
    print("filled==1 is ",filled==1)
    print("Triangle area is ",t.get_area())
    print("Triangle perimeter is ",t.get_perimeter())
    print("Triangle color is ",t.get_color())
    print("Triangle filled =", "True" if(t.is_filled()==1) else "False")
main()

        