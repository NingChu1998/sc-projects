"""
File: 
Name: Grogu
----------------------
TODO:

"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GRoundRect, GLine, GArc
from campy.graphics.gwindow import GWindow
from campy.graphics.gtypes import GPoint

window = GWindow(width=800, height=800, title='Grogu')


def main():
    """
    TODO
    The reason why I want to draw Grogu is because it just soo cute that I can't help myself.
    But the most interesting thing is that before Grogu, I never obsessed with any character.
    """
    background()
    ear()
    face()
    eye()
    neck()
    body()
    hand()
    text()



def background():
    back = GRect(800, 800)
    back.filled = True
    back.fill_color = 'skyblue'
    back.color = 'skyblue'
    window.add(back)




def ear():
    l_ear1 = GRect(190, 26, x=(window.width - 240) / 2 + 150, y=(window.height - 160) / 3 + 30)
    l_ear1.filled = True
    l_ear1.fill_color = 'pink'
    l_ear1.color = 'pink'
    window.add(l_ear1)
    r_ear1 = GRect(190, 26, x=(window.width - 240) / 2 - 100, y=(window.height - 160) / 3 + 30)
    r_ear1.filled = True
    r_ear1.fill_color = 'pink'
    r_ear1.color = 'pink'
    window.add(r_ear1)
    l_ear2 = GRect(180, 10, x=(window.width - 240) / 2 + 160, y=(window.height - 160) / 3 + 50)
    l_ear2.filled = True
    l_ear2.fill_color = 'green'
    l_ear2.color = 'green'
    window.add(l_ear2)
    r_ear2 = GRect(180, 10, x=(window.width - 240) / 2 - 100, y=(window.height - 160) / 3 + 50)
    r_ear2.filled = True
    r_ear2.fill_color = 'green'
    r_ear2.color = 'green'
    window.add(r_ear2)
    left_ear = GRect(200, 16, x=(window.width - 240) / 2 + 150, y=(window.height - 160) / 3 + 20)
    left_ear.filled = True
    left_ear.fill_color = 'green'
    left_ear.color = 'green'
    window.add(left_ear)
    r_ear = GRect(200, 16, x=(window.width - 240) / 2 - 110, y=(window.height - 160) / 3 + 20)
    r_ear.filled = True
    r_ear.fill_color = 'green'
    r_ear.color = 'green'
    window.add(r_ear)

def eye():
    l_eye = GOval(80, 55, x=(window.width - 240) / 2 + 135, y=(window.height - 160) / 3 + 40)
    l_eye.filled = True
    window.add(l_eye)
    r_eye = GOval(80, 55, x=(window.width - 240) / 2 + 35, y=(window.height - 160) / 3 + 40)
    r_eye.filled = True
    window.add(r_eye)
    l_eye_w = GOval(16, 11, x=(window.width - 240) / 2 + 150, y=(window.height - 160) / 3 + 55)
    l_eye_w.filled = True
    l_eye_w.fill_color = 'white'
    window.add(l_eye_w)
    r_eye_w = GOval(16, 11, x=(window.width - 240) / 2 + 50, y=(window.height - 160) / 3 + 55)
    r_eye_w.filled = True
    r_eye_w.fill_color = 'white'
    window.add(r_eye_w)

def face():
    face = GOval(240, 160, x=(window.width - 240) / 2, y=(window.height - 160) / 3)
    face.filled = True
    face.color = 'green'
    face.fill_color = 'green'
    window.add(face)

def neck():
    neck = GRoundRect(240, 50, x=(window.width - 240) / 2, y=(window.height - 160) / 3 + 110, corner=50)
    neck.filled = True
    neck.fill_color = 'sandybrown'
    neck.color = 'sandybrown'
    window.add(neck)

def body():
    body = GRoundRect(220, 100, x=(window.width - 240) / 2 + 10, y=(window.height - 160) / 3 + 160, corner=50)
    body.filled = True
    body.fill_color = 'sandybrown'
    body.color = 'sandybrown'
    window.add(body)


def hand():
    s_hand = GOval(370, 30, x=(window.width - 240) / 2 - 65, y=(window.height - 160) / 3 + 140)
    s_hand.filled = True
    s_hand.fill_color = 'green'
    s_hand.color = 'green'
    window.add(s_hand)
    hand =GRoundRect(320, 60, x=(window.width - 240) / 2 - 40, y=(window.height - 160) / 3 + 140, corner=50)
    hand.filled = True
    hand.fill_color = 'sandybrown'
    hand.color = 'sandybrown'
    window.add(hand)

def text():
    text_label = GLabel("Grogu wishes you a wonderful week!", x=50, y=50)
    text_label.font = 'Courier-30-Bold'
    text_label.text = 'Grogu wishes you a wonderful week!'
    window.add(text_label, 90, 600)


"""def polygon():
    point = GPoint(100, 100)
    pointt = GPoint(200, 100)
    pointtt = GPoint(90, 400)
    pointttt = GPoint(210, 400)
    tttshape = GPolygon()
    tttshape.add_vertex(point)
    tttshape.add_vertex(pointt)
    tttshape.add_vertex(pointttt)
    tttshape.add_vertex(pointtt)
    window.add(tttshape)"""


if __name__ == '__main__':
    main()
