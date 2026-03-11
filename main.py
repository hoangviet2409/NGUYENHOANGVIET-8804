def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = int(input("Nhap so a: "))
b = int(input("Nhap so b: "))

print("Uoc chung lon nhat la:", ucln(a, b))