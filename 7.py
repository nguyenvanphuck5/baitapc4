def tinh_tong_chu_so(N):
    total = 0  # Khởi tạo biến tổng
    while N > 0:
        digit = N % 10  # Lấy chữ số cuối cùng của N
        total += digit  # Cộng chữ số này vào tổng
        N //= 10 # Loại bỏ chữ số cuối cùng
    return total

# Nhập số nguyên N từ bàn phím
N = int(input("Nhập số nguyên N: "))

# Gọi hàm và in ra kết quả
tong_chu_so = tinh_tong_chu_so(N)
print(f"Tổng các chữ số của {N} là: {tong_chu_so}")