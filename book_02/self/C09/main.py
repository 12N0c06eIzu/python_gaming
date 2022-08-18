import tkinter

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

m = Mouse()
icon = "./assets/neko_cursor.png"
cs = Cursor(icon)

def game():
    if 24 <= m.y and m.y < 24+72*8 and 24 <= m.y and m.y < 24+72*10:
        cursor.x = int((m.x - 24) / 72)
        cursor.y = int((m.y - 24) / 72)
    fnt = ("Times New Roman", 30)
    txt = "mouse({}, {}, {})".format(m.x, m.y, m.c)
    cvs.delete("TEST")
    cvs.create_text(456, 384, text=txt, fill="black", font=fnt, tag="TEST")
    root.after(100, game)

root = tkinter.Tk()
root.title("マウス入力")
root.resizable(False, False)

wd = 1000
hg = 800
cvs = tkinter.Canvas(root, width=wd, height=hg)
cvs.pack()

bg = tkinter.PhotoImage(file="./assets/neko_bg.png")
cursor = tkinter.PhotoImage(cs.icon)


game()
root.mainloop()

