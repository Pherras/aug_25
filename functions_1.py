from functools import partial

import unicodedata

from lib.my_unnecessary_lib import clock


@clock
def factorial(n):
    return 1 if n < 2 else n * factorial(n - 1)


nfc = partial(unicodedata.normalize, 'NFC')
string_a = "café"
string_b = "cafe\u0301"


def make_average():
    count = 0
    sum = 0

    def average(value):
        nonlocal count, sum
        if value is not None:
            count += 1
            sum += value
        return round(sum / count, 2)

    return average


avg_int = make_average()
avg_float = make_average()

if __name__ == '__main__':
    print(factorial(5))

    # print(avg_int(10))
    # print(avg_int(37))
    # print("-------")
    # print(avg_float(10.4))
    # print(avg_float(37.0))

    # print(string_a == string_b)
    # print(nfc(string_a) == nfc(string_b))

    # print(list(map(factorial, range(5))))
    # print([factorial(n) for n in range(5)])
    #
    # print(list(map(factorial, filter(lambda x: x % 2, range(5)))))
    # print([factorial(n) for n in range(5) if n % 2])
