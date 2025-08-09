
def input_number():
    temp = input("Введите число: ")
    try:
        return int(temp)
    except ValueError:
        print(f"Некорректный ввод, {temp} не является числом")
        return input_number()


if __name__ == '__main__':
    print("1")


