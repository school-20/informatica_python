#work only on python 3.9.7 

while True:
    number = input("Input two-digit number or -1 for exit: ")
    if number == "-1":
        print("Goodbye! Thank you for using my programm.")
        break
    if len(number) == 2 and number[0].isdigit() and number[1].isdigit():
        print(int(number[0]) - int(number[1]))
    else:
        print("Input number is not correct, please try again")
