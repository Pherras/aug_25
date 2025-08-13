import collections


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

#норм вариант - collections.Counter(text)
def count_letters(text, only_alpha=True) -> dict:
    def_dict = collections.defaultdict(int)
    if only_alpha:
        for i in text:
            if i.isalpha():
                def_dict[i] += 1
    else:
        for i in text:
            def_dict[i] += 1
    return def_dict