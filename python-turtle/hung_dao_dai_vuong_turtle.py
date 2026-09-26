"""Minh họa Hưng Đạo Đại Vương Trần Quốc Tuấn bằng Python Turtle.

Đây là hình minh họa cách điệu, không phải chân dung lịch sử.
Chạy: python hung_dao_dai_vuong_turtle.py
"""

import math
import turtle


screen = turtle.Screen()
screen.setup(1000, 740)
screen.title("Hưng Đạo Đại Vương — Trần Quốc Tuấn")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)


def polygon(points, fill, outline=None, border=1):
    """Vẽ đa giác được tô màu."""
    pen.penup()
    pen.goto(points[0])
    pen.pensize(border)
    pen.pencolor(outline or fill)
    pen.fillcolor(fill)
    pen.pendown()
    pen.begin_fill()
    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])
    pen.end_fill()


def oval(cx, cy, rx, ry, color, steps=40):
    """Xấp xỉ hình bầu dục bằng nhiều đoạn thẳng ngắn."""
    polygon([
        (cx + rx * math.cos(2 * math.pi * i / steps),
         cy + ry * math.sin(2 * math.pi * i / steps))
        for i in range(steps)
    ], color)


def line(points, color, width=2):
    pen.penup()
    pen.goto(points[0])
    pen.pencolor(color)
    pen.pensize(width)
    pen.pendown()
    for point in points[1:]:
        pen.goto(point)
    pen.pensize(1)


def write(x, y, message, size, color, style="bold"):
    pen.penup()
    pen.goto(x, y)
    pen.pencolor(color)
    pen.write(message, align="center", font=("Arial", size, style))


# ─── BẦU TRỜI VÀ SÔNG NÚI ───────────────────────────────────────────
for i in range(37):
    t = i / 36
    rgb_bottom = (58, 84, 105)
    rgb_top = (14, 31, 54)
    rgb = tuple(round(a * (1 - t) + b * t)
                for a, b in zip(rgb_bottom, rgb_top))
    color = "#{:02x}{:02x}{:02x}".format(*rgb)
    y = -370 + i * 20
    polygon([(-500, y), (500, y),
             (500, y + 21), (-500, y + 21)], color)

# Mặt trời và những đám mây ở phía xa.
oval(-310, 170, 72, 72, "#BD9664")
oval(-310, 170, 58, 58, "#E9BA77")
for x, y, s in [(-370, 225, 1.0), (320, 205, 0.8)]:
    for dx, dy, rx, ry in [(-30, 0, 37, 11), (0, 10, 46, 16),
                           (43, 0, 42, 11)]:
        oval(x + dx * s, y + dy * s, rx * s, ry * s, "#46617B")

polygon([(-500, -135), (-375, 15), (-300, -105),
         (-165, 55), (-35, -115), (100, 25), (260, -140),
         (370, -12), (500, -145), (500, -370), (-500, -370)],
        "#203D55")
polygon([(-500, -205), (-350, -130), (-205, -212),
         (-42, -112), (100, -200), (250, -120),
         (410, -218), (500, -161), (500, -370), (-500, -370)],
        "#284E59")
polygon([(-500, -270), (500, -270),
         (500, -370), (-500, -370)], "#335C62")

# Sông và các đường gợn sóng.
polygon([(-500, -280), (-310, -272), (-70, -294),
         (120, -279), (320, -301), (500, -290),
         (500, -370), (-500, -370)], "#3B7180")
for x, y, length in [(-390, -314, 85), (-340, -338, 115),
                      (230, -321, 110), (310, -350, 87)]:
    line([(x, y), (x + length, y)], "#79A6A6", 2)

# Hai lá quân kỳ đứng xa phía sau nhân vật.
for x, height, direction in [(-355, 90, 1), (355, 62, -1)]:
    line([(x, -253), (x, height + 55)], "#B2915F", 5)
    polygon([(x, height + 45), (x + direction * 88, height + 21),
             (x + direction * 66, height - 38),
             (x, height - 22)], "#9E3835")
    oval(x, height + 55, 7, 7, "#E2B55D")


# ─── TƯỚNG QUÂN ─────────────────────────────────────────────────────
# Bóng dưới chân và áo choàng đỏ phía sau.
oval(0, -285, 160, 17, "#294B52")
polygon([(-100, 63), (104, 62), (153, -56),
         (225, -275), (100, -251), (22, -178),
         (-78, -252), (-222, -277), (-156, -73)],
        "#9E3434", "#D69D68", 2)
polygon([(-101, 51), (-158, -63), (-204, -266),
         (-159, -244), (-94, -112)], "#BC4B42")
polygon([(103, 50), (157, -63), (207, -264),
         (159, -240), (87, -107)], "#7C292E")

# Hai chân, tấm giáp chân và giày.
polygon([(-71, -138), (-3, -138), (-13, -264),
         (-92, -270)], "#283844")
polygon([(4, -138), (71, -138), (91, -268),
         (13, -265)], "#293C47")
polygon([(-77, -165), (-20, -169), (-22, -245),
         (-86, -247)], "#53606A", "#D5A656", 2)
polygon([(20, -169), (77, -165), (88, -247),
         (22, -245)], "#53606A", "#D5A656", 2)
oval(-63, -271, 49, 15, "#222C33")
oval(63, -271, 49, 15, "#222C33")

# Tay trái đưa ngang; tay phải cầm kiếm.
line([(-85, 36), (-148, 6), (-187, -67)], "#4E5961", 42)
line([(-85, 36), (-148, 6), (-187, -67)], "#B59150", 3)
line([(85, 35), (154, 47), (209, 115)], "#4E5961", 42)
line([(85, 35), (154, 47), (209, 115)], "#B59150", 3)
oval(-187, -68, 19, 22, "#AE784F")

# Vạt áo và giáp thân.
polygon([(-89, 42), (89, 42), (108, -81),
         (77, -175), (-77, -175), (-108, -81)],
        "#333D46", "#D5A452", 3)
polygon([(-64, 17), (64, 17), (77, -105),
         (0, -145), (-77, -105)], "#657078", "#C59B55", 2)
polygon([(-64, 19), (0, 35), (64, 19),
         (47, -24), (0, -44), (-47, -24)],
        "#778088", "#D8B46A", 2)

# Họa tiết trên giáp và đai lưng.
for x in (-45, -22, 22, 45):
    line([(x, -35), (x * 0.8, -93)], "#B9A171", 2)
polygon([(-92, -105), (92, -105), (89, -132),
         (-89, -132)], "#443C39", "#D6AA5E", 2)
oval(0, -119, 24, 24, "#D8AB57")
oval(0, -119, 15, 15, "#7B4935")
polygon([(0, -136), (7, -119), (0, -106),
         (-7, -119)], "#E7C77D")

# Miếng giáp vai rộng và găng tay.
polygon([(-103, 72), (-154, 51), (-144, -2),
         (-90, 11), (-68, 49)], "#5D6266", "#DCAD64", 3)
polygon([(103, 72), (154, 51), (144, -2),
         (90, 11), (68, 49)], "#5D6266", "#DCAD64", 3)
for x in (-114, 114):
    oval(x, 40, 10, 10, "#D8A95E")

# Cổ áo và khuôn mặt.
polygon([(-35, 62), (35, 62), (28, 98),
         (-28, 98)], "#AA734E")
oval(0, 123, 53, 69, "#B98962")
oval(-52, 118, 9, 17, "#A56F50")
oval(52, 118, 9, 17, "#A56F50")

# Mắt, lông mày và mũi tạo nét mặt nghiêm nghị.
line([(-39, 145), (-18, 151), (-8, 146)], "#2C2928", 5)
line([(8, 146), (18, 151), (39, 145)], "#2C2928", 5)
line([(-34, 131), (-23, 129), (-13, 131)], "#2B2624", 3)
line([(13, 131), (23, 129), (34, 131)], "#2B2624", 3)
pen.penup()
for x in (-23, 23):
    pen.goto(x, 130)
    pen.dot(5, "#1F2020")
line([(0, 125), (-5, 110), (2, 107)], "#8F654D", 2)

# Râu mép và râu dài: đặc điểm nổi bật của bức minh họa.
polygon([(-6, 102), (-18, 106), (-46, 94),
         (-31, 84), (-11, 90), (0, 83)], "#25282A")
polygon([(6, 102), (18, 106), (46, 94),
         (31, 84), (11, 90), (0, 83)], "#25282A")
polygon([(-31, 78), (-15, 68), (0, 71), (15, 68),
         (31, 78), (24, 25), (7, 2), (0, -5),
         (-9, 7), (-25, 33)], "#272A2B")
line([(-12, 62), (-10, 26), (-5, 8)], "#525253", 2)
line([(10, 59), (13, 29), (7, 8)], "#525253", 2)

# Mũ chiến với hai vành bảo vệ hai bên khuôn mặt.
polygon([(-55, 161), (-46, 199), (-28, 218),
         (0, 233), (28, 218), (46, 199), (55, 161),
         (32, 170), (0, 177), (-32, 170)],
        "#41494C", "#E1B869", 3)
polygon([(-57, 163), (-67, 126), (-58, 69),
         (-43, 82), (-45, 151)], "#4A4D4D", "#CDA55F", 2)
polygon([(57, 163), (67, 126), (58, 69),
         (43, 82), (45, 151)], "#4A4D4D", "#CDA55F", 2)
polygon([(0, 226), (13, 204), (10, 173),
         (0, 165), (-10, 173), (-13, 204)], "#D8AD5C")
oval(0, 194, 6, 8, "#7D4435")

# Chùm lông đỏ trên đỉnh mũ.
polygon([(0, 232), (-16, 270), (-66, 294),
         (-101, 281), (-64, 278), (-24, 254),
         (-8, 229)], "#BD4B3A")
polygon([(0, 232), (12, 273), (4, 295),
         (25, 273), (13, 236)], "#8F3532")

# Kiếm ở tay phải: cán, chắn tay và lưỡi kiếm hướng lên.
polygon([(195, 98), (215, 119), (232, 107),
         (211, 86)], "#B98449", "#E4BC69", 2)
line([(188, 105), (240, 150)], "#DBAE56", 10)
line([(208, 91), (238, 122)], "#EAC671", 9)
polygon([(230, 145), (254, 157), (341, 298),
         (327, 304), (239, 177)], "#DDE4E7", "#8EA7AD", 2)
line([(245, 164), (330, 292)], "#FFFFFF", 2)
oval(202, 105, 18, 20, "#A9714D")

# Lớp sương dưới chân tạo chiều sâu.
for x, y, rx in [(-248, -295, 110), (215, -295, 128)]:
    oval(x, y, rx, 13, "#5A8990")

write(0, 314, "HƯNG ĐẠO ĐẠI VƯƠNG", 26, "#F5D48C")
write(0, -341, "TRẦN QUỐC TUẤN", 18, "#E6C694")

screen.update()
turtle.done()
