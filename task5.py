while True:
    x = input("Введите стоимость покупки или -1 для выхода:")
    if x == "-1":
        break
    if x.isdigit():
        x = int(x)
        if x > 1000:
            print(f"Скидка составила 5%. К оплате: {x * 0.95:.2f} р.")
            continue
        if x > 500:
            print(f"Скидка составила 3%. К оплате: {x * 0.97:.2f} р.")
            continue
        print(f"Скидки нет. К оплате: {x:.2f} р.")
    else:
        print("Input number is not correct, please try again")     
print("Goodbye! Thank you for using my programm!")

