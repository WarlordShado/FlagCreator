import turtle as t

class makeShape():

    def __makeDiamond__(color,size):

        #positions the Turtle
        t.penup()
        t.goto(0,0)
        t.left(90)
        t.forward(size - 50)
        t.left(135)
        t.pendown()
    
        t.color("black")
        t.pensize(3)
        t.fillcolor(color)
        t.begin_fill()
    
        for i in range(4):
            t.forward(size)
            t.left(90)

        t.end_fill()
        
    def __makeCircle__(color,rad):
        t.color("black")
        t.pensize(3)
    
        #positions the Turtle
        t.penup()
        t.goto(0,0)
        t.right(90)
        t.forward(rad)
        t.left(90)
        t.pendown()
    
        t.fillcolor(color)
        t.begin_fill()
        t.circle(rad)
        t.end_fill()
        
    def __makeStar__(color,size,points):
    
        #positions the Turtle
        t.color("black")
        t.pensize(3)
        t.penup()
        t.goto(0,0)
        t.left(90)
        t.forward(size + 30)
        t.right(90)
        t.forward(size)
        t.pendown()
        
        angle = 360 / points
        t.fillcolor(color)
        t.begin_fill()
        for i in range(points):
            t.forward(size)
            t.right(angle * 2)
            t.forward(size)
            t.left(angle)
            
        t.end_fill()
            