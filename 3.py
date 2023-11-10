# Nhập hai số tự nhiên m và n từ bàn phím
m = int(input("Nhập số tự nhiên m: "))
n = int(input("Nhập số tự nhiên n (n > m): "))

# Kiểm tra nếu m > n, yêu cầu người dùng nhập lại
while m >= n:
    print("Vui lòng đảm bảo m < n.")
    m = int(input("Nhập số tự nhiên m: "))
    n = int(input("Nhập số tự nhiên n (n > m): "))

# In ra các số chia hết cho m trong khoảng từ 1 đến n
print(f"Các số chia hết cho {m} trong khoảng từ 1 đến {n} là:")
for x in range(1, n + 1):
    if x % m == 0:
        print(x)