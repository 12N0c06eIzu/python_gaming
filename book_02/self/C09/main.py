from email.mime import image
import tkinter as tk

# import os
# print(os.getcwd())

neko = [
    [1, 0, 0, 0, 0, 0, 7, 7],
    [0, 2, 0, 0, 0, 0, 7, 7],
    [0, 0, 3, 0, 0, 0, 7, 7],
    [0, 0, 0, 4, 0, 0, 7, 7],
    [0, 0, 0, 0, 5, 0, 7, 7],
    [0, 0, 0, 0, 0, 6, 7, 7],
    [0, 0, 0, 0, 0, 0, 7, 7],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 3, 4, 5, 6],
]

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]])

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
    # 盤上をマウスカーソルが飛び出てしまわないようにする。
    if 24 <= m.x and m.x < 24+72*8 and 24 <= m.y and m.y < 24+72*10:
        cs.x = int((m.x - 24) / 72)
        cs.y = int((m.y - 24) / 72)
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

img_neko = [
    None,
    tk.PhotoImage(file="./peace/1.png"),
    tk.PhotoImage(file="./peace/2.png"),
    tk.PhotoImage(file="./peace/3.png"),
    tk.PhotoImage(file="./peace/4.png"),
    tk.PhotoImage(file="./peace/5.png"),
    tk.PhotoImage(file="./peace/6.png"),
    tk.PhotoImage(file="./assets/neko_niku.png"),
]

draw_neko()

game()
root.mainloop()

