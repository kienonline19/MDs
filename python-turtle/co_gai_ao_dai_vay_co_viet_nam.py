"""Thiếu nữ áo dài vẫy cờ Việt Nam — chạy bằng Python Turtle."""

import math
import random
import turtle


screen = turtle.Screen()
screen.setup(960, 700)
screen.title("Thiếu nữ áo dài vẫy cờ Việt Nam")
screen.tracer(0)

scenery = turtle.Turtle(visible=False)
scenery.speed(0)
pen = turtle.Turtle(visible=False)
pen.speed(0)


def shape(t, points, color, outline=None):
    """Vẽ và tô một đa giác theo danh sách tọa độ."""
    t.penup()
    t.goto(points[0])
    t.pencolor(outline or color)
    t.fillcolor(color)
    t.pendown()
    t.begin_fill()
    for point in points[1:]:
        t.goto(point)
    t.goto(points[0])
    t.end_fill()


def ellipse(t, cx, cy, rx, ry, color, steps=32):
    points = [
        (cx + rx * math.cos(2 * math.pi * i / steps),
         cy + ry * math.sin(2 * math.pi * i / steps))
        for i in range(steps)
    ]
    shape(t, points, color)


def line(t, points, color, width=2):
    t.penup()
    t.goto(points[0])
    t.pencolor(color)
    t.pensize(width)
    t.pendown()
    for point in points[1:]:
        t.goto(point)
    t.pensize(1)


def background():
    # Bầu trời chuyển nhẹ từ xanh sang kem.
    for i in range(28):
        y = -350 + i * 25
        r = 244 - i // 3
        g = 248 - i // 4
        b = 235 + i // 3
        color = f"#{r:02x}{g:02x}{b:02x}"
        shape(scenery, [(-480, y), (480, y), (480, y + 26), (-480, y + 26)], color)

    # Những dải đồi tạo chiều sâu.
    shape(scenery, [(-480, -160), (-330, -110), (-170, -158),
                    (40, -105), (220, -160), (480, -120),
                    (480, -350), (-480, -350)], "#B9DCC6")
    shape(scenery, [(-480, -214), (-260, -178), (-80, -225),
                    (135, -175), (310, -220), (480, -190),
                    (480, -350), (-480, -350)], "#8FC9AD")
    shape(scenery, [(-480, -275), (480, -275),
                    (480, -350), (-480, -350)], "#78B797")

    # Mây mềm ở góc trên; tránh che nhân vật và lá cờ.
    for x, y, size in [(-355, 210, 1), (310, 222, 0.8)]:
        for dx, dy, rx, ry in [(-32, 0, 38, 17), (0, 10, 45, 23),
                               (38, 0, 39, 17)]:
            ellipse(scenery, x + dx * size, y + dy * size,
                    rx * size, ry * size, "#FFFFFF")

    # Hoa giấy phía xa.
    random.seed(12)
    for _ in range(32):
        x = random.randint(-440, 440)
        y = random.randint(-220, 310)
        if -215 < x < 255 and -130 < y < 300:
            continue
        scenery.penup()
        scenery.goto(x, y)
        scenery.dot(random.choice([4, 5, 6]),
                    random.choice(["#FFD166", "#FF8FAB", "#FFFFFF"]))

    scenery.penup()
    scenery.goto(0, -317)
    scenery.pencolor("#FFFFFF")
    scenery.write("VIỆT NAM TRONG TIM TÔI", align="center",
                  font=("Arial", 20, "bold"))


background()
phase = 0.0


def draw_person(sway):
    # Tóc phía sau người: lọn tóc dài ôm vai.
    shape(pen, [(-179, 111), (-190, 35), (-197, -87),
                (-164, -99), (-143, -45), (-113, -55),
                (-79, -94), (-68, 20), (-84, 136)], "#242431")
    ellipse(pen, -133, 106, 58, 75, "#242431")

    # Quần trắng xanh và giày ở dưới tà áo dài.
    shape(pen, [(-153, -90), (-123, -90), (-126, -245),
                (-140, -269), (-167, -269), (-161, -213)], "#D8EAF0")
    shape(pen, [(-120, -90), (-101, -90), (-91, -269),
                (-116, -269), (-128, -229)], "#EAF6F7")
    ellipse(pen, -164, -270, 19, 7, "#425368")
    ellipse(pen, -98, -270, 18, 7, "#425368")

    # Cánh tay trái buông nhẹ, cánh tay phải đưa lên vẫy cờ.
    line(pen, [(-166, 11), (-198, -30)], "#FFFFFF", 25)
    line(pen, [(-198, -30), (-205, -53)], "#F3C3A4", 12)
    ellipse(pen, -205, -56, 8, 10, "#F3C3A4")

    hand_x = 10 + 17 * math.sin(phase)
    hand_y = 90 + 9 * math.sin(phase)
    line(pen, [(-96, 8), (-53, 34)], "#FFFFFF", 27)
    line(pen, [(-53, 34), (hand_x, hand_y)], "#F3C3A4", 13)

    # Hai tà áo dài bay nhè nhẹ, có khoảng mở để thấy quần.
    shape(pen, [(-158, -73), (-181, -117), (-193, -190),
                (-221 + sway, -257), (-186 + sway, -268),
                (-147, -206), (-123, -98)], "#F8FCF9")
    shape(pen, [(-110, -75), (-86, -118), (-70, -187),
                (-47 + sway, -258), (-84 + sway, -267),
                (-116, -208), (-141, -99)], "#E8F4F4")
    line(pen, [(-158, -82), (-167, -157),
               (-188 + sway, -246)], "#C7E2E4", 2)
    line(pen, [(-106, -83), (-89, -161),
               (-75 + sway, -246)], "#C7E2E4", 2)

    # Thân áo, cổ áo kín và các cúc nhỏ.
    shape(pen, [(-170, 26), (-96, 26), (-104, -80),
                (-126, -101), (-153, -80)], "#FFFFFF")
    shape(pen, [(-145, 32), (-115, 32), (-113, 18),
                (-147, 18)], "#E9F5F4")
    line(pen, [(-126, 17), (-126, -78)], "#D7ECEB", 2)
    for y in (4, -13, -30, -47):
        pen.penup()
        pen.goto(-120, y)
        pen.dot(4, "#82B8B2")

    # Cổ, tai, khuôn mặt; tóc phía trước được vẽ sau khuôn mặt.
    shape(pen, [(-143, 37), (-118, 37), (-120, 57),
                (-141, 57)], "#F3C3A4")
    ellipse(pen, -89, 99, 9, 15, "#EAB397")
    ellipse(pen, -132, 107, 40, 53, "#F6CDAE")
    ellipse(pen, -151, 100, 4, 5, "#F2A9A1")
    ellipse(pen, -105, 100, 4, 5, "#F2A9A1")

    # Mái tóc ôm trán và hai lọn tóc buông xuống.
    shape(pen, [(-173, 126), (-170, 153), (-151, 172),
                (-125, 173), (-102, 160), (-91, 134),
                (-111, 142), (-130, 148), (-148, 137)], "#242431")
    shape(pen, [(-169, 139), (-175, 109), (-164, 53),
                (-155, 52), (-160, 119)], "#242431")
    shape(pen, [(-94, 134), (-87, 113), (-93, 56),
                (-103, 54), (-101, 114)], "#242431")

    # Bông hoa nhỏ cài trên mái tóc.
    for i in range(5):
        angle = 2 * math.pi * i / 5
        ellipse(pen, -165 + 8 * math.cos(angle),
                146 + 8 * math.sin(angle), 5, 5, "#FFF4F0", 14)
    ellipse(pen, -165, 146, 4, 4, "#E9AC63", 14)

    # Mắt sáng, lông mày và nụ cười.
    line(pen, [(-151, 113), (-140, 116)], "#55403C", 2)
    line(pen, [(-122, 116), (-111, 113)], "#55403C", 2)
    ellipse(pen, -145, 108, 2.6, 4, "#313348")
    ellipse(pen, -116, 108, 2.6, 4, "#313348")
    line(pen, [(-142, 84), (-136, 80), (-129, 78),
               (-121, 80), (-116, 85)], "#C7686B", 2.5)

    return hand_x, hand_y


def draw_flag(hand_x, hand_y):
    # Cờ Việt Nam có tỉ lệ hình chữ nhật 3:2.
    width, height = 210, 140
    left = hand_x
    bottom = hand_y + 40

    def point(u, v):
        # Mép cạnh cột đứng yên; phía ngoài gợn sóng nhiều hơn.
        ripple = 10 * (u / width) * math.sin(u / 29 - phase * 2)
        return left + u, bottom + v + ripple

    # Cán cờ đặt sau mặt cờ.
    line(pen, [(hand_x, hand_y - 8),
               (hand_x, bottom + height + 10)], "#83624C", 7)
    ellipse(pen, hand_x, bottom + height + 11, 5, 5, "#D6AC5F")

    # Những dải đỏ liền nhau mô phỏng bề mặt vải uốn lượn.
    count = 21
    for i in range(count):
        u1 = i * width / count
        u2 = (i + 1) * width / count
        red = "#DA251D" if i % 4 else "#DD2921"
        shape(pen, [point(u1, 0), point(u2, 0),
                    point(u2, height), point(u1, height)], red)

    # Ngôi sao vàng năm cánh, cùng biến dạng theo mặt cờ.
    cx, cy = width / 2, height / 2
    star = []
    for i in range(10):
        angle = math.radians(90 + i * 36)
        radius = 41 if i % 2 == 0 else 16.5
        star.append(point(cx + radius * math.cos(angle),
                          cy + radius * math.sin(angle)))
    shape(pen, star, "#FFDF36")

    # Bàn tay nắm cán ở lớp phía trước.
    ellipse(pen, hand_x, hand_y, 9, 11, "#F3C3A4")


def animate():
    global phase
    pen.clear()
    sway = 8 * math.sin(phase * 1.2)
    hand_x, hand_y = draw_person(sway)
    draw_flag(hand_x, hand_y)
    screen.update()
    phase += 0.11
    screen.ontimer(animate, 55)


animate()
screen.mainloop()
