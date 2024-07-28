# AES

## AES (Advanced Encryption Standard) là một chuẩn mã hóa được thiết kế để thay thế DES (Data Encryption Standard) và được coi là một trong những phương pháp mã hóa đối xứng an toàn và hiệu quả nhất hiện nay. Dưới đây là tổng quan về AES:

### 1. Giới thiệu về AES
+ Tên đầy đủ: Advanced Encryption Standard.
+ Xuất xứ: Được phát triển bởi hai nhà mật mã học người Bỉ là Joan Daemen và Vincent Rijmen. Thuật toán này ban đầu có tên là Rijndael.
+ Chính thức công nhận: Được công nhận là chuẩn mã hóa liên bang của Hoa Kỳ bởi NIST (National Institute of Standards and Technology) vào năm 2001.

### 2. Đặc điểm của AES
+ Loại mã hóa: Mã hóa khối (block cipher).
+ Kích thước khối: 128 bit.
+ Kích thước khóa: AES hỗ trợ ba kích thước khóa: 128, 192, và 256 bit.
+ Số vòng lặp: Phụ thuộc vào độ dài của khóa:
```
10 vòng cho khóa 128 bit.
12 vòng cho khóa 192 bit.
14 vòng cho khóa 256 bit.
```
### 3. Quy trình mã hóa AES
+ AES thực hiện mã hóa qua nhiều vòng lặp, mỗi vòng bao gồm các bước sau:

1. SubBytes: Thay thế từng byte trong khối bằng một byte khác từ một bảng thay thế (S-box).
2. ShiftRows: Dịch chuyển hàng trong ma trận trạng thái.
3. MixColumns: Trộn các cột của ma trận trạng thái (ngoại trừ vòng cuối cùng).
4. AddRoundKey: Thực hiện XOR giữa ma trận trạng thái và khóa vòng.
### 4. Quy trình giải mã AES
+ Quy trình giải mã là quá trình ngược lại của mã hóa và bao gồm các bước sau:

1. InvSubBytes: Thay thế từng byte bằng giá trị ngược từ S-box ngược.
2. InvShiftRows: Dịch chuyển các hàng ngược lại.
3. InvMixColumns: Trộn các cột ngược lại (ngoại trừ vòng cuối cùng).
4. AddRoundKey: Thực hiện XOR giữa ma trận trạng thái và khóa vòng.
### 5. Ưu điểm của AES
+ Bảo mật cao: Được coi là an toàn trước các tấn công hiện tại và được sử dụng rộng rãi trong nhiều ứng dụng bảo mật.
+ Hiệu suất: Hiệu suất cao trên cả phần cứng và phần mềm.
+ Linh hoạt: Hỗ trợ nhiều độ dài khóa khác nhau, phù hợp với các mức độ bảo mật khác nhau.
# 6. Ứng dụng của AES
+ AES được sử dụng trong nhiều lĩnh vực và ứng dụng khác nhau, bao gồm:
1. Bảo mật truyền thông và mạng (ví dụ: TLS/SSL).
2. Bảo mật lưu trữ dữ liệu (ví dụ: mã hóa đĩa cứng).
3. Bảo mật thông tin cá nhân (ví dụ: mã hóa dữ liệu trên các thiết bị di động).

