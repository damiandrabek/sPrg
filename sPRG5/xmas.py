import random
import tkinter

canvasWidth = 600
canvasHeight = 600
canvasColor = "white"
fps = 300
c = tkinter.Canvas(width=canvasWidth, height=canvasHeight, bg=canvasColor)
c.pack()

def draw_circles(x, y, r, color):
  c.create_oval(x-r, y-r, x+r, y+r, fill=color, tags="circle")

def change_color():
  for circle in c.find_withtag("circle"):
    color = random.choice(["red", "green", "blue", "yellow", "orange", "purple", "pink"])
    c.itemconfig(circle, fill=color)

  c.after(int(1000/fps), change_color)

for i in range(30):
  x = random.randint(0, canvasWidth)
  y = random.randint(0, canvasHeight)
  r = random.randint(3, 7)
  color = random.choice(["red", "green", "blue", "yellow", "orange", "purple", "pink"])
  draw_circles(x, y, r, color)

change_color()

tkinter.mainloop()