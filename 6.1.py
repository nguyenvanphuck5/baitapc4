#Giải hệ phương trình bậc nhất:
# Nhập hệ số a và b từ người dùng
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))

if a == 0:
    print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình là: x = {x}")