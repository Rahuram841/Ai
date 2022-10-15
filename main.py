from FieldElement import FieldElement
from elliptic_curve import Point
def _print(Point):
    print("X",Point.x)
    print("Y",Point.y)

prime = 223

a = FieldElement(num=0, prime=prime)
b = FieldElement(num=7, prime=prime)
x1 = FieldElement(num=192, prime=prime)
y1 = FieldElement(num=105, prime=prime)
x2 = FieldElement(num=47, prime=prime)
y2 = FieldElement(num=152, prime=prime)
x = FieldElement(num=47, prime=prime)
y=FieldElement(num=71, prime=prime)
p1 = Point(x1, y1, a, b)
p2 = Point(x2, y2, a, b)
p=Point(x,y,a,b)
_print(p1+p2)
result=p
i=11
while i>0:
    result+=p
    print("I:",11-i)
    _print(result)
    i=i-1
