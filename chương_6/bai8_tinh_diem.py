# Nhập điểm từ người dùng
try:
    diem_chuyen_can = float(input("Nhập điểm chuyên cần: "))
    diem_giua_ky = float(input("Nhập điểm giữa kỳ: "))
    diem_cuoi_ky = float(input("Nhập điểm cuối kỳ: "))
    
    # Tính điểm trung bình
    diem_trung_binh = (diem_chuyen_can + diem_giua_ky + diem_cuoi_ky) / 3
    
    # Xếp loại theo điểm trung bình
    if diem_trung_binh >= 9:
       loai = 'A'
    else:
        if diem_trung_binh >= 7:
            loai = 'B'
        else:
            if diem_trung_binh >= 5:
                loai = 'C'
            else:
                loai = 'D'
    
    # In kết quả
    print(f"Điểm trung bình: {diem_trung_binh:.2f}, Xếp loại: {loai}")
except ValueError:
    print("Vui lòng nhập đúng định dạng số cho điểm.")
