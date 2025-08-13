

from lib.my_unnecessary_lib import count_letters

if __name__ == '__main__':
    text = "lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    for char, quantity in count_letters(text).items():
        print(f"{char}: {quantity}",)

