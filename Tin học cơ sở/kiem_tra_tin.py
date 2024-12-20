# Danh sách cầu thủ
ds_cau_thu = []

# Hàm nhập thông tin cầu thủ
def nhap_cau_thu():
    try:
        ma_ct = input("Nhập mã cầu thủ: ")
        ten_ct = input("Nhập tên cầu thủ: ")
        tuoi = int(input("Nhập tuổi: "))
        vi_tri = input("Nhập vị trí (thủ môn/hậu vệ/tiền vệ/tiền đạo): ")
        so_huy_chuong = int(input("Nhập số huy chương: "))
        
        # Tính thưởng
        if so_huy_chuong > 10:
            thuong = so_huy_chuong * 500000
        elif 5 <= so_huy_chuong <= 10:
            thuong = so_huy_chuong * 300000
        else:
            thuong = so_huy_chuong * 200000

        cau_thu = {
            "ma_ct": ma_ct,
            "ten_ct": ten_ct,
            "tuoi": tuoi,
            "vi_tri": vi_tri,
            "so_huy_chuong": so_huy_chuong,
            "thuong": thuong
        }
        ds_cau_thu.append(cau_thu)
        print("Đã thêm cầu thủ thành công!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho tuổi hoặc số huy chương!")

# Hàm hiển thị danh sách cầu thủ
def xem_danh_sach_cau_thu():
    if not ds_cau_thu:
        print("Danh sách cầu thủ trống!")
        return
    print(f"{'Mã CT':<10}{'Tên cầu thủ':<20}{'Tuổi':<10}{'Vị trí':<15}{'Số HC':<10}{'Thưởng':<15}")
    print("-" * 80)
    for ct in ds_cau_thu:
        print(f"{ct['ma_ct']:<10}{ct['ten_ct']:<20}{ct['tuoi']:<10}{ct['vi_tri']:<15}{ct['so_huy_chuong']:<10}{ct['thuong']:<15}")

# Hàm tìm kiếm và xóa cầu thủ theo mã
def xoa_cau_thu():
    try:
        ma_ct = input("Nhập mã cầu thủ cần xóa: ")
        for ct in ds_cau_thu:
            if ct["ma_ct"] == ma_ct:
                ds_cau_thu.remove(ct)
                print("Đã xóa cầu thủ thành công!")
                return
        print("Không tìm thấy cầu thủ!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Hàm tìm kiếm và chỉnh sửa thông tin cầu thủ
def sua_cau_thu():
    try:
        ma_ct = input("Nhập mã cầu thủ cần sửa: ")
        for ct in ds_cau_thu:
            if ct["ma_ct"] == ma_ct:
                print("Nhập thông tin mới (bỏ trống để giữ nguyên):")
                ten_ct = input("Tên cầu thủ: ")
                if ten_ct:
                    ct["ten_ct"] = ten_ct
                tuoi = input("Tuổi: ")
                if tuoi:
                    ct["tuoi"] = int(tuoi)
                vi_tri = input("Vị trí: ")
                if vi_tri:
                    ct["vi_tri"] = vi_tri
                so_huy_chuong = input("Số huy chương: ")
                if so_huy_chuong:
                    ct["so_huy_chuong"] = int(so_huy_chuong)
                    # Cập nhật thưởng
                    if ct["so_huy_chuong"] > 10:
                        ct["thuong"] = ct["so_huy_chuong"] * 500000
                    elif 5 <= ct["so_huy_chuong"] <= 10:
                        ct["thuong"] = ct["so_huy_chuong"] * 300000
                    else:
                        ct["thuong"] = ct["so_huy_chuong"] * 200000
                print("Đã cập nhật thông tin cầu thủ!")
                return
        print("Không tìm thấy cầu thủ!")
    except ValueError:
        print("Lỗi: Vui lòng nhập đúng định dạng cho tuổi hoặc số huy chương!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Hàm sắp xếp danh sách theo số huy chương
def sap_xep_so_huy_chuong():
    try:
        ds_cau_thu.sort(key=lambda x: x["so_huy_chuong"])
        print("Danh sách đã được sắp xếp theo số huy chương!")
    except Exception as e:
        print(f"Lỗi: {e}")

# Menu chương trình
def menu():
    while True:
        try:
            print("\nQuản lý đội bóng")
            print("1. Xem danh sách cầu thủ")
            print("2. Nhập thông tin cầu thủ")
            print("3. Tìm kiếm và xóa cầu thủ theo mã")
            print("4. Tìm kiếm và chỉnh sửa thông tin cầu thủ theo mã")
            print("5. Xem danh sách cầu thủ sắp xếp theo số huy chương")
            print("6. Thoát chương trình")
            chon = input("Chọn chức năng (1-6): ")
            if chon == "1":
                xem_danh_sach_cau_thu()
            elif chon == "2":
                nhap_cau_thu()
            elif chon == "3":
                xoa_cau_thu()
            elif chon == "4":
                sua_cau_thu()
            elif chon == "5":
                sap_xep_so_huy_chuong()
            elif chon == "6":
                print("Thoát chương trình!")
                break
            else:
                print("Chức năng không hợp lệ, vui lòng chọn lại!")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")

# Chạy chương trình
menu()
