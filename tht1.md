# 20 BÀI LUYỆN TẬP SỐ HỌC VỚI PYTHON

**Ôn thi Tin học trẻ** — Cấp số cộng · Cấp số nhân · UCLN · BCNN · Chia hết · Các loại số

---

## Quy ước chung

- Đọc dữ liệu từ bàn phím (input chuẩn), in kết quả ra màn hình (output chuẩn).
- Các số trên cùng một dòng cách nhau bởi **một dấu cách**.
- Giới hạn thời gian: **1 giây / test**.
- Trong bảng test, mỗi ô `code` là **một dòng**; dòng mới được thể hiện bằng xuống dòng trong ô.
- Cột **Loại**:
  -  **Cơ bản** — test thông thường, giống ví dụ.
  -  **Biên** — giá trị nhỏ nhất / lớn nhất, trường hợp đặc biệt (n = 1, hai số bằng nhau, kết quả bằng 0…).
  -  **Bẫy** — test được thiết kế để "bắt" lỗi hay gặp: dùng `/` thay `//`, dùng `sqrt`/`log` số thực, vòng lặp quá chậm, quên số âm…

## Bảng tổng hợp

| Bài | Tên bài | Chủ đề chính | Mức độ |
|---|---|---|---|
| 1 | Khán đài sân vận động | Cấp số cộng |  |
| 2 | Nuôi cấy vi khuẩn | Cấp số nhân |  |
| 3 | Vé số may mắn | Chia hết, đếm trong đoạn |  |
| 4 | Lát gạch | UCLN |  |
| 5 | Hai ngọn hải đăng | BCNN |  |
| 6 | Mã khóa nguyên tố | Số nguyên tố |  |
| 7 | Gấp giấy lên Mặt Trăng | Cấp số nhân |  |
| 8 | Dãy số đều đặn | Cấp số cộng, sắp xếp |  |
| 9 | Số hoàn hảo | Ước số, các loại số |  |
| 10 | Số chính phương trong đoạn | Số chính phương |  |
| 11 | Số khổng lồ | Dấu hiệu chia hết |  |
| 12 | Chia quà Trung thu | UCLN của dãy |  |
| 13 | Bến xe buýt | BCNN của dãy |  |
| 14 | Mảnh giấy rách | Cấp số cộng |  |
| 15 | Cộng phân số | UCLN, BCNN |  |
| 16 | Dãy nhân | Cấp số nhân, phân số |  |
| 17 | Fizz Buzz | Chia hết, BCNN, bao hàm – loại trừ |  |
| 18 | Số nguyên tố đối xứng | Sàng Eratosthenes, số đối xứng |  |
| 19 | Chia nhóm hai đội | Ước chung |  |
| 20 | Cặp số bí ẩn | UCLN & BCNN |  |

 Dễ ·  Trung bình ·  Khá

---

## Bài 1. Khán đài sân vận động 

**Chủ đề:** Cấp số cộng

Khán đài sân vận động của trường có **n** hàng ghế xếp theo bậc thang. Hàng thứ nhất (gần sân nhất) có **a** ghế, mỗi hàng phía sau có nhiều hơn hàng ngay trước nó đúng **d** ghế.

Ban tổ chức cần biết **hàng cuối cùng** có bao nhiêu ghế (để đặt băng rôn) và **cả khán đài** có tổng cộng bao nhiêu ghế (để in vé).

**Input:** Một dòng gồm ba số nguyên `a d n`.

**Output:** Một dòng gồm hai số: số ghế ở hàng cuối và tổng số ghế.

**Giới hạn:** 1 ≤ a ≤ 10⁹; 0 ≤ d ≤ 10⁹; 1 ≤ n ≤ 10⁹.

**Ví dụ:**

```
Input:  5 3 4
Output: 14 38
```

*Giải thích:* Các hàng có 5, 8, 11, 14 ghế. Hàng cuối có 14 ghế, tổng 5 + 8 + 11 + 14 = 38.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `5 3 4` | `14 38` |  | Ví dụ đề bài |
| 2 | `1 2 10` | `19 100` |  | Tổng 10 số lẻ đầu tiên |
| 3 | `1 1 100` | `100 5050` |  | Bài toán Gauss 1 + 2 + … + 100 |
| 4 | `10 0 5` | `10 50` |  | d = 0, mọi hàng bằng nhau |
| 5 | `7 4 1` | `7 7` |  | n = 1, chỉ có một hàng |
| 6 | `3 2 1000000000` | `2000000001 1000000002000000000` |  | n rất lớn → không được dùng vòng lặp |
| 7 | `1000000000 1000000000 1000000000` | `1000000000000000000 500000000500000000000000000` |  | Mọi giá trị lớn nhất → dùng `/` sẽ sai số |

---

## Bài 2. Nuôi cấy vi khuẩn 

**Chủ đề:** Cấp số nhân

Phòng thí nghiệm nuôi một bình vi khuẩn. Ngày thứ nhất bình có **a** con. Mỗi ngày sau đó, số vi khuẩn **gấp q lần** ngày hôm trước. Mỗi tối, nhà khoa học ghi số vi khuẩn của ngày hôm đó vào sổ.

Sau **n** ngày, hãy cho biết số vi khuẩn của **ngày thứ n** và **tổng tất cả các số** đã ghi trong sổ.

**Input:** Một dòng gồm ba số nguyên `a q n`.

**Output:** Một dòng gồm hai số: số vi khuẩn ngày thứ n và tổng các số đã ghi.

**Giới hạn:** 1 ≤ a ≤ 1000; 1 ≤ q ≤ 10; 1 ≤ n ≤ 60. *(Kết quả có thể rất lớn — Python xử lý được số nguyên lớn.)*

**Ví dụ:**

```
Input:  3 2 5
Output: 48 93
```

*Giải thích:* Sổ ghi 3, 6, 12, 24, 48. Ngày thứ 5 có 48 con; tổng = 93.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `3 2 5` | `48 93` |  | Ví dụ đề bài |
| 2 | `2 3 4` | `54 80` |  | Công bội 3 |
| 3 | `7 1 10` | `7 70` |  | q = 1 → công thức tổng chia cho (q − 1) = 0 |
| 4 | `5 10 1` | `5 5` |  | n = 1 |
| 5 | `1 2 60` | `576460752303423488 1152921504606846975` |  | 2⁵⁹ và 2⁶⁰ − 1 |
| 6 | `1000 10 60` | `100000000000000000000000000000000000000000000000000000000000000 111111111111111111111111111111111111111111111111111111111111000` |  | Kết quả rất lớn |

---

## Bài 3. Vé số may mắn 

**Chủ đề:** Chia hết

Ở hội chợ, các vé được đánh số liên tiếp từ **L** đến **R**. Một vé được gọi là **may mắn** nếu số trên vé chia hết cho **k**. Hỏi có bao nhiêu vé may mắn?

**Input:** Một dòng gồm ba số nguyên `L R k`.

**Output:** Số vé may mắn.

**Giới hạn:** 1 ≤ L ≤ R ≤ 10¹⁸; 1 ≤ k ≤ 10¹⁸.

**Ví dụ:**

```
Input:  1 10 3
Output: 3
```

*Giải thích:* Các vé may mắn là 3, 6, 9.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `1 10 3` | `3` |  | Ví dụ đề bài |
| 2 | `12 18 6` | `2` |  | Cả L và R đều chia hết cho k (12 và 18) |
| 3 | `5 5 5` | `1` |  | L = R và chia hết |
| 4 | `7 7 5` | `0` |  | L = R và không chia hết |
| 5 | `10 20 100` | `0` |  | k lớn hơn R |
| 6 | `1 1000000000000000000 1` | `1000000000000000000` |  | k = 1, đoạn cực lớn → không được duyệt |
| 7 | `1 1000000000000000000 7` | `142857142857142857` |  | Đoạn cực lớn |
| 8 | `999999999999999999 1000000000000000000 1000000000000000000` | `1` |  | k = R = 10¹⁸ |

---

## Bài 4. Lát gạch 

**Chủ đề:** Ước chung lớn nhất (UCLN)

Nền một căn phòng hình chữ nhật kích thước **a × b** (cm). Bác thợ muốn lát kín nền bằng các viên gạch **hình vuông giống hệt nhau**, cạnh là số nguyên (cm), **không phải cắt** viên nào. Để đỡ công, bác chọn loại gạch **to nhất** có thể.

Hãy cho biết cạnh viên gạch và số viên gạch cần dùng.

**Input:** Một dòng gồm hai số nguyên `a b`.

**Output:** Một dòng gồm hai số: cạnh viên gạch và số viên gạch.

**Giới hạn:** 1 ≤ a, b ≤ 10⁹.

**Ví dụ:**

```
Input:  12 18
Output: 6 6
```

*Giải thích:* Gạch cạnh 6 cm; chiều 12 xếp được 2 viên, chiều 18 xếp được 3 viên → 6 viên.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `12 18` | `6 6` |  | Ví dụ đề bài |
| 2 | `5 20` | `5 4` |  | Một số chia hết cho số kia |
| 3 | `7 7` | `7 1` |  | Phòng hình vuông, a = b |
| 4 | `13 17` | `1 221` |  | Hai số nguyên tố cùng nhau |
| 5 | `1 1000000000` | `1 1000000000` |  | a = 1 |
| 6 | `1000000000 999999999` | `1 999999999000000000` |  | Số lớn, hai số liên tiếp → Euclid phải chạy nhanh |
| 7 | `1000000000 1000000000` | `1000000000 1` |  | Giá trị lớn nhất, a = b |

---

## Bài 5. Hai ngọn hải đăng 

**Chủ đề:** Bội chung nhỏ nhất (BCNN)

Trên bờ biển có hai ngọn hải đăng. Ngọn A cứ **a** giây chớp sáng một lần, ngọn B cứ **b** giây chớp sáng một lần. Tại **giây 0**, cả hai cùng chớp.

Hãy cho biết:
1. Lần đầu tiên **sau giây 0** hai ngọn cùng chớp là giây thứ mấy?
2. Từ giây 1 đến giây **T** (tính cả giây T), hai ngọn cùng chớp bao nhiêu lần?

**Input:** Một dòng gồm ba số nguyên `a b T`.

**Output:** Dòng 1: đáp án câu 1. Dòng 2: đáp án câu 2.

**Giới hạn:** 1 ≤ a, b ≤ 10⁹; 1 ≤ T ≤ 10¹⁸.

**Ví dụ:**

```
Input:
4 6 30
Output:
12
2
```

*Giải thích:* Hai ngọn cùng chớp ở giây 12, 24, 36… Trong [1, 30] có 2 lần (12 và 24).

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `4 6 30` | `12`<br>`2` |  | Ví dụ đề bài |
| 2 | `3 9 27` | `9`<br>`3` |  | b chia hết cho a |
| 3 | `5 5 20` | `5`<br>`4` |  | a = b |
| 4 | `7 11 50` | `77`<br>`0` |  | BCNN > T → 0 lần |
| 5 | `6 8 24` | `24`<br>`1` |  | T đúng bằng BCNN (tính cả giây T) |
| 6 | `1 1 1` | `1`<br>`1` |  | Giá trị nhỏ nhất |
| 7 | `1000000000 999999999 1000000000000000000` | `999999999000000000`<br>`1` |  | Số lớn → BCNN = a // UCLN × b |

---

## Bài 6. Mã khóa nguyên tố 

**Chủ đề:** Số nguyên tố

Chiếc két sắt bí mật chỉ mở khi mã khóa là một **số nguyên tố**. Cho mã khóa **n**, hãy kiểm tra xem két có mở được không.

*Nhắc lại:* Số nguyên tố là số tự nhiên **lớn hơn 1**, chỉ có đúng hai ước là 1 và chính nó.

**Input:** Một số nguyên `n`.

**Output:** `YES` nếu n là số nguyên tố, ngược lại `NO`.

**Giới hạn:** 0 ≤ n ≤ 10¹².

**Ví dụ:**

```
Input:  7
Output: YES
```

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `7` | `YES` |  | Ví dụ đề bài |
| 2 | `0` | `NO` |  | 0 không phải số nguyên tố |
| 3 | `1` | `NO` |  | 1 không phải số nguyên tố |
| 4 | `2` | `YES` |  | Số nguyên tố chẵn duy nhất |
| 5 | `9` | `NO` |  | 9 = 3²: vòng lặp phải xét cả i × i = n |
| 6 | `999999999989` | `YES` |  | Số nguyên tố lớn → chỉ duyệt đến √n |
| 7 | `999966000289` | `NO` |  | = 999983², ước nhỏ nhất đúng bằng √n |
| 8 | `1000000000000` | `NO` |  | Giá trị lớn nhất |

---

## Bài 7. Gấp giấy lên Mặt Trăng 

**Chủ đề:** Cấp số nhân

Một tờ giấy dày **t** micromet (µm). Mỗi lần gấp, tờ giấy được gấp thành **q** lớp chồng lên nhau nên độ dày tăng **gấp q lần**. Hỏi cần gấp **ít nhất bao nhiêu lần** để độ dày đạt **ít nhất H** micromet?

*Thú vị:* Khoảng cách Trái Đất – Mặt Trăng ≈ 384 400 km = 384 400 000 000 000 µm. Một tờ giấy dày 100 µm chỉ cần gấp đôi **42 lần** là "chạm" tới Mặt Trăng!

**Input:** Một dòng gồm ba số nguyên `t H q`.

**Output:** Số lần gấp ít nhất (có thể bằng 0).

**Giới hạn:** 1 ≤ t, H ≤ 10¹⁸; 2 ≤ q ≤ 10.

**Ví dụ:**

```
Input:  1 10 2
Output: 4
```

*Giải thích:* Độ dày lần lượt 1 → 2 → 4 → 8 → 16. Sau 4 lần gấp thì 16 ≥ 10.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `1 10 2` | `4` |  | Ví dụ đề bài |
| 2 | `100 384400000000000 2` | `42` |  | Lên Mặt Trăng |
| 3 | `2 17 3` | `2` |  | Gấp ba: 2 → 6 → 18 |
| 4 | `1 8 2` | `3` |  | H đúng bằng t × qᵏ (dấu ≥) |
| 5 | `50 50 2` | `0` |  | t = H, không cần gấp |
| 6 | `1000 5 3` | `0` |  | t > H |
| 7 | `1 125 5` | `3` |  | Dùng `log` số thực cho ra 3.0000000000000004 → làm tròn lên thành 4 (sai) |
| 8 | `1 1000000000000000000 2` | `60` |  | H lớn nhất |
| 9 | `1 1000000000000000000 10` | `18` |  | H = 10¹⁸ đúng bằng lũy thừa |

---

## Bài 8. Dãy số đều đặn 

**Chủ đề:** Cấp số cộng, sắp xếp

Cho một dãy gồm **n** số nguyên. Hãy cho biết:
- In `YES` nếu dãy **theo đúng thứ tự đã cho** là một cấp số cộng;
- In `SORT` nếu dãy chưa phải cấp số cộng, nhưng **sau khi sắp xếp tăng dần** thì trở thành cấp số cộng;
- In `NO` nếu không thể.

*Lưu ý:* Dãy có 1 hoặc 2 phần tử luôn là cấp số cộng. Công sai có thể âm hoặc bằng 0.

**Input:** Dòng 1: số nguyên `n`. Dòng 2: n số nguyên a₁, a₂, …, aₙ.

**Output:** `YES`, `SORT` hoặc `NO`.

**Giới hạn:** 1 ≤ n ≤ 10⁵; |aᵢ| ≤ 10⁹.

**Ví dụ:**

```
Input:
4
7 1 4 10
Output:
SORT
```

*Giải thích:* Sắp xếp lại được 1, 4, 7, 10 — cấp số cộng với công sai 3.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `4`<br>`7 1 4 10` | `SORT` |  | Ví dụ đề bài |
| 2 | `5`<br>`1 3 5 7 9` | `YES` |  | Cấp số cộng sẵn |
| 3 | `4`<br>`1 2 4 8` | `NO` |  | Cấp số nhân, không phải cấp số cộng |
| 4 | `1`<br>`42` | `YES` |  | n = 1 |
| 5 | `2`<br>`100 -5` | `YES` |  | n = 2 luôn đúng |
| 6 | `5`<br>`3 3 3 3 3` | `YES` |  | Công sai bằng 0 |
| 7 | `4`<br>`10 7 4 1` | `YES` |  | Giảm dần (công sai âm) vẫn là `YES`, không phải `SORT` |
| 8 | `3`<br>`2 2 3` | `NO` |  | Có phần tử trùng nhau |
| 9 | `4`<br>`-3 3 -1 1` | `SORT` |  | Có số âm |

---

## Bài 9. Số hoàn hảo 

**Chủ đề:** Ước số, các loại số

Người Hy Lạp cổ đại phân loại số nguyên dương **n** dựa vào **s** — tổng các **ước thực sự** của n (các ước dương **nhỏ hơn** n):
- s = n → n là **số hoàn hảo** (ví dụ 6 = 1 + 2 + 3);
- s < n → n là **số thiếu**;
- s > n → n là **số dư**.

**Input:** Một số nguyên `n`.

**Output:** Dòng 1: tổng s. Dòng 2: `HOAN HAO`, `THIEU` hoặc `DU`.

**Giới hạn:** 1 ≤ n ≤ 10¹².

**Ví dụ:**

```
Input:
12
Output:
16
DU
```

*Giải thích:* Ước thực sự của 12: 1, 2, 3, 4, 6 → tổng 16 > 12.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `12` | `16`<br>`DU` |  | Ví dụ đề bài |
| 2 | `6` | `6`<br>`HOAN HAO` |  | Số hoàn hảo nhỏ nhất |
| 3 | `13` | `1`<br>`THIEU` |  | Số nguyên tố |
| 4 | `1` | `0`<br>`THIEU` |  | n = 1 không có ước thực sự |
| 5 | `16` | `15`<br>`THIEU` |  | Số chính phương: không cộng ước 4 hai lần |
| 6 | `36` | `55`<br>`DU` |  | Số chính phương: không cộng ước 6 hai lần |
| 7 | `8128` | `8128`<br>`HOAN HAO` |  | Số hoàn hảo thứ tư |
| 8 | `137438691328` | `137438691328`<br>`HOAN HAO` |  | Số lớn → chỉ duyệt đến √n |
| 9 | `999999999989` | `1`<br>`THIEU` |  | Số nguyên tố lớn |

---

## Bài 10. Số chính phương trong đoạn 

**Chủ đề:** Số chính phương

Số chính phương là bình phương của một số nguyên (1, 4, 9, 16, …). Đếm số lượng số chính phương trong đoạn **[L, R]**.

**Input:** Một dòng gồm hai số nguyên `L R`.

**Output:** Số lượng số chính phương trong đoạn.

**Giới hạn:** 1 ≤ L ≤ R ≤ 10¹⁸.

**Ví dụ:**

```
Input:  1 10
Output: 3
```

*Giải thích:* Các số chính phương là 1, 4, 9.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `1 10` | `3` |  | Ví dụ đề bài |
| 2 | `1 1` | `1` |  | Đoạn nhỏ nhất |
| 3 | `16 16` | `1` |  | L = R là số chính phương |
| 4 | `17 24` | `0` |  | Không có số nào |
| 5 | `2 3` | `0` |  | Không có số nào |
| 6 | `1 1000000000000000000` | `1000000000` |  | Đoạn cực lớn → không được duyệt |
| 7 | `999999998000000001 999999999999999999` | `1` |  | L = 999999999², `sqrt` số thực cho kết quả sai |
| 8 | `999999999999999999 1000000000000000000` | `1` |  | `int(math.sqrt(10¹⁸ − 1))` ra 10⁹ (sai) |

---

## Bài 11. Số khổng lồ 

**Chủ đề:** Dấu hiệu chia hết

Cho một số tự nhiên **N** rất lớn, có thể tới **100 000 chữ số**. Hãy cho biết N chia hết cho những số nào trong tập **{2, 3, 4, 5, 9, 11}**.

**Input:** Một dòng chứa số `N` (không có chữ số 0 vô nghĩa ở đầu, trừ khi N = 0).

**Output:** Các số trong tập {2, 3, 4, 5, 9, 11} mà N chia hết, in theo thứ tự tăng dần, cách nhau một dấu cách. Nếu không chia hết cho số nào, in `KHONG`.

**Giới hạn:** N có từ 1 đến 10⁵ chữ số.

**Ví dụ:**

```
Input:  1980
Output: 2 3 4 5 9 11
```

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `1980` | `2 3 4 5 9 11` |  | Ví dụ đề bài: chia hết cả 6 số |
| 2 | `12` | `2 3 4` |  | Thông thường |
| 3 | `10` | `2 5` |  | Thông thường |
| 4 | `121` | `11` |  | Chỉ chia hết cho 11 |
| 5 | `7` | `KHONG` |  | Không chia hết số nào |
| 6 | `0` | `2 3 4 5 9 11` |  | 0 chia hết cho mọi số |
| 7 | `4` | `2 4` |  | Chỉ có 1 chữ số, dấu hiệu chia hết cho 4 |
| 8 | `5` | `5` |  | Một chữ số |
| 9 | `918082` | `2 11` |  | Tổng đan dấu bị âm (−22) |
| 10 | *(chuỗi gồm 100 000 chữ số 9)* | `3 9 11` |  | `int(N)` báo lỗi vượt 4300 chữ số trên Python 3.11+ → phải dùng dấu hiệu chia hết |

*Sinh test 10 bằng lệnh:* `print("9" * 100000)`

---

## Bài 12. Chia quà Trung thu 

**Chủ đề:** UCLN của dãy số

Lớp có **n** loại quà Trung thu, loại thứ i có **aᵢ** món. Cô giáo muốn chia **hết** số quà vào các túi **giống hệt nhau** (mỗi túi có cùng số món của từng loại), không thừa món nào. Cô muốn số túi **nhiều nhất**.

**Input:** Dòng 1: số nguyên `n`. Dòng 2: n số nguyên a₁, a₂, …, aₙ.

**Output:** Dòng 1: số túi nhiều nhất. Dòng 2: n số — số món của từng loại trong một túi.

**Giới hạn:** 1 ≤ n ≤ 10⁵; 1 ≤ aᵢ ≤ 10⁹.

**Ví dụ:**

```
Input:
3
12 18 24
Output:
6
2 3 4
```

*Giải thích:* Chia thành 6 túi, mỗi túi có 2 món loại 1, 3 món loại 2, 4 món loại 3.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `3`<br>`12 18 24` | `6`<br>`2 3 4` |  | Ví dụ đề bài |
| 2 | `4`<br>`100 75 50 25` | `25`<br>`4 3 2 1` |  | Thông thường |
| 3 | `1`<br>`15` | `15`<br>`1` |  | n = 1 |
| 4 | `3`<br>`7 7 7` | `7`<br>`1 1 1` |  | Mọi số bằng nhau |
| 5 | `3`<br>`8 9 10` | `1`<br>`8 9 10` |  | UCLN(8, 10) = 2 nhưng UCLN cả dãy = 1 |
| 6 | `2`<br>`1000000000 500000000` | `500000000`<br>`2 1` |  | Số lớn |

---

## Bài 13. Bến xe buýt 

**Chủ đề:** BCNN của dãy số

Bến xe có **n** tuyến xe buýt, tất cả cùng xuất bến lúc **06:00**. Tuyến thứ i cứ **aᵢ** phút lại có một chuyến xuất bến.

Hỏi sau **ít nhất bao nhiêu phút** thì tất cả các tuyến lại cùng xuất bến? Nếu thời điểm đó vẫn **trong ngày** (trước 24:00), hãy in giờ dạng `HH:MM`; ngược lại in `NGAY KHAC`.

**Input:** Dòng 1: số nguyên `n`. Dòng 2: n số nguyên a₁, a₂, …, aₙ.

**Output:** Dòng 1: số phút. Dòng 2: giờ `HH:MM` hoặc `NGAY KHAC`.

**Giới hạn:** 1 ≤ n ≤ 100; 1 ≤ aᵢ ≤ 10⁴. *(Số phút có thể rất lớn.)*

**Ví dụ:**

```
Input:
3
10 15 20
Output:
60
07:00
```

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `3`<br>`10 15 20` | `60`<br>`07:00` |  | Ví dụ đề bài |
| 2 | `4`<br>`4 6 8 12` | `24`<br>`06:24` |  | BCNN ≠ tích các số |
| 3 | `3`<br>`8 9 15` | `360`<br>`12:00` |  | Đúng giữa trưa |
| 4 | `1`<br>`45` | `45`<br>`06:45` |  | n = 1 |
| 5 | `3`<br>`12 12 12` | `12`<br>`06:12` |  | Mọi số bằng nhau |
| 6 | `2`<br>`1 1` | `1`<br>`06:01` |  | Phút có 1 chữ số → phải in `06:01` |
| 7 | `2`<br>`1079 1` | `1079`<br>`23:59` |  | Phút cuối cùng trong ngày |
| 8 | `2`<br>`1080 1080` | `1080`<br>`NGAY KHAC` |  | Đúng 24:00 → đã sang ngày khác |
| 9 | `25`<br>`2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97` | `2305567963945518424753102147331756070`<br>`NGAY KHAC` |  | 25 số nguyên tố → kết quả cực lớn |

---

## Bài 14. Mảnh giấy rách 

**Chủ đề:** Cấp số cộng

Bạn Minh viết một cấp số cộng gồm **toàn số nguyên** lên tờ giấy, nhưng tờ giấy bị rách. Minh chỉ còn đọc được: số hạng thứ **p** bằng **x** và số hạng thứ **q** bằng **y**.

Hãy tìm số hạng đầu u₁, công sai d và số hạng thứ **m** của cấp số cộng đó. Nếu **không tồn tại** cấp số cộng toàn số nguyên nào thỏa mãn, in `KHONG`.

**Input:** Một dòng gồm năm số nguyên `p x q y m`.

**Output:** Nếu tồn tại: dòng 1 gồm `u₁ d`, dòng 2 là uₘ. Ngược lại in `KHONG`.

**Giới hạn:** 1 ≤ p < q ≤ 10⁹; |x|, |y| ≤ 10¹⁸; 1 ≤ m ≤ 10⁹.

**Ví dụ:**

```
Input:
2 5 5 14 10
Output:
2 3
29
```

*Giải thích:* Từ u₂ = 5 đến u₅ = 14 có 3 bước, mỗi bước tăng (14 − 5) / 3 = 3. Vậy u₁ = 2, d = 3, u₁₀ = 2 + 9 × 3 = 29.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `2 5 5 14 10` | `2 3`<br>`29` |  | Ví dụ đề bài |
| 2 | `3 10 7 -2 1` | `16 -3`<br>`16` |  | Công sai âm, m = 1 |
| 3 | `1 4 3 9 5` | `KHONG` |  | Công sai 5/2 không nguyên |
| 4 | `2 -7 4 -8 3` | `KHONG` |  | Công sai −1/2: kiểm tra chia hết với số âm |
| 5 | `4 7 9 7 100` | `7 0`<br>`7` |  | Công sai bằng 0 |
| 6 | `5 0 6 1 1` | `-4 1`<br>`-4` |  | u₁ âm |
| 7 | `1 0 1000000000 999999999000000000 1000000000` | `0 1000000000`<br>`999999999000000000` |  | Số lớn → không dùng `/` |

---

## Bài 15. Cộng phân số 

**Chủ đề:** UCLN, BCNN, phân số tối giản

Tính tổng hai phân số **a/b + c/d** và in kết quả dưới dạng **phân số tối giản**.

**Input:** Một dòng gồm bốn số nguyên `a b c d`.

**Output:** Kết quả dạng `p/q` tối giản với **q > 0**. Nếu kết quả là số nguyên (q = 1) thì chỉ in `p`.

**Giới hạn:** |a|, |c| ≤ 10⁹; 1 ≤ |b|, |d| ≤ 10⁹ (mẫu số có thể âm).

**Ví dụ:**

```
Input:  1 6 1 3
Output: 1/2
```

*Giải thích:* 1/6 + 1/3 = 1/6 + 2/6 = 3/6 = 1/2.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `1 6 1 3` | `1/2` |  | Ví dụ đề bài, cần rút gọn |
| 2 | `1 2 1 3` | `5/6` |  | Đã tối giản |
| 3 | `1 2 1 2` | `1` |  | Kết quả là số nguyên |
| 4 | `1 3 -1 3` | `0` |  | Kết quả bằng 0 |
| 5 | `0 5 0 7` | `0` |  | Cả hai tử bằng 0 |
| 6 | `3 -4 1 4` | `-1/2` |  | Mẫu âm → dấu âm phải đưa lên tử |
| 7 | `-2 -3 1 6` | `5/6` |  | Cả tử và mẫu âm |
| 8 | `1000000000 999999999 1 999999998` | `999999998999999999/999999997000000002` |  | Số lớn |

---

## Bài 16. Dãy nhân 

**Chủ đề:** Cấp số nhân, phân số

Cho dãy **n** số nguyên **khác 0**. Hãy kiểm tra dãy (theo đúng thứ tự đã cho) có phải **cấp số nhân** không. Nếu có, in thêm **công bội** dưới dạng phân số tối giản.

*Lưu ý:* Công bội có thể là phân số (ví dụ 81, 27, 9, 3 có công bội 1/3) hoặc số âm.

**Input:** Dòng 1: số nguyên `n`. Dòng 2: n số nguyên a₁, a₂, …, aₙ.

**Output:** Nếu là cấp số nhân: dòng 1 in `YES`, dòng 2 in công bội dạng `p/q` tối giản với q > 0 (nếu q = 1 chỉ in `p`). Ngược lại in `NO`.

**Giới hạn:** 2 ≤ n ≤ 10⁵; 1 ≤ |aᵢ| ≤ 10⁹.

**Ví dụ:**

```
Input:
4
81 27 9 3
Output:
YES
1/3
```

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `4`<br>`81 27 9 3` | `YES`<br>`1/3` |  | Ví dụ đề bài, công bội phân số |
| 2 | `4`<br>`3 6 12 24` | `YES`<br>`2` |  | Công bội nguyên |
| 3 | `4`<br>`1 2 4 7` | `NO` |  | Không phải cấp số nhân |
| 4 | `3`<br>`2 -6 18` | `YES`<br>`-3` |  | Công bội âm |
| 5 | `2`<br>`6 4` | `YES`<br>`2/3` |  | n = 2 luôn đúng |
| 6 | `5`<br>`5 5 5 5 5` | `YES`<br>`1` |  | Công bội 1 |
| 7 | `4`<br>`8 -12 18 -27` | `YES`<br>`-3/2` |  | Công bội là phân số âm |
| 8 | `3`<br>`-4 -2 -1` | `YES`<br>`1/2` |  | Toàn số âm, công bội dương |
| 9 | `3`<br>`999999937 999999938 999999939` | `NO` |  | So sánh `a[1]/a[0] == a[2]/a[1]` bằng số thực cho kết quả sai |

---

## Bài 17. Fizz Buzz 

**Chủ đề:** Chia hết, BCNN, nguyên lý bao hàm – loại trừ

Cả lớp chơi trò Fizz Buzz: lần lượt đếm từ 1 đến **N**. Với mỗi số:
- chia hết cho **cả a và b** → hô `FizzBuzz`;
- chỉ chia hết cho **a** → hô `Fizz`;
- chỉ chia hết cho **b** → hô `Buzz`;
- còn lại → đọc số đó.

Đếm số lần hô `Fizz`, `Buzz`, `FizzBuzz` và số lần đọc số.

**Input:** Một dòng gồm ba số nguyên `N a b`.

**Output:** Một dòng gồm bốn số: số lần `Fizz`, `Buzz`, `FizzBuzz`, đọc số.

**Giới hạn:** 1 ≤ N, a, b ≤ 10¹⁸.

**Ví dụ:**

```
Input:  15 3 5
Output: 4 2 1 8
```

*Giải thích:* Fizz: 3, 6, 9, 12. Buzz: 5, 10. FizzBuzz: 15. Còn lại 8 số.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `15 3 5` | `4 2 1 8` |  | Ví dụ đề bài |
| 2 | `100 3 5` | `27 14 6 53` |  | Trò chơi gốc |
| 3 | `12 2 4` | `3 0 3 6` |  | b là bội của a → BCNN = 4, không phải 8 |
| 4 | `10 2 2` | `0 0 5 5` |  | a = b |
| 5 | `7 1 1` | `0 0 7 0` |  | Mọi số đều là FizzBuzz |
| 6 | `1 7 9` | `0 0 0 1` |  | N = 1 |
| 7 | `1000000000000000000 2 3` | `333333333333333334 166666666666666667 166666666666666666 333333333333333333` |  | N cực lớn → không được duyệt |
| 8 | `1000000000000000000 1000000000000000000 999999999999999999` | `1 1 0 999999999999999998` |  | BCNN vượt N rất xa |

---

## Bài 18. Số nguyên tố đối xứng 

**Chủ đề:** Sàng Eratosthenes, số đối xứng

Một số được gọi là **nguyên tố đối xứng** nếu nó vừa là số nguyên tố, vừa đọc xuôi hay ngược đều giống nhau (ví dụ 11, 101, 131).

Hãy đếm số lượng số nguyên tố đối xứng trong đoạn **[1, N]** và cho biết số **lớn nhất** trong chúng.

**Input:** Một số nguyên `N`.

**Output:** Dòng 1: số lượng. Dòng 2: số nguyên tố đối xứng lớn nhất không vượt quá N, hoặc `-1` nếu không có.

**Giới hạn:** 1 ≤ N ≤ 10⁶.

**Ví dụ:**

```
Input:
20
Output:
5
11
```

*Giải thích:* Các số là 2, 3, 5, 7, 11.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `20` | `5`<br>`11` |  | Ví dụ đề bài |
| 2 | `1000` | `20`<br>`929` |  | Thông thường |
| 3 | `1` | `0`<br>`-1` |  | Không có số nào |
| 4 | `2` | `1`<br>`2` |  | Số nguyên tố nhỏ nhất |
| 5 | `10` | `4`<br>`7` |  | Chỉ có số 1 chữ số |
| 6 | `11` | `5`<br>`11` |  | N đúng bằng một số cần đếm |
| 7 | `100` | `5`<br>`11` |  | 22, 33, …, 99 đều không phải số nguyên tố; 101 > 100 |
| 8 | `1000000` | `113`<br>`98689` |  | N lớn nhất → cần sàng, kiểm tra từng số sẽ chậm |

---

## Bài 19. Chia nhóm hai đội 

**Chủ đề:** Ước chung

Đội tuyển A có **a** học sinh, đội tuyển B có **b** học sinh. Thầy giáo muốn chia **mỗi đội** thành các nhóm có cùng **k** người (giá trị k giống nhau cho cả hai đội), không thừa bạn nào.

Hỏi có bao nhiêu giá trị k thỏa mãn, và **tổng** tất cả các giá trị k đó là bao nhiêu?

**Input:** Một dòng gồm hai số nguyên `a b`.

**Output:** Dòng 1: số giá trị k. Dòng 2: tổng các giá trị k.

**Giới hạn:** 1 ≤ a, b ≤ 10¹².

**Ví dụ:**

```
Input:
12 18
Output:
4
12
```

*Giải thích:* k có thể là 1, 2, 3, 6 → 4 giá trị, tổng 12.

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `12 18` | `4`<br>`12` |  | Ví dụ đề bài |
| 2 | `720 1080` | `24`<br>`1170` |  | UCLN = 360 có nhiều ước |
| 3 | `7 13` | `1`<br>`1` |  | Nguyên tố cùng nhau → chỉ k = 1 |
| 4 | `1 1000000000000` | `1`<br>`1` |  | a = 1 |
| 5 | `36 36` | `9`<br>`91` |  | UCLN là số chính phương → không đếm ước 6 hai lần |
| 6 | `999999999989 999999999989` | `2`<br>`999999999990` |  | UCLN là số nguyên tố lớn |
| 7 | `999966000289 999966000289` | `3`<br>`999967000273` |  | UCLN = 999983² |
| 8 | `1000000000000 1000000000000` | `169`<br>`2499694822171` |  | Giá trị lớn nhất |

---

## Bài 20. Cặp số bí ẩn 

**Chủ đề:** UCLN & BCNN

Thầy giáo đố: *"Có bao nhiêu cặp số nguyên dương (a, b) mà UCLN(a, b) = **G** và BCNN(a, b) = **L**?"*

Cặp (a, b) và (b, a) được tính là **hai cặp khác nhau** nếu a ≠ b.

**Input:** Một dòng gồm hai số nguyên `G L`.

**Output:** Số cặp (a, b) thỏa mãn.

**Giới hạn:** 1 ≤ G, L ≤ 10¹².

**Ví dụ:**

```
Input:  2 12
Output: 4
```

*Giải thích:* Các cặp là (2, 12), (12, 2), (4, 6), (6, 4).

**Test cases:**

| # | Input | Output | Loại | Kiểm tra |
|---|---|---|---|---|
| 1 | `2 12` | `4` |  | Ví dụ đề bài |
| 2 | `1 30030` | `64` |  | 30030 = 2·3·5·7·11·13 |
| 3 | `4 32` | `2` |  | (8, 16) có UCLN 8 chứ không phải 4 → chỉ còn (4, 32), (32, 4) |
| 4 | `5 5` | `1` |  | G = L → chỉ có cặp (5, 5) |
| 5 | `1 1` | `1` |  | Giá trị nhỏ nhất |
| 6 | `3 10` | `0` |  | L không chia hết cho G |
| 7 | `10 7` | `0` |  | L < G |
| 8 | `1 1000000000000` | `4` |  | 10¹² = 2¹²·5¹² nhiều ước nhưng chỉ 4 cặp |
| 9 | `1 200560490130` | `2048` |  | Tích 11 số nguyên tố đầu tiên |
| 10 | `1000000000000 1000000000000` | `1` |  | G = L lớn nhất |
