# HƯỚNG DẪN SYMJA: TÍNH ĐẠO HÀM, TÍCH PHÂN KÝ HIỆU BẰNG JAVA

Tài liệu đi từ cài đặt đến giải bài từng bước, theo đúng thứ tự các vấn đề gặp phải khi dùng Symja trong Eclipse.

---

## Mục lục

1. [Symja là gì, khi nào dùng](#1-symja-là-gì-khi-nào-dùng)
2. [Cài đặt trong Eclipse](#2-cài-đặt-trong-eclipse)
3. [Chương trình đầu tiên](#3-chương-trình-đầu-tiên)
4. [Tắt cảnh báo đỏ trong Console](#4-tắt-cảnh-báo-đỏ-trong-console)
5. [Cú pháp Symja](#5-cú-pháp-symja)
6. [Tính đạo hàm](#6-tính-đạo-hàm)
7. [Kiểm tra đáp án](#7-kiểm-tra-đáp-án)
8. [Giải từng bước](#8-giải-từng-bước)
9. [Tính tích phân](#9-tính-tích-phân)
10. [Vẽ đồ thị](#10-vẽ-đồ-thị)
11. [Tốc độ chạy](#11-tốc-độ-chạy)
12. [Lỗi thường gặp](#12-lỗi-thường-gặp)
13. [Mẫu code hoàn chỉnh](#13-mẫu-code-hoàn-chỉnh)
14. [Bảng tra lệnh nhanh](#14-bảng-tra-lệnh-nhanh)

---

## 1. Symja là gì, khi nào dùng

**Symja** là thư viện tính toán **ký hiệu** cho Java, giống một bản Mathematica thu nhỏ. Nó nhận vào biểu thức dạng chuỗi và trả về **công thức**, không phải con số.

| | Symja | Apache Commons Math |
|---|---|---|
| Kết quả | Công thức: `2*x*Cos(x)` | Con số: `1.0806...` |
| Đạo hàm | Ra công thức $`y'`$ | Giá trị $`y'(x_0)`$ tại một điểm |
| Tích phân | Nguyên hàm và tích phân chính xác | Tích phân xác định gần đúng |
| Kích thước | Lớn (nhiều MB, nhiều thư viện phụ) | Nhỏ (1 file .jar) |
| Tốc độ | Khởi động chậm vài giây | Gần như tức thì |

**Chọn thư viện theo nhu cầu:**

| Muốn | Dùng |
|---|---|
| Công thức đạo hàm, nguyên hàm của mọi loại hàm | Symja |
| Công thức đạo hàm của **đa thức** | Commons Math `PolynomialFunction` |
| Giá trị đạo hàm, tích phân tại một điểm, tính nhiều lần | Commons Math |

---

## 2. Cài đặt trong Eclipse

Symja kéo theo nhiều thư viện phụ, **nên dùng Maven Project**. Thêm từng file .jar bằng tay rất dễ thiếu.

### Cách 1: Maven Project (khuyên dùng)

**Bước 1.** Tạo project: **File → New → Other → Maven → Maven Project** → tích **Create a simple project** → điền Group Id (vd `com.example`), Artifact Id (vd `DerivativeIntegral`) → **Finish**.

**Bước 2.** Mở `pom.xml`, thêm vào trong thẻ `<dependencies>`:

```xml
<dependencies>
    <!-- Symja -->
    <dependency>
        <groupId>org.matheclipse</groupId>
        <artifactId>matheclipse-core</artifactId>
        <version>3.0.0</version>
    </dependency>

    <!-- Tắt cảnh báo SLF4J (xem mục 4) -->
    <dependency>
        <groupId>org.slf4j</groupId>
        <artifactId>slf4j-nop</artifactId>
        <version>1.7.36</version>
    </dependency>
</dependencies>
```

**Bước 3.** Lưu file (Ctrl+S) → chuột phải project → **Maven → Update Project** (Alt+F5) → OK.

Thư viện xuất hiện trong mục **Maven Dependencies** là xong.

### Cách 2: Java Project thường (dùng file .jar)

Tải lẻ `matheclipse-core-3.0.0.jar` là **không đủ**, chạy sẽ báo `NoClassDefFoundError`. Cách lấy đủ bộ .jar:

1. Tạo một Maven Project tạm như cách 1.
2. Chuột phải project → **Run As → Maven build…** → ô **Goals** gõ `dependency:copy-dependencies` → **Run**.
3. Mở thư mục `target/dependency`: ở đó có đầy đủ mọi file .jar Symja cần.
4. Copy cả thư mục vào `lib` của project bài tập → chọn tất cả → chuột phải → **Build Path → Add to Build Path**.

Bộ .jar này dùng lại được.

**Link tham khảo:**
- Maven Central: https://central.sonatype.com/artifact/org.matheclipse/matheclipse-core
- SourceForge (bản 3.0.0): https://sourceforge.net/projects/matheclipse/files/v3.0.0
- Mã nguồn và tài liệu: https://github.com/axkr/symja_android_library

---

## 3. Chương trình đầu tiên

Tính đạo hàm của $`y = \ln(x^2 + 3x)`$:

```java
package com.example.DerivativeIntegral;

import org.matheclipse.core.eval.ExprEvaluator;

public class TestDerivative {
    public static void main(String[] args) {
        ExprEvaluator expr = new ExprEvaluator();
        System.out.println(expr.eval("D(Log(x^2 + 3*x), x)"));
    }
}
```

| Dòng | Ý nghĩa |
|---|---|
| `import ...ExprEvaluator;` | Nạp bộ tính toán của Symja |
| `new ExprEvaluator()` | Tạo bộ tính toán. Lần đầu mất vài giây để nạp quy tắc toán học |
| `"Log(x^2 + 3*x)"` | Hàm $`\ln(x^2 + 3x)`$ viết bằng cú pháp Symja |
| `D(..., x)` | Đạo hàm theo biến $`x`$ |
| `expr.eval(...)` | Tính và trả về biểu thức kết quả (kiểu `IExpr`) |

**Kết quả:**
```
(3+2*x)/(3*x+x^2)
```
Tức là $`y' = \dfrac{2x + 3}{x^2 + 3x}`$. Symja tự sắp xếp số hạng theo thứ tự riêng, nên `3+2*x` chính là $`2x + 3`$.

---

## 4. Tắt cảnh báo đỏ trong Console

Lần chạy đầu, Console thường hiện các dòng đỏ như:

```
ERROR StatusLogger Log4j2 could not find a logging implementation...
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
```

**Đây không phải lỗi của chương trình.** Kết quả vẫn in đúng ở dòng cuối. Đó là cảnh báo từ hai thư viện ghi log (Log4j và SLF4J) mà Symja dùng bên trong, báo rằng chúng không tìm thấy nơi để ghi log.

### Tắt cảnh báo SLF4J

Thêm `slf4j-nop` vào `pom.xml` (đã có trong mục 2) rồi **Maven → Update Project**.

Nếu vẫn còn dòng SLF4J: mở **Maven Dependencies**, tìm `slf4j-api-x.y.z.jar`. Nếu phiên bản bắt đầu bằng **2.** thì đổi `1.7.36` thành đúng số phiên bản đó.

### Tắt cảnh báo Log4j

Thêm dòng sau **ở đầu `main`, trước `new ExprEvaluator()`**:

```java
System.setProperty("log4j2.loggerContextFactory",
        "org.apache.logging.log4j.simple.SimpleLoggerContextFactory");
```

Phải đặt trước, vì Log4j khởi động ngay khi Symja được tạo. Đặt sau thì cảnh báo đã in ra rồi.

**Cách khác, không sửa code:** **Run As → Run Configurations…** → tab **Arguments** → ô **VM arguments** dán:
```
-Dlog4j2.loggerContextFactory=org.apache.logging.log4j.simple.SimpleLoggerContextFactory
```

---

## 5. Cú pháp Symja

### Bảng chuyển Toán → Symja

| Toán | Symja | Ghi chú |
|---|---|---|
| $`2x`$ | `2*x` | **Bắt buộc có dấu `*`** |
| $`x^n`$ | `x^n` | |
| $`\sqrt{x}`$ | `Sqrt(x)` | |
| $`\sin x`$, $`\cos x`$, $`\tan x`$ | `Sin(x)`, `Cos(x)`, `Tan(x)` | Viết hoa chữ đầu |
| $`\cos^3 x`$ | `Cos(x)^3` | Không viết `Cos^3(x)` |
| $`\arctan x`$ | `ArcTan(x)` | |
| $`e^x`$ | `Exp(x)` hoặc `E^x` | |
| $`\ln x`$ | `Log(x)` | `Log` là logarit **tự nhiên** |
| $`\log_a x`$ | `Log(a, x)` | **Cơ số đứng trước** |
| $`\pi`$ | `Pi` | |
| $`e`$ | `E` | |

### Quy tắc cần nhớ

- Tên hàm **viết hoa chữ đầu**: `Sin`, không phải `sin`.
- Dùng **ngoặc tròn** cho hàm: `Sin(x)`. (Mathematica dùng ngoặc vuông, Symja chấp nhận cả hai.)
- **Ngoặc nhọn** `{ }` dùng cho danh sách và khoảng: `{x, 0, 1}`.

### Đọc kết quả Symja in ra

| Symja in | Nghĩa là |
|---|---|
| `3+2*x` | $`2x + 3`$ (thứ tự đảo) |
| `E^x` | $`e^x`$ |
| `Log(x)` | $`\ln x`$ |
| `Sec(x)` | $`\dfrac{1}{\cos x}`$ |
| `x^(1/2)` | $`\sqrt{x}`$ |

---

## 6. Tính đạo hàm

### Các lệnh cơ bản

| Muốn | Lệnh | Ví dụ |
|---|---|---|
| Đạo hàm cấp 1 | `D(f, x)` | `D(x^2*Sin(x), x)` |
| Đạo hàm cấp $`n`$ | `D(f, {x, n})` | `D(x*Exp(x), {x, 2})` |
| Giá trị tại $`x = a`$ | `D(f, x) /. x -> a` | `D(Log(x^2+3*x), x) /. x -> 1` |

Lệnh cuối in ra `5/4`, là **phân số chính xác**, không phải `1.25` như Commons Math.

### Các lệnh biến đổi kết quả

| Lệnh | Tác dụng | Ví dụ |
|---|---|---|
| `Simplify(e)` | Rút gọn | `Simplify(D(Sin(x)/(1+Cos(x)), x))` → `1/(1+Cos(x))` |
| `Expand(e)` | Khai triển | `Expand((2*x+1)*(x-1))` → `-1-x+2*x^2` |
| `Together(e)` | Gộp thành một phân thức | `Together(1 - 3/(x-1)^2)` |
| `Factor(e)` | Phân tích thành nhân tử | `Factor(x^2 - 1)` → `(-1+x)*(1+x)` |
| `Cancel(e)` | Rút gọn tử và mẫu | `Cancel((x^2-1)/(x-1))` → `1+x` |
| `PowerExpand(e)` | Áp dụng $`\ln(a^b) = b\ln a`$, $`\sqrt{a^2} = a`$ (coi biến dương) | `PowerExpand(Log(x^x))` → `x*Log(x)` |
| `e /. a -> b` | Thay $`a`$ bằng $`b`$ | `Sin(x)^2 /. Sin(x)^2 -> 1 - Cos(x)^2` |

### Ví dụ 20 loại hàm

| Loại | Hàm | Lệnh Symja |
|---|---|---|
| Đa thức | $`2x^5 - 3x^3 + x - 4`$ | `D(2*x^5 - 3*x^3 + x - 4, x)` |
| Tích | $`(x^2+1)(x^3-2x)`$ | `D((x^2 + 1)*(x^3 - 2*x), x)` |
| Hàm hợp | $`(2x+3)^5`$ | `D((2*x + 3)^5, x)` |
| Thương | $`\dfrac{3x-2}{x+1}`$ | `D((3*x - 2)/(x + 1), x)` |
| Căn | $`\sqrt{3x^2-2x+5}`$ | `D(Sqrt(3*x^2 - 2*x + 5), x)` |
| Lượng giác | $`\sin 3x + \cos 2x`$ | `D(Sin(3*x) + Cos(2*x), x)` |
| Hàm hợp 2 lớp | $`\cos^3 x`$ | `D(Cos(x)^3, x)` |
| Hàm mũ | $`e^{x^2-2x}`$ | `D(Exp(x^2 - 2*x), x)` |
| Mũ cơ số $`a`$ | $`2^x + 3^{2x}`$ | `D(2^x + 3^(2*x), x)` |
| Logarit | $`\ln(x^2+3x)`$ | `D(Log(x^2 + 3*x), x)` |
| Logarit cơ số $`a`$ | $`\log_2(5x)`$ | `D(Log(2, 5*x), x)` |
| Lượng giác ngược | $`\arctan 2x`$ | `D(ArcTan(2*x), x)` |
| Cơ số và mũ đều là biến | $`x^x`$ | `D(x^x, x)` |
| Cấp hai | $`(xe^x)''`$ | `D(x*Exp(x), {x, 2})` |

---

## 7. Kiểm tra đáp án

Không nên so sánh **chuỗi** kết quả, vì cùng một công thức có nhiều cách viết. Ví dụ $`\cos 2x`$ và $`\cos^2 x - \sin^2 x`$ là một, nhưng chuỗi khác nhau.

Dùng `PossibleZeroQ`: lấy hiệu hai biểu thức, nếu bằng 0 thì chúng bằng nhau.

```java
IExpr kq = util.eval("PossibleZeroQ(D(Sin(x)*Cos(x), x) - Cos(2*x))");
System.out.println(kq.isTrue());   // true
```

| Phần | Ý nghĩa |
|---|---|
| `D(...) - (đáp án)` | Hiệu giữa kết quả của Symja và đáp án tay |
| `PossibleZeroQ(...)` | Trả về `True` nếu hiệu đó bằng 0 |
| `.isTrue()` | Chuyển kết quả Symja thành `boolean` của Java |

Nhớ `import org.matheclipse.core.interfaces.IExpr;`

**Ứng dụng chấm bài:** để trống cột đáp án, cho học sinh tự tính tay rồi điền vào, chạy chương trình để chấm tự động. Học sinh viết đáp án dạng khác vẫn được tính đúng.

---

## 8. Giải từng bước

Symja **không có sẵn** chế độ giải từng bước. Cách làm là tự chia bài thành các bước như khi giải tay, mỗi bước gọi Symja một lần và in kết quả.

### 8.1. Gán biến trong Symja

Symja nhớ biến giữa các lần gọi `eval`, nên có thể đặt $`u`$, $`v`$ như giải tay:

```java
util.eval("u = x^2 + 1");
util.eval("du = D(u, x)");        // u' = 2*x
util.eval("du*v + u*dv");         // dùng lại u, du ở trên
```

Hết mỗi bài phải **xóa biến** để bài sau không bị dính giá trị cũ:
```java
util.eval("Clear(u, v, du, dv)");
```

### 8.2. Ví dụ: quy tắc tích $`y = (x^2 + 1)(x^3 - 2x)`$

```java
System.out.println("u  = " + util.eval("u = x^2 + 1"));
System.out.println("v  = " + util.eval("v = x^3 - 2*x"));
System.out.println("u' = " + util.eval("du = D(u, x)"));
System.out.println("v' = " + util.eval("dv = D(v, x)"));
System.out.println("u'v + uv' = " + util.eval("du*v + u*dv"));
System.out.println("Khai triển: " + util.eval("Expand(du*v + u*dv)"));
```

Kết quả:
```
u  = 1+x^2
v  = -2*x+x^3
u' = 2*x
v' = -2+3*x^2
u'v + uv' = 2*x*(-2*x+x^3)+(1+x^2)*(-2+3*x^2)
Khai triển: -2-3*x^2+5*x^4
```

### 8.3. Ví dụ: lấy logarit hai vế $`y = x^x`$

| Bước | Toán | Symja |
|---|---|---|
| 1 | $`\ln y = x \ln x`$ | `PowerExpand(Log(x^x))` |
| 2 | $`\dfrac{y'}{y} = (x\ln x)' = \ln x + 1`$ | `D(x*Log(x), x)` |
| 3 | $`y' = x^x(\ln x + 1)`$ | `x^x*D(x*Log(x), x)` |
| Kiểm tra | | `D(x^x, x)` |

```java
System.out.println("Bước 1: ln y = " + util.eval("PowerExpand(Log(x^x))"));
System.out.println("Bước 2: (x ln x)' = " + util.eval("D(x*Log(x), x)"));
System.out.println("Bước 3: y' = " + util.eval("x^x*D(x*Log(x), x)"));
System.out.println("Kiểm tra: " + util.eval("D(x^x, x)"));
```

**Vì sao cần `PowerExpand`:** Symja không tự biến $`\ln(x^x)`$ thành $`x \ln x`$, vì công thức $`\ln(a^b) = b\ln a`$ chỉ đúng khi $`a > 0`$. `PowerExpand` cho phép áp dụng công thức này.

### 8.4. Ví dụ: dùng hằng đẳng thức $`y = \dfrac{\sin x}{1 + \cos x}`$

Dùng phép thay `/.` để làm đúng bước "thay $`\sin^2 x + \cos^2 x = 1`$" như giải tay:

```java
util.eval("u = Sin(x)");  util.eval("v = 1 + Cos(x)");
util.eval("du = D(u, x)"); util.eval("dv = D(v, x)");

System.out.println(util.eval("Expand(du*v - u*dv)"));
// Cos(x)+Cos(x)^2+Sin(x)^2

System.out.println(util.eval("Expand(du*v - u*dv) /. Sin(x)^2 -> 1 - Cos(x)^2"));
// 1+Cos(x)
```

### 8.5. Ví dụ: chia đa thức trước $`y = \dfrac{x^2 + x + 1}{x - 1}`$

```java
util.eval("PolynomialQuotient(x^2 + x + 1, x - 1, x)");   // thương: 2+x
util.eval("PolynomialRemainder(x^2 + x + 1, x - 1, x)");  // dư: 3
// => y = x + 2 + 3/(x - 1)
util.eval("Together(D(x + 2 + 3/(x - 1), x))");
```

### 8.6. Khung chương trình giải từng bước

Viết vài hàm in dùng chung để code mỗi bài ngắn gọn:

```java
static ExprEvaluator util;
static int buocSo;

/** In đề bài, xóa biến cũ */
static void deBai(int so, String ham, String nhanDang) {
    util.eval("Clear(u, v, du, dv)");
    buocSo = 0;
    System.out.println("BÀI " + so + ": " + ham);
    System.out.println("  Nhận dạng: " + nhanDang);
}

/** Một bước tính */
static void buoc(String moTa, String lenh) {
    buocSo++;
    System.out.println("  Bước " + buocSo + ": " + moTa);
    System.out.println("      = " + util.eval(lenh));
}

/** Gán biến và in */
static void gan(String ten, String bieuThuc, String hienThi) {
    System.out.println("      " + hienThi + " = " + util.eval(ten + " = " + bieuThuc));
}
```

Mỗi bài khi đó chỉ còn vài dòng:

```java
static void bai05() {
    deBai(5, "y = (3x - 2)/(x + 1)", "Thương -> (u/v)' = (u'v - uv')/v^2");
    gan("u", "3*x - 2", "u");
    gan("v", "x + 1", "v");
    gan("du", "D(u, x)", "u'");
    gan("dv", "D(v, x)", "v'");
    buoc("Tử số u'v - uv'", "Expand(du*v - u*dv)");
    buoc("Kết quả", "Expand(du*v - u*dv)/v^2");
}
```

---

## 9. Tính tích phân

### Các lệnh

| Loại | Lệnh | Ví dụ |
|---|---|---|
| Nguyên hàm | `Integrate(f, x)` | `Integrate(3*x^2 + 2*x, x)` → `x^2+x^3` |
| Tích phân xác định | `Integrate(f, {x, a, b})` | `Integrate(Sin(x), {x, 0, Pi})` → `2` |
| Tích phân tính số | `NIntegrate(f, {x, a, b})` | `NIntegrate(Exp(-x^2), {x, 0, 1})` → `0.746824...` |

### Lưu ý

- Symja **không ghi hằng số $`C`$** trong nguyên hàm. Khi chép đáp án phải tự thêm $`+ C`$.
- Tích phân xác định ra **giá trị chính xác** (`2`, `Pi/4`), không có sai số như Commons Math.
- Nếu Symja không tính được, nó **in lại nguyên lệnh** `Integrate(...)` chứ không báo lỗi. Khi đó với tích phân xác định thì chuyển sang `NIntegrate`.

### Ví dụ

| Toán | Lệnh | Kết quả |
|---|---|---|
| $`\int \dfrac{1}{x}\,dx`$ | `Integrate(1/x, x)` | $`\ln x`$ |
| $`\int e^{2x}\,dx`$ | `Integrate(Exp(2*x), x)` | $`\dfrac{e^{2x}}{2}`$ |
| $`\int x\cos x\,dx`$ | `Integrate(x*Cos(x), x)` | $`\cos x + x\sin x`$ |
| $`\int_1^e \ln x\,dx`$ | `Integrate(Log(x), {x, 1, E})` | $`1`$ |
| $`\int_0^1 \dfrac{1}{1+x^2}\,dx`$ | `Integrate(1/(1+x^2), {x, 0, 1})` | $`\dfrac{\pi}{4}`$ |

### Kiểm tra nguyên hàm bằng đạo hàm

```java
System.out.println(util.eval("D(Integrate(x*Cos(x), x), x)"));   // x*Cos(x)
```
Đạo hàm lại nguyên hàm phải ra hàm ban đầu.

---

## 10. Vẽ đồ thị

Symja có `Plot` (2D), `Plot3D` (3D), `ParametricPlot`, `ListPlot`. Đồ thị **mở trong trình duyệt**, không mở cửa sổ Java.

```java
import org.matheclipse.core.expression.F;

public static void main(String[] args) throws Exception {
    // ... setProperty, tạo util ...
    F.show(util.eval("Plot({Log(x^2 + 3*x), D(Log(x^2 + 3*x), x)}, {x, 0.1, 5})"));
}
```

| Phần | Ý nghĩa |
|---|---|
| `{hàm1, hàm2}` | Vẽ nhiều hàm trên cùng một hình, ở đây là $`y`$ và $`y'`$ |
| `{x, 0.1, 5}` | Khoảng vẽ. Chọn $`0.1`$ vì hàm không xác định tại $`0`$ |
| `F.show(...)` | Tạo file HTML tạm và mở bằng trình duyệt |
| `throws Exception` | Vì `show` có thể ném lỗi khi ghi file |

| Muốn vẽ | Lệnh |
|---|---|
| Nhiều hàm | `Plot({Sin(x), Cos(x)}, {x, 0, 2*Pi})` |
| Đường tham số | `ParametricPlot({Cos(t), Sin(t)}, {t, 0, 2*Pi})` |
| Mặt 3D | `Plot3D(Sin(x*y), {x, 0, 3}, {y, 0, 3})` |
| Kéo, phóng to được | `JSXGraph(Plot(Sin(x), {x, 0, 2*Pi}))` |

**Gợi ý khi dạy:** vẽ $`y`$ và $`y'`$ cùng một hình. Chỗ $`y'`$ cắt trục hoành chính là chỗ $`y`$ đạt cực trị.

**Lưu ý:** các kiểu vẽ dùng JavaScript có thể cần thêm module `matheclipse-jsgraphics`. Muốn đồ thị hiện trong cửa sổ Java thì dùng **XChart** hoặc **JFreeChart**, lấy giá trị từ Symja hoặc Commons Math để vẽ.

---

## 11. Tốc độ chạy

Symja chậm chủ yếu ở **lần chạy đầu**:
- Tạo `ExprEvaluator` phải nạp hàng nghìn quy tắc toán học.
- Thư viện lớn, JVM mất thời gian nạp class.
- Lần đầu Java chạy chưa được tối ưu (JIT chưa "nóng").

**Đo thử:**
```java
long t0 = System.currentTimeMillis();
ExprEvaluator util = new ExprEvaluator();
long t1 = System.currentTimeMillis();
util.eval("D(Log(x^2 + 3*x), x)");
long t2 = System.currentTimeMillis();
util.eval("D(Sin(x^2), x)");
long t3 = System.currentTimeMillis();

System.out.println("Khởi tạo:   " + (t1 - t0) + " ms");
System.out.println("Lệnh 1:     " + (t2 - t1) + " ms");
System.out.println("Lệnh 2:     " + (t3 - t2) + " ms");
```

**Cách dùng cho nhanh:**

| Nên | Không nên |
|---|---|
| Tạo `ExprEvaluator` **một lần** (`static`), dùng cho mọi bài | Tạo mới trong vòng lặp hoặc trong từng hàm |
| Gom nhiều bài vào một lần chạy | Mỗi bài một chương trình riêng |
| Chỉ dùng `D(...)` khi không cần rút gọn | Bọc `Simplify` ở mọi chỗ |
| Dùng Commons Math khi cần tính số hàng nghìn lần | Dùng Symja để tính giá trị cho vẽ đồ thị dày điểm |

Khi dạy, nên báo trước cho học sinh là lần chạy đầu phải chờ vài giây, để các em không tưởng chương trình bị treo.

---

## 12. Lỗi thường gặp

| Hiện tượng | Nguyên nhân | Cách sửa |
|---|---|---|
| Dòng đỏ `ERROR StatusLogger Log4j2...` | Log4j không có bộ ghi log | `System.setProperty(...)` trước `new ExprEvaluator()` (mục 4) |
| Dòng đỏ `SLF4J: Failed to load class...` | SLF4J không có bộ ghi log | Thêm `slf4j-nop` vào `pom.xml` (mục 4) |
| `NoClassDefFoundError` | Thiếu .jar phụ | Dùng Maven, hoặc `dependency:copy-dependencies` (mục 2) |
| `import` báo đỏ | Chưa tải thư viện | **Maven → Update Project** |
| Kết quả in nguyên lệnh `D(...)` hoặc `Integrate(...)` | Sai cú pháp hoặc Symja không tính được | Kiểm tra dấu `*`, chữ hoa; tích phân thì thử `NIntegrate` |
| `2x` bị hiểu sai | Thiếu dấu nhân | Viết `2*x` |
| `sin(x)` không tính | Tên hàm viết thường | Viết `Sin(x)` |
| Bài sau ra kết quả lạ | Biến $`u`$, $`v`$ của bài trước còn nhớ | `util.eval("Clear(u, v, du, dv)")` đầu mỗi bài |
| `Log(x^x)` không thành `x*Log(x)` | Symja không tự giả định $`x > 0`$ | Dùng `PowerExpand(...)` |
| Kết quả có `NaN` (Commons Math) | Điểm $`x_0`$ ngoài tập xác định | Chọn $`x_0`$ khác |
| Chạy rất chậm | Tạo `ExprEvaluator` nhiều lần | Tạo một lần, dùng lại (mục 11) |

---

## 13. Mẫu code hoàn chỉnh

Dùng làm khung cho mọi bài tập đạo hàm, tích phân:

```java
package com.example.DerivativeIntegral;

import org.matheclipse.core.eval.ExprEvaluator;
import org.matheclipse.core.interfaces.IExpr;

public class MauSymja {

    static ExprEvaluator util;

    public static void main(String[] args) {
        // 1. Tắt cảnh báo Log4j (trước khi tạo ExprEvaluator)
        System.setProperty("log4j2.loggerContextFactory",
                "org.apache.logging.log4j.simple.SimpleLoggerContextFactory");

        // 2. Tạo bộ tính toán MỘT LẦN
        util = new ExprEvaluator();

        // 3. Đạo hàm
        in("y' của ln(x^2 + 3x)", "D(Log(x^2 + 3*x), x)");
        in("y'' của x.e^x",        "D(x*Exp(x), {x, 2})");
        in("y'(1) của ln(x^2+3x)", "D(Log(x^2 + 3*x), x) /. x -> 1");

        // 4. Tích phân
        in("Nguyên hàm x.cos x",   "Integrate(x*Cos(x), x)");
        in("Tích phân sin, 0->pi", "Integrate(Sin(x), {x, 0, Pi})");

        // 5. Kiểm tra đáp án
        kiemTra("x^x", "x^x*(Log(x) + 1)");
    }

    static void in(String moTa, String lenh) {
        System.out.println(moTa + " = " + util.eval(lenh));
    }

    static void kiemTra(String ham, String dapAn) {
        IExpr r = util.eval("PossibleZeroQ(D(" + ham + ", x) - (" + dapAn + "))");
        System.out.println("Kiểm tra (" + ham + ")' = " + dapAn + ": "
                + (r.isTrue() ? "ĐÚNG" : "SAI"));
    }
}
```

---

## 14. Bảng tra lệnh nhanh

| Nhóm | Lệnh | Tác dụng |
|---|---|---|
| **Đạo hàm** | `D(f, x)` | Đạo hàm cấp 1 |
| | `D(f, {x, n})` | Đạo hàm cấp $`n`$ |
| **Tích phân** | `Integrate(f, x)` | Nguyên hàm (không có $`+C`$) |
| | `Integrate(f, {x, a, b})` | Tích phân xác định, chính xác |
| | `NIntegrate(f, {x, a, b})` | Tích phân xác định, tính số |
| **Biến đổi** | `Simplify(e)` | Rút gọn |
| | `Expand(e)` | Khai triển |
| | `Factor(e)` | Phân tích nhân tử |
| | `Together(e)` | Gộp một phân thức |
| | `Cancel(e)` | Rút gọn tử, mẫu |
| | `PowerExpand(e)` | Khai triển lũy thừa, logarit (coi biến dương) |
| **Đa thức** | `PolynomialQuotient(p, q, x)` | Thương phép chia đa thức |
| | `PolynomialRemainder(p, q, x)` | Dư phép chia đa thức |
| **Thay thế** | `e /. x -> a` | Thay $`x`$ bằng $`a`$ |
| **Biến** | `u = ...` | Gán biến |
| | `Clear(u, v)` | Xóa biến |
| **So sánh** | `PossibleZeroQ(a - b)` | Kiểm tra $`a = b`$ |
| **Vẽ** | `Plot(f, {x, a, b})` | Đồ thị 2D |
| | `Plot3D(f, {x, a, b}, {y, c, d})` | Mặt 3D |
| | `F.show(...)` (Java) | Mở đồ thị trong trình duyệt |
| **Java** | `new ExprEvaluator()` | Tạo bộ tính toán |
| | `util.eval("...")` | Tính, trả về `IExpr` |
| | `kq.isTrue()` | Đổi kết quả `True/False` sang `boolean` |