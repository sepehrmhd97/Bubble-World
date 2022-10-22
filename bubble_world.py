from tkinter import *
import numpy as np
import random

#constants
ri = 10
w = 600
h = 400
n = 10
speed = 4
delay = 10
bg_color = 'white'

tk = Tk()
tk.title('Bubble World')

canvas = Canvas(tk, width=w, height=h, bg=bg_color)
canvas.pack()


#bubble class
class Bubble():
    def __init__(self, x, y, r, speed):
        self.x = x
        self.y = y
        self.r = r
        self.dx = speed
        self.dy = speed
        
        
    def create(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill='blue' )
        
    def hide(self):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill=bg_color)   
    
    def col_det(self, ball):
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a * a + b * b) ** 0.5 <= self.r + ball.r 
    
    def movement(self):
        #canvas.move(self.bubble,self.dx,self.dy)
        
        #walls collision
        if (self.x + self.r + self.dx >= w) or (self.x - self.r + self.dx <= 0):
            self.dx = -self.dx
        if (self.y + self.r + self.dy >= h) or (self.y - self.r + self.dy <= 0):
            self.dy = -self.dy
            
        #bubbles collision
        
        for bubble in bubble_list:
            if self.col_det(bubble):
                canvas.delete(bubble)
                bubble_list.remove(bubble)
                self.hide()
                r += ri
                self.create()
                
                
def mouse_click(event):
    global player_bubble
        
    if event.num == 1:
        if player_bubble.dy * player_bubble > 0:
            player_bubble.dy = -player_bubble.dy
        else:
            player_bubble.dx = -player_bubble.dx
                
    elif event.num == 3:
        if player_bubble.dy * player_bubble > 0:
            player_bubble.dx = -player_bubble.dx
        else:
            player_bubble.dy = -player_bubble.dy  
        
    #create list of bubbles
def creat_bubble_list(number):
    lst = []
    rax = np.random.uniform(10,600,number)
    ray = np.random.uniform(10,400,number)
    for i in range(0,number):
        next_bubble = Bubble(rax[i], ray[i], ri, speed)
        lst.append(next_bubble)
        next_bubble.create()
    return lst
    
# def main():
#     if 'player_bubble' in globals:
#         player_bubble.movement()
            
#     tk.after(delay, main)
    
# root = tk.Tk()
#     root.title('Bubble World')
#     canvas = tk.Canvas(root, width=w, height=h, bg=bg_color)
#     canvas.pack()
canvas.bind('<Button-1>', mouse_click)
canvas.bind('<Button-2>', mouse_click, '+')
canvas.bind('<Button-3>', mouse_click, '+')      
bubble_list = creat_bubble_list(n)
# main()  
# if 'player_bubble' in globals():  # for restarts
#     del player_bubble      
# bubble = Bubble(100, 300, r, 4)
tk.mainloop()