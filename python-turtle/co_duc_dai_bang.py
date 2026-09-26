import base64
import zlib
import turtle

screen = turtle.Screen()
screen.setup(900, 620)
screen.bgcolor("#EDF0F4")
screen.title("Cờ công vụ liên bang Đức — Bundesdienstflagge")
screen.tracer(0)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

SCALE = 1.5
LEFT = -375
TOP = 225


def point(x, y):
    return LEFT + x * SCALE, TOP - y * SCALE


def polygon(points, color, outline=None, width=1):
    pen.penup()
    pen.goto(point(*points[0]))
    pen.pencolor(outline or color)
    pen.fillcolor(color)
    pen.pensize(width)
    pen.pendown()
    pen.begin_fill()
    for x, y in points[1:]:
        pen.goto(point(x, y))
    pen.goto(point(*points[0]))
    pen.end_fill()


def rectangle(x1, y1, x2, y2, color):
    polygon([(x1, y1), (x2, y1), (x2, y2), (x1, y2)], color)


rectangle(6, 6, 506, 306, "#B7C0CC")  
rectangle(0, 0, 500, 100, "#000000")
rectangle(0, 100, 500, 200, "#DD0000")
rectangle(0, 200, 500, 300, "#FFCE00")

shield = [
    (189, 83), (300, 83), (300, 177), (296, 194),
    (286, 206), (270, 215), (245, 221), (221, 215),
    (204, 205), (192, 190), (189, 177),
]
polygon(shield, "#FFCE00", "#1A1A1A", 2)

BLACK = (
    'c-jrb>tm@3008h0_fk9ZCYs08h>%K%QVCJXBg(9iov?GZ-S_j~zxVgy_d~1mW2+ZvF#)z8r08Im2WST9i6A50wWTk$+L'
    '!h))E1#Q0<j{reGbR+VO9*U-'
    'AJSuDVHOx7+D^p&_fi*qXZFU#puF|fu&fr8e^rH;m5&JyjF{|Qrz$p;6tJ#B^G`Xd`Q;oNrp+XQquHOU@=8XsimI=^J!'
    '8_uY4HH!%Z1p`5CZ~Y08<Up9PEArkpi>1bjf6GGhAo;KO}GzF+t`u#{`aIm6F`rF=uq8-'
    '4*q3y(yhAs5E;g6<bV{{i$%-~|OQ7;t$6E@j|S0WLUjsRH3@%&nd-'
    'H6UDzKi5td0tgfFXX13J1L1nyt$UXS5N^cXhIeTK;bt6eB39FOo8E;4ATkb<h(+2i>0Mg@)QZ6^#A?}Y%ezuRh>F1!@<'
    '3rawXi7LrMxR0gy<MdBSjk1Xw#x?m-enq5Mp95gA^G|V@!*&UB<h%gHSsLw~=BStF{THJ<-'
    '~x)wbRC`N{@EYz$_RB8%Z{U16shYg(-1vgd0j80tjR9i-U7@J?OnOtp?_b)1*Z`PL1Fy3uqODRwcuODNr`)-'
    '|_X=cRkT^#Y+@G~GjrJq+*FmEKhAncJT8(mUU{K!}T`xonZcaE?&8sm7UG&UxX^w|*ehkEZ+CVjso(gwmhteRJD)Uiz='
    'MK_E1UrU%*L0L2FcIiQ4rs0^n1V7VPQFN4<`ANayYQ+&3-qc~5HJk9f>!mB#J-15$mf4vC-'
    'P>804Y(YSAfglB%7eqx+bz!*`_D8|L4FkY1k{V_ULlhqp<dEivqB2zV;c`3NABWdBF_IFq1rfzXf)p8E6ctg`#pPDqAE'
    'ii2$`&NFA`zs-3?xyJR9#x`r2SEjq~uINMk_MWkePujE3&G~%bmPGjv}d1rZ7S)Bbpy6%1G5mtKDdSR3a%QQ&7-'
    '~LJ5j$D65^aKaL~GaV9@TE92I1tQzChZv1qbgp-p@ep0GTNO7VXlhtnWbee{f(@cI^Do>lzR5hln-Sp|ChLdV0ua?ScL'
    'sn;oy0X=$(=42v!TDJUo7G1%&6ut1+0$trPR`-'
    '{oKWT~d;WCN!buIzY1N6gwzb1a4<~dur{k)=w)KN&KnVlR8Q9!d+s46LK#2vMTcG-'
    '4Z7&X<2_;N8XQH~fw#|dLgc8eiZi#8jwX-'
    '~UD=4u_=T_zUYU8Y)y)_hHr|;K~<eKK!;(Wbv*3ah+6yKzg4c^?){6?B?=Gw+`HtyL9MXYqj!W$ONTe52H9P4=ARvTMN'
    '*p4RK*=*~1yJ~$$3A@o`H=o<Jx=jhTGInZ&LkW&D-'
    'nWKNq<FZyJA|MEDLpr2_b%lAzwf^^<rm*Sw#1{ZpGu_@!=DVpE0sL#(W80KFwW@Xxh0%6?G?pdo6@VMe~m=GR@ASW=7&'
    'OlCgWFB-*qnta;d0S1i6-HHwe0AGPlS1&GX(6<PFo_JntLEd}Fz9y#5`fzO&qSUVq10?=1H|oV=_02Uh;5H9y+@4{7o-'
    '(>}4s&szPH8GMe$pL6XeX7Dp5{6Y!8GW>5W_dCn|!E%3gxW78w-(BvXZtvf2_dl&kGQ|'
)
RED = (
    'c-jTQ$wGoa007WK8-ln~fkgr$XqqY4Zf1a@4kG)&45PsR|3UBFea`QviwAx2sDC|aOG^80Xe(M<F`CXS*3GXqyIi-'
    '%dTVC1RiiU8x|-'
    '3O8vUs;m@T>a{HLlMNjg~8QBh8^dNM5_sbFinBh}sR&*J3#yZ1!Z(=>0h@&264`}krW{5Qonj{(yOhH_w?f&_(hFBGJ3'
    '=Z0YsH3reE6z$GYP{foJ+a#gn#3Cuhq^yvNa%vt@kfoSFih^w(iV8Fx=*BRGkdUm)XQGmsPUgmWi_brl+;nmmqGlg)JQ'
    '_(zQINSqu8+bTGd;`+Sdy`AW8mWm6-=+-gu=25;1>}hbeC`f0X~WGmF`|S;R^g~f^T&D#tApz-'
    '%?yMZ23Ga!KKVl#jw@OusV5FhUz9;^Fr;O>n#5VRCQHO'
)


def draw_details(data, color):
    raw = zlib.decompress(base64.b85decode(data))
    pen.pencolor(color)
    pen.pensize(SCALE + 0.35)
    for i in range(0, len(raw), 3):
        row, start, end = raw[i:i + 3]
        y = 86 + row + 0.5
        x1 = 190 + start + 0.5
        x2 = 190 + end + 0.5
        pen.penup()
        pen.goto(point(x1, y))
        if start == end:
            pen.dot(SCALE + 0.35, color)
        else:
            pen.pendown()
            pen.goto(point(x2, y))


draw_details(BLACK, "#111111")
draw_details(RED, "#C90000")

screen.update()
turtle.done()
