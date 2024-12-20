#Bai 1
year = int(input("Nhập năm: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} là năm nhuận.")
else:
    print(f"{year} không phải là năm nhuận.")

#Bai 2
# Nhập tọa độ điểm M và tâm I cùng bán kính R
x = float(input("Nhập hoành độ x của điểm M: "))
y = float(input("Nhập tung độ y của điểm M: "))
a = float(input("Nhập hoành độ x của tâm I: "))
b = float(input("Nhập tung độ y của tâm I: "))
R = float(input("Nhập bán kính R: "))

# Tính khoảng cách giữa điểm M và tâm I
distance_squared = (x - a) ** 2 + (y - b) ** 2
R_squared = R ** 2

# Kiểm tra điểm M có nằm trong hình tròn không
if distance_squared <= R_squared:
    print(True)  # Điểm M nằm trong hoặc trên hình tròn
else:
    print(False)  # Điểm M nằm ngoài hình tròn

#Bai 3
# Nhập 3 số từ bàn phím
num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ hai: "))
num3 = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất bằng hàm max
max_num = max(num1, num2, num3)

# In ra số lớn nhất
print(f"Số lớn nhất trong ba số là: {max_num}")

#Bai 4
# Nhập vào ba cạnh a, b, c
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra xem có phải là tam giác không
if a + b > c and a + c > b and b + c > a:
    print("a, b, c là bộ ba cạnh của một tam giác.")
    
    # Kiểm tra loại tam giác
    if a == b == c:
        print("Đây là tam giác đều.")
    else:
        if a == b or a == c or b == c:
            print("Đây là tam giác cân.")
        else:
            if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
                print("Đây là tam giác vuông.")
            else:
                print("Đây là tam giác thường.")
else:
    print("a, b, c không phải là bộ ba cạnh của tam giác.")

#Bai 5
# Nhập ký tự từ bàn phím
char = input("Nhập một ký tự: ").lower()

# Kiểm tra xem ký tự có phải là chữ cái không
if char.isalpha() and len(char) == 1:
    if char in "aeiou":
        print(f"{char} là nguyên âm.")
    else:
        print(f"{char} là phụ âm.")
else:
    print("Ký tự không hợp lệ. Vui lòng nhập một ký tự từ a-z hoặc A-Z.")

#Bai 6
# Hiện menu lựa chọn thể loại phim
print("Chọn thể loại phim bạn muốn xem:")
print("1. Phim tình cảm")
print("2. Phim kinh dị")
print("3. Phim hoạt hình")
print("4. Phim khoa học viễn tưởng")

# Nhập lựa chọn từ người dùng
choice = input("Nhập số tương ứng với thể loại phim: ")

if choice == '1':
    print("Bạn đã chọn Phim tình cảm.")
else:
    if choice == '2':
        print("Bạn đã chọn Phim kinh dị.")
    else:
        if choice == '3':
            print("Bạn đã chọn Phim hoạt hình.")
        else:
            if choice == '4':
                print("Bạn đã chọn Phim khoa học viễn tưởng.")
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 4.")
