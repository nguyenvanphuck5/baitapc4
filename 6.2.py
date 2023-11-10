# Tính số ngày của một tháng trong một năm nào đó:
# Nhập tháng và năm từ người dùng
month = int(input("Nhập tháng (1-12): "))
year = int(input("Nhập năm: "))

leap_year = (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))

if month < 1 or month > 12:
    print("Tháng không hợp lệ.")
else:
    if month == 2:
        if leap_year:
            print("Tháng 2 của năm nhuận có 29 ngày.")
        else:
            print("Tháng 2 có 28 ngày.")
    elif month in [1, 3, 5, 7, 8, 10, 12]:
        print(f"Tháng {month} có 31 ngày.")
    else:
        print(f"Tháng {month} có 30 ngày.")