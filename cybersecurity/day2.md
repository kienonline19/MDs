## Các lệnh sau để biết ?
1. Tôi đang ở đâu ?
- whoami: tôi là người dùng nào ?
- pwd: hiện tại tôi ở đâu ? - print working directory
- ls: có gì trong thư mục này ? - list
- ls -la: liệt kê thêm các file ẩn (bắt đầu với dấu .) và chi tiết liên quan

2. Di chuyển đến thư mục khác
- cd /: đi tới gốc của cây (hệ thống)
- cd ~: quay trở lại thư mục home của bạn
- cd -: quay lại thư mục trước đó
- cd ..: đi lên một cấp thư mục ? cd - (tìm hiểu chỗ này)

3. Liệt kê các files trong root
- ls /: liệt kê các file/dir trong root
- ls -l /: chi tiết hơn về các files trong root
- tree -L 1 /: hiển thị cấu trúc thư mục cấp 1 ngay bên trong root

4. Nhận dạng hệ thống
- cat /etc/os-release: tên và phiên bản của bản phân phối (distro)
- uname -a: phiên bản và kiến trúc của kernel
- hostname: tên máy của mình

5. Đọc các file cấu hình hệ thống trong /etc
- ls /etc | head -20: liệt kê thư mục etc trong 20 dòng đầu theo thứ tự bảng chữ cái
- cat /etc/hostname: kali

6. awk: in ra nội dung của file văn bản có cấu trúc hàng cột bảng ma trận
- awk '{print $1}' users.txt: in ra cột 1
- awk '{print NR, $1, NF}' users.txt: in ra số thứ tự của dòng các cột tương ứng và số lượng cột trên mỗi dòng
- awk '$2 >= 25 {print NR, $1, $NF}' users.txt: lọc ra những người có tuổi từ 25
- dùng -F: để chỉ ra các cột ngăn cách với nhau = :

7. grep tìm kiếm trên từng dòng