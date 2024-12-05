#In ra màn hình
print("Ngô Đức Quang")
print("Anime")
#Biến trong python
ten = "Ngô Đức Quang"
tuoi = "18"
chieu_cao = "1.60"
#Kiểu dữ liệu trong python
#Kiểu số:- int: số nguyên (-1, 5, 20); float: số thực (3.14, -2.5)
#Kiểu chuỗi: str: dùng để biểu diễn văn bản ("Hello", `Python`)
#Kiểu Boolean: bool: Chỉ có hai giá trị: True hoặc False
age = "25"
name = "Alice"
is_student = True
#Kiểu danh sách: list: Một tập hợp các giá trị, có thể là các kiểu dữ liệu khác nhau ([1, 2, 3, 'apple'])
#Kiểu tuple: Tương tự như list, nhưng không thể thay đổi giá trị sau khi tạo
#Kiểu dictionary: dict: Một tập hợp các cặp khoá- giá trị ("name":"Alice", "age":{30})
fruits = ["apple", "banana", "orange"]
coordinates = (10, 20)
person = {"name": "Ngô Đức Quang", "age": 18, "city": "Hai Duong"}
#Cách kiểm tra dữ liệu 
'''print(type(x))''' #In ra <class 'int'>
#Các phép toán với biến: +, -, *, /, //(chia lấy phần nguyên), %(lấy dư)
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
#Nhập liệu trong python
ten = input("Nhập tên của bạn: ")
tuoi = input("Bạn bao nhiêu tuổi?")
print("Xin chào,", ten)
print("Năm sau bạn sẽ", int(tuoi) + 1, "tuổi")

so_thuc = float(input("Nhập một số thực: "))
print("Số bạn vừa nhập là:", so_thuc)

#Điều kiện trong python
tuoi = 18
if tuoi >= 18:
    print("Bạn đã đủ tuổi để lái xe")
#Các toán tử trong python: ==(bằng nhau), !=(không bằng nhau), <, >, <=, >=
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")
#elif dùng để kiểm tra nhiều điều kiện khác
diem = 8
if diem >= 9:
    print("Xuất sắc")
elif diem >= 7:
    print("Giỏi")
elif diem >= 5:
    print("Khá")
else:
    print("Cần cố gắng hơn")
#Các toán tử logic: 
#and: Cả hai điều kiện phải đúng
#or: Chỉ cần một trong hai điều kiện đúng
#not: Đảo ngược giá trị của điều kiện
gioi_tinh = "Nam"
tuoi = 20
if gioi_tinh == "nam" and tuoi >= 18:
    print("Bạn là nam và đủ tuổi để đi làm")
    
