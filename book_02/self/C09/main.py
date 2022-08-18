import tkinter as tk

# import os
# print(os.getcwd())

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Cursor():
    def __init__(self, icon):
        self.icon = icon
        self.x = 0
        self.y = 0

class Mouse():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.c = 0

def mouse_move(e):
    m.x = e.x
    m.y = e.y

def game():
    if 24 <= m.y and m.y < 24+72*8 and 24 <= m.y and m.y < 24+72*10:
        cursor.x = int((m.x - 24) / 72)
        cursor.y = int((m.y - 24) / 72)
    cvs.delete("CURSOR")
    cvs.create_image(cs.x*72+60, cs.y*72+60, image=cursor, tag="CURSOR")
    root.after(100, game)


m = Mouse()
cs = Cursor("./assets/neko_cursor.png")

root = tk.Tk()
root.title("マウス入力")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)

window = Window(1000, 800)

cvs = tk.Canvas(root, width=window.width, height=window.height)
cvs.pack()

bg = tk.PhotoImage(file="./assets/neko_bg.png")
cursor = tk.PhotoImage(file=cs.icon)
cvs.create_image(456, 384, image=bg)

game()
root.mainloop()

