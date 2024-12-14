import tkinter

with open("transport.txt", "r") as file:
    lines = file.readlines()

stops = [line.strip() for line in lines]


canvasWidth = 800
canvasHeight = 800
canvasColor = "white"

c = tkinter.Canvas(width=canvasWidth, height=canvasHeight, bg=canvasColor)
c.pack()

stopSize = 15
circleColor = "green"
rectangleColor = "blue"


def drawRectangle(x, y, size, color):
    c.create_rectangle(x - size, y - size, x + size, y + size, fill=color, outline="")


def drawCircle(x, y, size, color):
    c.create_oval(x - size, y - size, x + size, y + size, fill=color, outline="black")


def drawText(x, y, color, text):
    c.create_text(x, y, font="Helvetica 10", fill=color, text=text, angle=35)


lineY = canvasHeight / 2


def draw():
    # Draw title
    c.create_text(canvasWidth / 2, canvasHeight / 4, font="Helvetica 40", fill="red", text="MHD Bratislava")

    # Calculate line start and end points dynamically
    startX = canvasWidth / 6
    step = 50
    endX = startX + (len(stops) - 1) * step


    c.create_line(startX, lineY, endX, lineY, fill="black")


    for i, stop in enumerate(stops):
        x = startX + i * step  
        cColor = "white" if "*" in stop else circleColor

        if i == 0:  
            drawRectangle(x, lineY, stopSize, rectangleColor)
        elif i == len(stops) - 1:
            drawRectangle(x, lineY, stopSize, rectangleColor)
        else:
            drawCircle(x, lineY, stopSize, cColor)

        # Draw the stop name
        drawText(x, lineY - 40, "black", stop.replace("*", ""))


draw()

tkinter.mainloop()
