#  Write a Python class named Rectangle constructed by a length and
# width and a method which will compute the area of a rectangle

'''class rectangle:
    height= 0
    width:0 
    
    
    

    def get_data(self):
        self.height = input("Enter  rengtangle height")
        self.width= input("Enter  rengtangle  width")
       
    def print_data(self):
        print("Rectangle height",self.height)
        print("Recnagle width",self.width)
        
        
        
    
rt =rectangle()
rt.get_data()
rt.print_data()

       '''
class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(30, 20)
print("Recnatgle area ",newRectangle.rectangle_area())

