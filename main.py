
def input_number():
    temp = input("Введите число: ")
    try:
        return int(temp)
    except ValueError:
        print(f"Некорректный ввод, {temp} не является числом")
        return input_number()

def is_palindrome(value: str, without_spaces = False):
    temp = value.lower()
    def compare(text: str):
        if text == text[::-1]:
            return f" {value} - Палиндром"
        else:
            return f" {value} - Не палиндром"
    if without_spaces:
       return compare(temp.replace(" ", ""))
    return compare(temp)

colors = ["красный", "зеленый", "желтый", "синий", "фиолетовый", "оранжевый", "белый", "черный", "розовый", "коричневый",]
sizes = ["S", "M", "L", "XL",]

if __name__ == '__main__':
    # print(is_palindrome("а роза упала на лапу Азора", without_spaces=True))
    print(input_number())
    # tshirt = [(color, size) for size in sizes for color in colors]
    # for t in tshirt:
    #     print(t)


