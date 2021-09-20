while True:
    x = input("Input three-digit number or -1 for exit: ")
    if x == "-1":
        break
    if len(x) == 3 and x.isdigit():
        a = x[0]
        b = x[1]
        c = x[2]
        a, c = c, a
        number = a + b + c
        print("Число после замены:", number)
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
#         x3, x1 = x1, x3
#         number = str(x3) + str(x2) + str(x1)
#         print("Число после замены:", number)
#     else:
#         print("Input number is not correct, please try again")
        
print("Goodbye! Thank you for using my programm!")


