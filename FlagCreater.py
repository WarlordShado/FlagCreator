import tkinter as tk
from tkinter import ttk
import turtle as turtle
from MakeShape import makeShape as shape

def main():
    
    canvas = turtle.getcanvas()
    turtle.bgcolor("black")
    root = canvas.master
    root.title("Flag Creator")
    
    global Select
    Select = tk.IntVar()

    settings = tk.Frame(root,width = 20,height = 20,padx = 5,pady = 5)
    
    radioFrame = tk.Frame(settings,width = 20, height = 20, padx = 5, pady = 5)
    radioFrame.grid(row = 0, column = 0)
    
    rbtHori = ttk.Radiobutton(radioFrame,text="Horizontal Stripes",value = 1,variable = Select)
    rbtHori.grid(row=0,column=0)
    
    rbtVert = ttk.Radiobutton(radioFrame,text="Vertical Stripes",value = 2,variable = Select)
    rbtVert.grid(row = 1,column = 0)
    
    rbtDia = ttk.Radiobutton(radioFrame,text="Diagonal Stripes",value = 3, variable = Select)
    rbtDia.grid(row = 2, column = 0)
    
    bgFrame = tk.Frame(settings,width=20,height=20,padx= 5,pady = 5)
    bgFrame.grid(row = 0,column = 1)
    
    buttonTitle = tk.Label(bgFrame,text = "Background Settings")
    buttonTitle.grid(row = 0,column = 0,columnspan = 2)
    
    startDrawButton = tk.Button(settings,width = 35,height=3,command = makeFlag,text="Draw Flag!")
    startDrawButton.grid(row = 1,column = 0,padx = 15,pady = 15,columnspan=3)
    
    lblColor = tk.Label(bgFrame,text = "Enter Colors (Seperated by Comma): ")
    lblColor.grid(row = 1,column = 0)

    global ColorText
    ColorText = tk.Text(bgFrame,width = 10,height = 1)
    ColorText.grid(row = 1,column = 1)
    
    lblSegmentAmt = tk.Label(bgFrame,text = "Enter Number of Segments:")
    lblSegmentAmt.grid(row = 2, column = 0)
    
    global SegmentText
    SegmentText = tk.Text(bgFrame,width  = 10, height = 1)
    SegmentText.grid(row = 2, column = 1)

    symbolSettingsFrame = tk.Frame(settings,width = 20,height = 20,padx =5,pady = 5)
    symbolSettingsFrame.grid(row = 0,column = 2)
    
    symbolTitle = tk.Label(symbolSettingsFrame,text = "Symbol Settings")
    symbolTitle.grid(row = 0,column = 0,columnspan = 2)
    
    lblColorSym = tk.Label(symbolSettingsFrame,text = "Enter Symbol Color: ")
    lblColorSym.grid(row = 1,column = 0)
    
    global textSymbolColor
    textSymbolColor = tk.Text(symbolSettingsFrame,width = 10,height = 1)
    textSymbolColor.grid(row = 1,column = 1)
    
    lblPoints = tk.Label(symbolSettingsFrame,text = "Number of Points (If star): ")
    lblPoints.grid(row = 2,column = 0)
    
    global textPoints
    textPoints = tk.Text(symbolSettingsFrame,width = 10,height = 1)
    textPoints.grid(row = 2,column = 1)
    
    global symbolCombo
    symbolCombo = ttk.Combobox(symbolSettingsFrame,width = 20,height=1)
    symbolCombo.grid(row = 3,column = 0,padx = 15,pady = 15,columnspan = 2)
    symbolCombo['values'] = ["Diamond","Circle","Star","None"]

    settings.pack(before = canvas)
    
    turtle.mainloop()
    
def makeFlag():
    turtle.reset()

    makeFlagBg()
    makeFlagSymbol()
    
def makeFlagSymbol():
    shapeSelect = symbolCombo.get()
    
    color = textSymbolColor.get("1.0",tk.END)
    color = color.replace("\n","")
    
    strpoints = textPoints.get("1.0",tk.END)
    strpoints = strpoints.replace("\n","")
    
    if strpoints.isnumeric() and shapeSelect == "Star":
        points = int(strpoints)
    
    
    match(shapeSelect):
        case "Diamond":
            shape.__makeDiamond__(color,250)
        case "Circle":
            shape.__makeCircle__(color,175)
        case "Star":
            shape.__makeStar__(color,50,points)
    
        
def makeFlagBg():
    try:
        style = int(Select.get())
        colorStr = ColorText.get("1.0",tk.END)
        segAmt = SegmentText.get("1.0",tk.END)
    
        colorStr = colorStr.replace("\n","")
        colorStr = colorStr.replace(" ","") #Removes Spaces
        segAmt = segAmt.replace("\n","")    
        
        if segAmt.isnumeric() == False:
            raise Exception("Error: Enter a Number")

        intSegAmt = int(segAmt)
        colors = []
        colors = colorStr.split(",",intSegAmt) #Spliting allows the user to enter as many colors as they want

        turtle.goto((turtle.window_width() / 2) * -1,(turtle.window_height() / 2))
        turtle.speed(200)
        
        if style == 1:
            segmentSize = (turtle.window_height() / intSegAmt)
            straightBg(intSegAmt,colors,style,segmentSize)
        elif style == 2:
            segmentSize = (turtle.window_width() / intSegAmt)
            straightBg(intSegAmt,colors,style,segmentSize)
        else:
            segmentSize = (turtle.window_width() / intSegAmt)
            diagonalBg(intSegAmt,colors,segmentSize)

    except Exception as ex:
        print(ex)
    
def straightBg(intSegAmt,colors,style,segmentSize):
     colorCount = 0
    
     for i in range(intSegAmt):
        turtle.color(colors[colorCount])
            
        colorCount += 1
            
        if colorCount > len(colors) - 1:
            colorCount = 0

        turtle.begin_fill()

        if style == 1:
            for rectSteps in range(2):
                turtle.forward(turtle.window_width())
                turtle.right(90)
                turtle.forward(segmentSize)
                turtle.right(90)
        else:
            for rectSteps in range(2):
                turtle.forward(segmentSize)
                turtle.right(90)
                turtle.forward(turtle.window_width())
                turtle.right(90)
        
        turtle.end_fill()
        turtle.penup()
        if style == 1:
            turtle.right(90)
            turtle.forward(segmentSize)
            turtle.left(90)
        else:
            turtle.forward(segmentSize)
        turtle.pendown()
    
def diagonalBg(intSegmentAmt,colors,segmentSize):
    colorCount = 0

    for offset in range(0,intSegmentAmt * int(segmentSize),int(segmentSize)):
        turtle.color(colors[colorCount])
        colorCount += 1

        if colorCount > len(colors) - 1:
            colorCount = 0
        
        turtle.begin_poly()
        turtle.begin_fill()
        turtle.forward(turtle.window_width() - offset)
        if offset != 0:
            turtle.right(45)
            turtle.forward(offset + 20)
            turtle.right(45)
        else:
            turtle.right(90)
            
        if offset >= turtle.window_height():
            turtle.right(270)
        else:
            turtle.forward(turtle.window_height() - offset)
            turtle.right(90)
            
        turtle.forward(turtle.window_width() - offset)
        turtle.right(90)
        turtle.forward(turtle.window_height() - offset)
        turtle.right(90)
        
        turtle.end_poly()
        turtle.end_fill()
main()
