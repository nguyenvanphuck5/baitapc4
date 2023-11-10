# Nhập một số từ bàn phím
num = float(input("Nhập một số: "))

# Kiểm tra xem số nhập vào có là số dương hay không
if num > 0:
    # Tính bình phương của số và in ra kết quả
    square = num * num
    print(f"Bình phương của {num} là {square}")
else:
    print("Số bạn vừa nhập không phải là số dương.")