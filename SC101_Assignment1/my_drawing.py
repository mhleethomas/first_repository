"""
File: my_drawing.py
Name: Ming-Hsiang (Thomas), Lee
----------------------
1. this file draws
"""

from campy.graphics.gobjects import GOval, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: routemap2023.png
    This is a simplified route map of Taipei Metro.
    The title is stolen from Taipei Rapid Transit Corporation
    It is colorful.
    There are lines. (acyually polygons)
    After drawing the map, I thought, why not highlight stanCode and give it a five-star rating?
    So, there it is.
    """
    window = GWindow(width=480, height=640, title="routemap2023.png")

    red = GPolygon()
    red.add_vertex((80, 40))  # A
    red.add_vertex((80, 130))  # B
    red.add_vertex((200, 130))  # C
    red.add_vertex((200, 410))  # D
    red.add_vertex((380, 410))  # E

    red.add_vertex((380, 405))  # e
    red.add_vertex((205, 405))  # d
    red.add_vertex((205, 125))  # c
    red.add_vertex((85, 125))  # b
    red.add_vertex((85, 40))  # a

    blue = GPolygon()
    blue.add_vertex((100, 580))  # A
    blue.add_vertex((100, 370))  # B
    blue.add_vertex((450, 370))  # C
    blue.add_vertex((450, 300))  # D

    blue.add_vertex((455, 300))  # d
    blue.add_vertex((455, 375))  # c
    blue.add_vertex((105, 375))  # b
    blue.add_vertex((105, 580))  # a

    brown = GPolygon()
    brown.add_vertex((450, 300))  # A
    brown.add_vertex((450, 230))  # B
    brown.add_vertex((290, 230))  # C
    brown.add_vertex((290, 450))  # D
    brown.add_vertex((360, 450))  # E
    brown.add_vertex((360, 520))  # F
    brown.add_vertex((410, 520))  # G

    brown.add_vertex((410, 525))  # g
    brown.add_vertex((355, 525))  # f
    brown.add_vertex((355, 455))  # e
    brown.add_vertex((285, 455))  # d
    brown.add_vertex((285, 225))  # c
    brown.add_vertex((455, 225))  # b
    brown.add_vertex((455, 300))  # a

    green = GPolygon()
    green.add_vertex((310, 610))  # A
    green.add_vertex((310, 530))  # B
    green.add_vertex((200, 410))  # C
    green.add_vertex((160, 410))  # D
    green.add_vertex((160, 330))  # E
    green.add_vertex((380, 330))  # F

    green.add_vertex((380, 335))  # F
    green.add_vertex((165, 335))  # E
    green.add_vertex((165, 405))  # D
    green.add_vertex((205, 405))  # C
    green.add_vertex((315, 525))  # B
    green.add_vertex((315, 610))  # A

    orange = GPolygon()
    orange.add_vertex((210, 540))  # A
    orange.add_vertex((210, 450))  # B
    orange.add_vertex((250, 410))  # C
    orange.add_vertex((250, 278))  # D
    orange.add_vertex((142, 278))  # EEE
    orange.add_vertex((30, 400))  # F
    orange.add_vertex((30, 470))  # G

    orange.add_vertex((25, 470))  # g
    orange.add_vertex((25, 395))  # f
    orange.add_vertex((135, 275))  # HHH
    orange.add_vertex((100, 240))  # I
    orange.add_vertex((100, 180))  # J

    orange.add_vertex((105, 180))  # j
    orange.add_vertex((105, 235))  # i
    orange.add_vertex((142, 272))  # KKK
    orange.add_vertex((255, 272))  # d
    orange.add_vertex((255, 415))  # c
    orange.add_vertex((215, 455))  # b
    orange.add_vertex((215, 540))  # a

    yellow = GPolygon()
    yellow.add_vertex((30, 330))  # A
    yellow.add_vertex((30, 360))  # B
    yellow.add_vertex((180, 510))  # C
    yellow.add_vertex((240, 510))  # D
    yellow.add_vertex((270, 530))  # E
    yellow.add_vertex((310, 530))  # F

    yellow.add_vertex((310, 525))  # f
    yellow.add_vertex((275, 525))  # e
    yellow.add_vertex((245, 505))  # d
    yellow.add_vertex((185, 505))  # c
    yellow.add_vertex((35, 355))  # b
    yellow.add_vertex((35, 330))  # a

    pink = GPolygon()
    pink.add_vertex((130, 100))  # A
    pink.add_vertex((130, 130))  # B

    pink.add_vertex((125, 130))  # b
    pink.add_vertex((125, 100))  # a

    lime = GPolygon()
    lime.add_vertex((280, 560))  # A
    lime.add_vertex((310, 560))  # B

    lime.add_vertex((310, 565))  # b
    lime.add_vertex((280, 565))  # a

    landmark_p = GPolygon()
    landmark_p.add_vertex((288, 405))  # tip
    landmark_p.add_vertex((298, 390))
    landmark_p.add_vertex((278, 390))

    landmark_o1 = GOval(20, 20, x=278, y=378)  # outer
    landmark_o2 = GOval(10, 10, x=283, y=383)  # inner

    landmark_label = GLabel("stanCode\n  * * * * *", x=257, y=378)
    landmark_label.font = "Helvetica-12"

    "###############################"

    lime.filled = True
    lime.fill_color = "yellowgreen"
    lime.color = "yellowgreen"
    window.add(lime)

    pink.filled = True
    pink.fill_color = "pink"
    pink.color = "pink"
    window.add(pink)

    yellow.filled = True
    yellow.fill_color = "yellow"
    yellow.color = "yellow"
    window.add(yellow)

    red.filled = True
    red.fill_color = "crimson"
    red.color = "crimson"
    window.add(red)

    blue.filled = True
    blue.fill_color = "royalblue"
    blue.color = "royalblue"
    window.add(blue)

    brown.filled = True
    brown.fill_color = "darkgoldenrod"
    brown.color = "darkgoldenrod"
    window.add(brown)

    green.filled = True
    green.fill_color = "green"
    green.color = "green"
    window.add(green)

    orange.filled = True
    orange.fill_color = "orange"
    orange.color = "orange"
    window.add(orange)

    landmark_p.filled = True
    landmark_p.fill_color = "red"
    landmark_p.color = "red"
    window.add(landmark_p)

    landmark_o1.filled = True
    landmark_o1.fill_color = "red"
    landmark_o1.color = "red"
    window.add(landmark_o1)

    landmark_o2.filled = True
    landmark_o2.fill_color = "black"
    landmark_o2.color = "black"
    window.add(landmark_o2)

    window.add(landmark_label)


if __name__ == '__main__':
    main()
