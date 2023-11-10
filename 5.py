# Hàm tính UCLN (Ước số chung lớn nhất)
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

# Hàm tính BCNN (Bội chung nhỏ nhất)
def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

# Nhập hai số nguyên từ bàn phím
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

# Tính và in ra BCNN của hai số
bcnn_result = bcnn(a, b)
print(f"BCNN của {a} và {b} là: {bcnn_result}")