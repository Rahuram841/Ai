from unittest import TestCase, result
from FieldElement import FieldElement

class Point:
    def __init__(self,x,y,a,b):
        self.a=a
        self.b=b
        self.x=x
        self.y=y
        if self.y**2!=self.x**3 + a*x+b:
            raise ValueError('({},{}) is not on the curve'.format(x,y))
    
    def __eq__(self,other):
        return self.x== other.x and self.y == other.y and self.a==other.a and self.b==other.b
    def __add__(self,other):
        if self.a!=other.a or self.b!=other.b:
            raise TypeError('Points {},{} are not on the same curve'.format(self,other))
        if self.x is None:
            return other
        if other.x is None:
            return self
        if self==other and self.y == self.x*0:
            return self.__class__(None,None,self.a,self.b)
        if self==other:
            s=((self.x**2)*3+self.a)*pow(self.y+self.y,-1)
            x=s**2-(self.x+self.x)
            y=s*(self.x-x)-self.y
            return self.__class__(x,y,self.a,self.b)
        slope=(other.y-(self.y))*pow((other.x-(self.x)),-1)
        result_x=(slope**2)-self.x-other.x
        result_y=slope*(self.x-result_x)-self.y
        return self.__class__(result_x,result_y,self.a,self.b)
    def __pow__(self,scalar):
        result=self
        for i in range(scalar):
            result=Point.__add__(self,result)
        return result

   
class ECCTest(TestCase):
    def test_on_curve(self):
        prime=223
        a=FieldElement(0,prime)
        b=FieldElement(7,prime)
        valid_points=((192,105),(17,56),(1,193))
        invalid_points=((200,119),(42,99))
        for x_raw,y_raw in valid_points:
            x=FieldElement(x_raw,prime)
            y=FieldElement(y_raw,prime)
            Point(x,y,a,b)
        for x_raw,y_raw in invalid_points:
            x=FieldElement(x_raw,prime)
            y=FieldElement(y_raw,prime)
            with self.assertRaises(ValueError):
                Point(x,y,a,b)
a=FieldElement(num=0,prime=223)
b=FieldElement(num=7,prime=223)
x1=FieldElement(num=192,prime=223)
y1=FieldElement(num=105,prime=223)
x2=FieldElement(num=17,prime=223)
y2=FieldElement(num=56,prime=223)

p1=Point(x1,y1,a,b)
p2=Point(x2,y2,a,b)
p3=p1+p2




