from tkinter.constants import CENTER, TOP
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font

from pathlib import Path
import sys
sys.path.append(".")


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


# from tkinter import *
# Explicit imports to satisfy Flake8


def choose():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_2
    button_2['image'] = button_image_1
    button_3['image'] = button_image_1
    button_4['image'] = button_image_1
    button_5['image'] = button_image_1
    button_6['image'] = button_image_1
    button_7['image'] = button_image_1
    button_1_ = Button(
        text="相\n同\n颜\n色\n选\n取",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="矩\n形\n选\n取",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat",
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)
    button_3_ = Button(
        text="圆\n形\n选\n取",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_3_.place(x=100.0, y=480.0, width=60.0, height=200.0)


def paint():
    from src import pen
    global draw
    pen.Pen(3).bind(draw)
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_1
    button_2['image'] = button_image_2
    button_3['image'] = button_image_1
    button_4['image'] = button_image_1
    button_5['image'] = button_image_1
    button_6['image'] = button_image_1
    button_7['image'] = button_image_1
    button_1_ = Button(
        text="画\n笔\n粗\n细",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="画\n笔\n颜\n色",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)
    button_3_ = Button(
        text="画\n笔\n风\n格",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_3_.place(x=100.0, y=480.0, width=60.0, height=200.0)


def eraser():
    global draw
    from src import eraser
    eraser.Eraser().bind(draw)
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_1
    button_2['image'] = button_image_1
    button_3['image'] = button_image_2
    button_4['image'] = button_image_1
    button_5['image'] = button_image_1
    button_6['image'] = button_image_1
    button_7['image'] = button_image_1
    button_1_ = Button(
        text="橡\n皮\n粗\n细",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="橡\n皮\n形\n状",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)
    button_3_ = Button(
        text="橡\n皮\n效\n果",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_3_.place(x=100.0, y=480.0, width=60.0, height=200.0)


def round():
    global draw
    from src import Shape
    Shape.Shape(3).bind(draw, 4)
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_1
    button_2['image'] = button_image_1
    button_3['image'] = button_image_1
    button_4['image'] = button_image_2
    button_5['image'] = button_image_1
    button_6['image'] = button_image_1
    button_7['image'] = button_image_1
    button_1_ = Button(
        text="线\n条\n粗\n细",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="线\n条\n颜\n色",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)
    button_3_ = Button(
        text="是\n否\n填\n充",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_3_.place(x=100.0, y=480.0, width=60.0, height=200.0)


def round_():
    global draw
    from src import Shape
    Shape.Shape(3).bind(draw, 3)
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_1
    button_2['image'] = button_image_1
    button_3['image'] = button_image_1
    button_4['image'] = button_image_1
    button_5['image'] = button_image_2
    button_6['image'] = button_image_1
    button_7['image'] = button_image_1
    button_1_ = Button(
        text="线\n条\n粗\n细",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="线\n条\n颜\n色",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)
    button_3_ = Button(
        text="是\n否\n填\n充",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_3_.place(x=100.0, y=480.0, width=60.0, height=200.0)


def pick():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_1
    button_2['image'] = button_image_1
    button_3['image'] = button_image_1
    button_4['image'] = button_image_1
    button_5['image'] = button_image_1
    button_6['image'] = button_image_2
    button_7['image'] = button_image_1
    button_1_ = Button(
        text="复\n制\n颜\n色",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="查\n看\n颜\n色",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)


def text():
    global button_1, button_2, button_3, button_4, button_5, button_6, button_7
    button_1['image'] = button_image_1
    button_2['image'] = button_image_1
    button_3['image'] = button_image_1
    button_4['image'] = button_image_1
    button_5['image'] = button_image_1
    button_6['image'] = button_image_1
    button_7['image'] = button_image_2
    button_1_ = Button(
        text="横\n排\n文\n字",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_1_.place(x=100.0, y=40.0, width=60.0, height=200.0)
    button_2_ = Button(
        text="竖\n排\n文\n字",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_2_.place(x=100.0, y=260.0, width=60.0, height=200.0)
    button_3_ = Button(
        text="文\n字\n样\n式",
        bg="#FDF419",
        font=("YeonSung Regular", 26 * -1),
        borderwidth=0,
        highlightthickness=0,
        command=lambda: print("button_1 clicked"),
        relief="flat"
    )
    button_3_.place(x=100.0, y=480.0, width=60.0, height=200.0)


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1440x1024")
window.configure(bg="#E0E0E0")

canvas = Canvas(
    window,
    bg="#E0E0E0",
    height=1024,
    width=1440,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_image_1 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_1 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="选择",
    borderwidth=0,
    highlightthickness=0,
    command=choose,
    relief="flat"
)
button_image_2 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
button_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
button_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
button_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
button_2 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="画笔",
    borderwidth=0,
    highlightthickness=0,
    command=paint,
    relief="flat"
)
button_3 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="橡皮",
    borderwidth=0,
    highlightthickness=0,
    command=eraser,
    relief="flat"
)
button_4 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="圆形",
    borderwidth=0,
    highlightthickness=0,
    command=round,
    relief="flat"
)
button_5 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="矩形",
    borderwidth=0,
    highlightthickness=0,
    command=round_,
    relief="flat"
)
button_6 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="取色",
    borderwidth=0,
    highlightthickness=0,
    command=pick,
    relief="flat"
)
button_7 = Button(
    image=button_image_1,
    font=("YeonSung Regular", 40 * -1),
    compound=CENTER,
    text="文本",
    borderwidth=0,
    highlightthickness=0,
    command=text,
    relief="flat"
)
button_8 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_9 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_10 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_11 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=100.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_2.place(
    x=275.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_3.place(
    x=450.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_4.place(
    x=625.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_5.place(
    x=800.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_6.place(
    x=975.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_7.place(
    x=1150.0,
    y=690.0,
    width=100.0,
    height=100.0
)
button_8.place(
    x=1250.0,
    y=70.0,
    width=100.0,
    height=100.0
)
button_9.place(
    x=1250.0,
    y=230.0,
    width=100.0,
    height=100.0
)
button_10.place(
    x=1250.0,
    y=390.0,
    width=100.0,
    height=100.0
)
button_11.place(
    x=1250.0,
    y=550.0,
    width=100.0,
    height=100.0
)
image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    689.0,
    350.0,
    image=image_image_2
)
draw = Canvas(
    window,
    bg="#FFFFFF",
    height=635,
    width=900,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
draw.place(
    x=239.0,
    y=30.0
)
window.resizable(False, False)
window.mainloop()
