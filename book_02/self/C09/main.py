import tkinter as tk
import random

class Window():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.index = 0
        self.timer = 0
        self.score = 0
        self.tsugi = 0

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
neko = []
check = []
for i in range(10):
    neko.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])

# 猫ピースの画像を表示する。
def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image=img_neko[neko[y][x]], tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]

    for y in range(1, 9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y - 1][x] == check[y][x] and check[y + 1][x] == check[y][x]:
                    neko[y - 1][x] = 7
                    neko[y][x] = 7
                    neko[y + 1][x] = 7

    for y in range(10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    neko[y][x - 1] = 7
                    neko[y][x] = 7
                    neko[y][x + 1] = 7

        for y in range(1, 9):
            for x in range(1, 7):
                if check[y][x] > 0:
                    if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                        neko[y - 1][x - 1] = 7
                        neko[y][x] = 7
                        neko[y + 1][x + 1] = 7
                    if check[y + 1][x - 1] == check[y][x] and check[y -1 ][x + 1] == check[y][x]:
                        neko[y + 1][x - 1] = 7
                        neko[y][x] = 7
                        neko[y - 1][x + 1] = 7

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
    # 風船押したら判定する。
    if 660 <= m.x and m.y < 840 and 100 <= m.y and m.y < 160 and m.c == 1:
        m.c = 0
        check_neko()
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

# 猫のイメージを保存する。
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
cvs.create_rectangle(660, 100, 840, 160, fill="white")
cvs.create_text(750, 130, text="テスト", fill="red", font=("Times New Roman", 30))

game()
root.mainloop()

