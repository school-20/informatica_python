#work only on python 3.9.7 

while True:
    number = input("Input two-digit number or -1 for exit: ")
    if number == "-1":
        break
    if len(number) == 2 and number[0].isdigit() and number[1].isdigit():
        result = abs(int(number[0]) - int(number[1]))
        print(result)
    else:
        print("Input number is not correct, please try again")

# Решение второе, используя арифметические операции. 

# while True:
#     x = input("введите двузначное число или -1 для выхода: ")
#     if x == "-1":
#         break
#     if len(x) == 2 and x[0].isdigit() and x[1].isdigit():
#         print(abs(int(x) // 10 - int(x) % 10))
#     else:
#         print("Input number is not correct, please try again")
print("Goodbye! Thank you for using my programm.")