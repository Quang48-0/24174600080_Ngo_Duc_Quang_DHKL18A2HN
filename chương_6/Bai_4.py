#Bai 4
cong_suat = float(input("Nhập công suất bóng đèn (W): "))
thoi_gian = float(input("Nhập thời gian sử dụng (giờ): "))

#Dieu kien
if cong_suat > 0 and thoi_gian > 0:
    dien_ap = 220  # Điện áp
    gia_dien = 7000  # đồng/kWh
    nang_luong_tieu_thu = cong_suat / 1000 * thoi_gian
    tien_dien = nang_luong_tieu_thu * gia_dien
    print(f"Số tiền điện phải trả: {tien_dien:.2f} đồng")
else:
    print("Công suất và thời gian phải lớn hơn 0.")