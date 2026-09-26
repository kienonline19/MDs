# 10 bài tập vẽ hình bằng Python Turtle (có lời giải)

> Mức độ: dễ → trung bình. Mỗi bài gồm đề bài, cú pháp cần biết và gợi ý. **Toàn bộ lời giải nằm ở cuối tài liệu** để bạn có thể thử làm trước.

## Chuẩn bị

Lưu mã của **mỗi bài** vào một file `.py` riêng và chạy bằng Python trên máy có giao diện đồ họa. Đừng đặt tên file là `turtle.py`, vì tên này trùng với thư viện cần nhập.

```python
import turtle

screen = turtle.Screen()
screen.setup(900, 700)

pen = turtle.Turtle()
pen.speed(5)

# Viết lệnh vẽ ở đây.

turtle.done()  # Giữ cửa sổ vẽ mở sau khi chương trình chạy xong.
```

**Quy ước:** `pen` là con rùa dùng để vẽ. Ban đầu nó đứng tại `(0, 0)` và hướng sang phải. Đơn vị độ dài trên màn hình là pixel; góc tính bằng độ.

| Lệnh | Ý nghĩa |
|---|---|
| `pen.forward(100)` | Đi thẳng 100 pixel và vẽ đường đi. |
| `pen.left(90)` / `pen.right(90)` | Quay trái / phải 90°. |
| `pen.penup()` / `pen.pendown()` | Nhấc bút để di chuyển không vẽ / đặt bút để tiếp tục vẽ. |
| `pen.goto(x, y)` | Đi tới tọa độ `(x, y)`. |
| `pen.circle(50)` | Vẽ đường tròn bán kính 50 pixel. |
| `pen.color("red")` | Đặt màu nét bút. |
| `pen.fillcolor("yellow")` | Đặt màu tô hình. |
| `pen.begin_fill()` / `pen.end_fill()` | Bắt đầu / kết thúc vùng cần tô màu. |

---

# Phần 1 — Đề bài

## Bài 1. Hình vuông

Viết hàm `draw_square(side)` vẽ hình vuông có mỗi cạnh dài `side`. Gọi hàm với `side = 120`. Sau khi vẽ, rùa phải trở về vị trí **và hướng** ban đầu.

**Cú pháp cần dùng:**

```python
for _ in range(4):  # Lặp lại 4 lần; _ nghĩa là không cần dùng số lần lặp.
    pen.forward(120)
    pen.left(90)
```

**Gợi ý:** Hình vuông có bốn cạnh bằng nhau; tại mỗi đỉnh, rùa quay 90°.

## Bài 2. Hình chữ nhật

Viết hàm `draw_rectangle(width, height)` vẽ hình chữ nhật rộng `width = 180`, cao `height = 100`. Chỉ viết cặp lệnh vẽ chiều rộng và chiều cao **một lần** trong vòng lặp. Rùa phải quay về vị trí và hướng ban đầu.

**Cú pháp cần dùng:**

```python
for _ in range(2):
    pen.forward(width)
    pen.left(90)
    pen.forward(height)
    pen.left(90)
```

**Gợi ý:** Một vòng lặp đi qua hai cạnh; lặp hai vòng sẽ đi hết bốn cạnh.

## Bài 3. Tam giác đều

Viết hàm `draw_triangle(side)` vẽ tam giác đều cạnh `140`. Rùa phải trở về vị trí và hướng ban đầu.

**Cú pháp cần dùng:** `pen.forward(side)`, `pen.left(angle)` và `range(3)`.

**Gợi ý:** Góc trong của tam giác đều là 60°, nhưng **góc quay của rùa** ở mỗi đỉnh là `180° − 60° = 120°`.

## Bài 4. Ngôi sao năm cánh

Viết hàm `draw_star(size)` vẽ ngôi sao năm cánh bằng **một nét liên tục**, không dùng `penup()`. Gọi hàm với `size = 160`.

**Cú pháp cần dùng:** `for _ in range(5)` và `pen.right(144)`.

**Gợi ý:** Sau mỗi đoạn thẳng, quay 144° để nối sang đỉnh không kề ngay bên cạnh. Sau năm đoạn, nét vẽ sẽ khép kín.

## Bài 5. Ngôi nhà

Vẽ ngôi nhà gồm thân hình vuông cạnh `200`, mái hình tam giác, một cửa ra vào và hai cửa sổ. Thân nhà có đáy từ `(-100, -100)` đến `(100, -100)`; đỉnh mái ở `(0, 200)`. Tự chọn màu cho từng phần.

**Cú pháp cần dùng:**

```python
pen.penup()
pen.goto(-100, -100)  # Di chuyển đến điểm bắt đầu mà không vẽ.
pen.pendown()

pen.fillcolor("lightblue")
pen.begin_fill()
# Vẽ đường bao của một hình kín ở đây.
pen.end_fill()
```

**Gợi ý:** Có thể viết một hàm `filled_polygon(points, color)` nhận danh sách các đỉnh, nối các đỉnh bằng `goto()` và tô màu. Cửa và cửa sổ cũng là các hình chữ nhật nhỏ.

## Bài 6. Dãy năm hình vuông

Viết `draw_square(side)` rồi **gọi lại hàm đó năm lần** để tạo năm hình vuông cạnh `60`, xếp cùng một hàng. Giữa hai hình liên tiếp có khoảng trống `10` pixel. Hình đầu bắt đầu tại `(-170, 0)`.

**Cú pháp cần dùng:** Định nghĩa hàm bằng `def`, lặp `range(5)`, `pen.penup()`, `pen.goto(x, y)` và `pen.pendown()`.

**Gợi ý:** Tọa độ x của hình thứ `i` là `-170 + i * (60 + 10)`; tất cả có cùng tọa độ y là `0`.

## Bài 7. Bông hoa tám cánh

Vẽ bông hoa bằng **tám đường tròn** bán kính `35`, cùng đi qua tâm `(0, 50)`. Sau mỗi đường tròn, quay rùa một góc bằng nhau. Vẽ thêm thân hoa màu xanh từ `(0, 50)` xuống `(0, -150)`.

**Cú pháp cần dùng:** `pen.circle(35)`, `pen.left(45)`, `pen.pensize(4)` và `pen.color("green")`.

**Gợi ý:** `360° / 8 = 45°`. `circle()` vẽ xong sẽ đưa rùa trở lại điểm bắt đầu, nên có thể quay rồi vẽ cánh tiếp theo.

## Bài 8. Bàn cờ 8 × 8

Vẽ 64 ô vuông cạnh `40`, tạo thành bàn cờ `8 × 8`. Góc dưới bên trái của cả bàn cờ là `(-160, -160)`. Tô xen kẽ màu trắng và xám; hai ô chung cạnh phải khác màu.

**Cú pháp cần dùng:**

```python
for row in range(8):
    for col in range(8):
        color = "white" if (row + col) % 2 == 0 else "gray"
```

**Gợi ý:** Ô ở hàng `row`, cột `col` có góc dưới bên trái tại `(-160 + col * 40, -160 + row * 40)`. Hàm `% 2` cho biết tổng chỉ số là chẵn hay lẻ.

## Bài 9. Xoắn ốc vuông

Vẽ một đường xoắn ốc gồm **40 đoạn thẳng**. Đoạn đầu dài `5` pixel; mỗi đoạn sau dài hơn đoạn trước `5` pixel. Sau mỗi đoạn, rùa quay phải 90°. Dùng màu tím.

**Cú pháp cần dùng:**

```python
length = 5
for _ in range(40):
    pen.forward(length)
    pen.right(90)
    length += 5  # Tương đương length = length + 5.
```

**Gợi ý:** Đưa rùa về gần tâm trước khi vẽ; mỗi lần đi xa hơn rồi quay sẽ tạo xoắn ốc vuông.

## Bài 10. Bầu trời đêm

Đặt nền màu xanh đậm. Vẽ **15 ngôi sao năm cánh** ở các vị trí khác nhau; kích thước và màu ngôi sao thay đổi. Vẽ thêm một mặt trăng màu vàng bằng hình tròn.

**Cú pháp cần dùng:**

```python
import random

random.seed(42)               # Cho cùng một kết quả mỗi lần chạy.
x = random.randint(-350, 350)  # Số nguyên ngẫu nhiên trong đoạn [-350, 350].
size = random.choice([8, 12, 16])
```

**Gợi ý:** Viết lại hàm `draw_star(size)` của bài 4. Với mỗi ngôi sao: nhấc bút, đi tới vị trí ngẫu nhiên, đặt bút, chọn màu rồi gọi hàm. Giới hạn vùng đặt sao để chúng nằm trong cửa sổ.

---

# Phần 2 — Lời giải tham khảo

> Mỗi khối mã dưới đây là **một chương trình độc lập**. Sao chép nguyên một khối vào file `.py` để chạy. Bạn có thể giải khác mà vẫn đúng nếu hình vẽ đáp ứng đề bài.

## Lời giải bài 1

```python
import turtle

pen = turtle.Turtle()

def draw_square(side):
    for _ in range(4):
        pen.forward(side)
        pen.left(90)

draw_square(120)
turtle.done()
```

```python
import turtle

screen = turtle.Screen()

screen.setup(900, 700)
screen.bgcolor("#0B1220")

pen = turtle.Turtle()

pen.speed(0)
pen.hideturtle()

def draw_square(side, x, y, fill_color, border_color, border_width=2):
    pen.penup()

    pen.goto(x, y)

    pen.setheading(0)

    pen.pendown()

    pen.pensize(border_width)
    pen.pencolor(border_color)
    pen.fillcolor(fill_color)

    pen.begin_fill()

    for _ in range(4):
        pen.forward(side)
        pen.left(90)

    pen.end_fill()


draw_square(260, -118, -142, "#050810", "#050810")
draw_square(260, -130, -130, "#38BDF8", "#38BDF8")
draw_square(244, -122, -122, "#16324F", "#16324F")
draw_square(200, -100, -100, "#16234F", "#7DD3FC", 2)

pen.penup()

pen.pencolor("#FACC15")

for x, y in [(-100, -100), (100, -100), (100, 100), (-100, 100)]:
    pen.goto(x, y)
    pen.dot(10)

turtle.done()

```

**Giải thích:** Mỗi vòng lặp vẽ một cạnh. Tổng góc quay là `4 × 90° = 360°`, nên rùa trở về đúng hướng ban đầu.

## Lời giải bài 2

```python
import turtle

pen = turtle.Turtle()

def draw_rectangle(width, height):
    for _ in range(2):
        pen.forward(width)
        pen.left(90)
        pen.forward(height)
        pen.left(90)

draw_rectangle(180, 100)
turtle.done()
```

**Giải thích:** Mỗi vòng vẽ một cạnh ngang và một cạnh dọc. Hai vòng tạo đủ bốn cạnh và tổng cộng quay 360°.

## Lời giải bài 3

```python
import turtle

pen = turtle.Turtle()

def draw_triangle(side):
    for _ in range(3):
        pen.forward(side)
        pen.left(120)

draw_triangle(140)
turtle.done()
```

**Giải thích:** Rùa quay theo góc ngoài 120° tại mỗi đỉnh. Ba lần quay tạo thành 360°.

## Lời giải bài 4

```python
import turtle

pen = turtle.Turtle()

def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

draw_star(160)
turtle.done()
```

**Giải thích:** Mỗi đoạn dài bằng nhau và được nối liền. Quay 144° năm lần giúp rùa đi qua cả năm đỉnh rồi trở về điểm xuất phát.

## Lời giải bài 5

```python
import turtle

screen = turtle.Screen()
screen.setup(600, 500)
pen = turtle.Turtle()
pen.speed(5)

def filled_polygon(points, color):
    pen.penup()
    pen.goto(points[0])
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()

    for point in points[1:]:
        pen.goto(point)
    pen.goto(points[0])  # Khép kín đường bao.

    pen.end_fill()

# Thân nhà: từ y = -100 đến y = 100.
filled_polygon(
    [(-100, -100), (100, -100), (100, 100), (-100, 100)],
    "lightblue",
)

# Mái nhà: đáy nằm trên cạnh trên của thân nhà.
filled_polygon([(-120, 100), (0, 200), (120, 100)], "tomato")

# Cửa ra vào chạm cạnh dưới của thân nhà.
filled_polygon([(-25, -100), (25, -100), (25, 0), (-25, 0)], "saddlebrown")

# Hai cửa sổ.
filled_polygon([(-80, 20), (-40, 20), (-40, 65), (-80, 65)], "yellow")
filled_polygon([(40, 20), (80, 20), (80, 65), (40, 65)], "yellow")

pen.hideturtle()
turtle.done()
```

**Giải thích:** `points[0]` lấy đỉnh đầu tiên; `points[1:]` lấy các đỉnh còn lại. `pen.goto(points[0])` nối đỉnh cuối về đỉnh đầu. Cùng một hàm được dùng để vẽ và tô cả thân, mái, cửa và cửa sổ.

## Lời giải bài 6

```python
import turtle

pen = turtle.Turtle()
pen.speed(5)

def draw_square(side):
    for _ in range(4):
        pen.forward(side)
        pen.left(90)

for i in range(5):
    x = -170 + i * (60 + 10)
    pen.penup()
    pen.goto(x, 0)
    pen.pendown()
    draw_square(60)

pen.hideturtle()
turtle.done()
```

**Giải thích:** Mỗi hình bắt đầu cách hình trước `60 + 10 = 70` pixel theo trục x. `penup()` ngăn rùa vẽ đường nối giữa các hình.

## Lời giải bài 7

```python
import turtle

pen = turtle.Turtle()
pen.speed(0)

# Vẽ thân trước để nét thân nằm dưới cánh hoa.
pen.penup()
pen.goto(0, -150)
pen.pendown()
pen.color("green")
pen.pensize(4)
pen.goto(0, 50)

# Tám đường tròn cùng bắt đầu tại tâm bông hoa.
pen.color("deeppink")
pen.pensize(2)
for _ in range(8):
    pen.circle(35)
    pen.left(45)

pen.hideturtle()
turtle.done()
```

**Giải thích:** Sau mỗi `circle(35)`, rùa về `(0, 50)` và giữ hướng ban đầu của vòng tròn đó. Quay 45° rồi vẽ tiếp tạo tám vòng tròn tỏa đều quanh điểm này.

## Lời giải bài 8

```python
import turtle

screen = turtle.Screen()
screen.setup(500, 500)
pen = turtle.Turtle()
pen.speed(0)

def draw_filled_square(x, y, side, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.fillcolor(color)
    pen.begin_fill()
    for _ in range(4):
        pen.forward(side)
        pen.left(90)
    pen.end_fill()

for row in range(8):
    for col in range(8):
        x = -160 + col * 40
        y = -160 + row * 40
        color = "white" if (row + col) % 2 == 0 else "gray"
        draw_filled_square(x, y, 40, color)

pen.hideturtle()
turtle.done()
```

**Giải thích:** Vòng ngoài chọn hàng, vòng trong chọn cột nên có `8 × 8 = 64` ô. Khi di chuyển sang ô chung cạnh, tính chẵn lẻ của `row + col` đổi và màu cũng đổi.

## Lời giải bài 9

```python
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
pen = turtle.Turtle()
pen.speed(0)
pen.color("purple")

length = 5
for _ in range(40):
    pen.forward(length)
    pen.right(90)
    length += 5

pen.hideturtle()
turtle.done()
```

**Giải thích:** `length` bắt đầu bằng 5 và tăng thêm 5 sau mỗi đoạn: 5, 10, 15, …, 200. Bốn lần quay phải tạo một vòng quanh tâm; đoạn dài dần làm đường vẽ mở rộng ra ngoài.

## Lời giải bài 10

```python
import random
import turtle

screen = turtle.Screen()
screen.setup(900, 700)
screen.bgcolor("midnightblue")

pen = turtle.Turtle()
pen.speed(0)

def draw_star(size):
    for _ in range(5):
        pen.forward(size)
        pen.right(144)

random.seed(42)
colors = ["white", "lightyellow", "gold", "lightcyan"]

for _ in range(15):
    x = random.randint(-370, 320)
    y = random.randint(-270, 270)
    size = random.choice([8, 12, 16, 20])

    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(random.choice(colors))
    draw_star(size)

# Mặt trăng: goto() đặt điểm thấp nhất của đường tròn.
pen.penup()
pen.goto(280, 170)
pen.pendown()
pen.color("gold")
pen.fillcolor("gold")
pen.begin_fill()
pen.circle(55)
pen.end_fill()

pen.hideturtle()
turtle.done()
```

**Giải thích:** `random.randint(a, b)` chọn vị trí, còn `random.choice(list)` chọn kích thước và màu. `random.seed(42)` giúp bạn chạy lại và thấy đúng bố cục cũ; bỏ dòng đó nếu muốn bầu trời khác nhau mỗi lần. Mỗi lần vẽ xong một ngôi sao, rùa trở về điểm và hướng ban đầu của ngôi sao ấy.

---

## Tự kiểm tra sau khi làm

- Hình có đủ số cạnh, cánh, ô hoặc ngôi sao theo đề không?
- Các đường nối giữa hai hình có xuất hiện ngoài ý muốn không? Nếu có, hãy dùng `penup()` trước khi di chuyển.
- Các hình cần tô đã có đủ `begin_fill()` và `end_fill()` chưa?
- Nếu cửa sổ vẽ đóng ngay hoặc không xuất hiện, hãy chạy file `.py` trong môi trường Python có hỗ trợ cửa sổ đồ họa và giữ `turtle.done()` ở cuối chương trình.
