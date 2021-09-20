while True:
    x = input("Input three-digit number or -1 for exit: ")
    if x == "-1":
        break
    if len(x) == 3 and x.isdigit():
        multiplication = int(x[0]) * int(x[1]) * int(x[2])
        amount = int(x[0]) + int(x[1]) + int(x[2])
        if amount == 0:
            print("Division by zero!")
            continue
        quotient = multiplication / amount
        print(f"Произведение: {multiplication}\nСумма: {amount}\nЧастное: {quotient:.2f}")
    else:
        print("Input number is not correct, please try again")

# Второе решение

# while True:
#     x = input("Input three-digit number or -1 for exit: ")
#     if x == "-1":
#         break
#     if len(x) == 3 and x.isdigit():
#         x = int(x)
#         x3 = (x // 100)
#         x2 = (x - x3 * 100) // 10
#         x1 = (x % 10)
#         multiplication = x3 * x2 * x1
#         amount = x3 + x2 + x1
#         if amount == 0:
#             print("Division by zero!")
#             continue
#         quotient = multiplication / amount
#         print(f"Произведение: {multiplication}\nСумма: {amount}\nЧастное: {quotient:.2f}")

print("Goodbye! Thank you for using my programm!")