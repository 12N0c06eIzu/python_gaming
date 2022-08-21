import tkinter as tk
import random
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

# 猫ピースの配置
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

# 猫ピースの画像を表示する。
def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

# 猫ピースの落下アルゴリズム
def drop_neko():
    for y in range(8, -1, -1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y + 1][x] == 0:
                neko[y + 1][x] = neko[y][x]
                neko[y][x] = 0

def mouse_move(e):
    m.x = e.x
    m.y = e.y

def mouse_press(e):
    m.c = 1

def game():
    drop_neko()
    # 盤上をマウスカーソルが飛び出てしまわないようにする。
    if 24 <= m.x and m.x < 24+72*8 and 24 <= m.y and m.y < 24+72*10:
        cs.x = int((m.x - 24) / 72)
        cs.y = int((m.y - 24) / 72)
        if m.c == 1:
            m.c = 0
            neko[cs.y][cs.x] = random.randint(1, 6)

    cvs.delete("CURSOR")
    cvs.create_image(cs.x*72+60, cs.y*72+60, image=cursor, tag="CURSOR")
    cvs.delete("NEKO")
    draw_neko()
    root.after(100, game)

# クラスインスタンス生成
m = Mouse()
cs = Cursor("./assets/neko_cursor.png")
window = Window(1000, 800)

# Rootの定義
root = tk.Tk()
root.title("マウス入力")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>", mouse_press)

cvs = tk.Canvas(root, width=window.width, height=window.height)
cvs.pack()

bg = tk.PhotoImage(file="./assets/neko_bg.png")
cursor = tk.PhotoImage(file=cs.icon)

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

cvs.create_image(456, 384, image=bg)

game()
root.mainloop()

