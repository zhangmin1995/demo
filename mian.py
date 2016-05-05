

#利用面向对象的继承机制定义椭圆（ellipse），正方形（square），矩形（rectangle），圆形（Circle）等类
#设计一个函数compute-area（shapes）;输入一个图形列表，输出这些图形的面积之和


class Shape(object): 
    @property
    def area(self):
        pass
 
         

class Ellipse(Shape):
    def __init__(self, long=0, short=0):
        super().__init__()
        self.long = long
        self.short = short
         
    @property
    def area(self):
        return 3.14159*self.long * self.short 
         
         
class Circle(Ellipse):
    def __init__(self, r=0):
        super().__init__(r, r)


class Rectangle(Shape):
    def __init__(self, wide=0, long=0):
        super().__init__()
        self.wide = wide
        self.long = long
         
    @property
    def area(self):
        return self.wide * self.long
         
         
class Square(Rectangle):
    def __init__(self, side=0):
        super().__init__(side, side)
         
         
def compute_area(lists):
    areas = [x.area for x in lists]
    return sum(areas)

shapes = [Ellipse(10,20), Square(15), Circle(5), Rectangle(20,15), Circle(5), Square(15), Ellipse(10,20)]
total_area=compute_area(shapes)
print('total_area: ', total_area)
