while True:
    x = input("Введите длину основания треугольника или -1 для выхода: ")
    if x == "-1":
        break
    h = input("Введите высоту треугольника: ")
    if not(x.isdigit() and h.isdigit()): 
        print("Input number is not correct, please try again")
        continue
    S = float(x) * float(h)/2
    print(f"Площадь треугольника: {S:.4f}")
    if S % 2 == 0:
        print("площадь кратна двум")
    else:
        print("Площадь не кратна двум")
print("Goodbye! Thank you for using my programm!")

