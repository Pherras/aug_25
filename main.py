from random import shuffle

from lib.my_unnecessary_lib import count_letters
from micro_apps.random_card.settings import app_title

if __name__ == '__main__':
    text = "lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    for char, quantity in count_letters(text).items():
        print(f"{char}: {quantity}",)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

