
from collections import deque, UserDict, defaultdict, namedtuple

list_of_symbols = [1, "20", 3, "41", 5, "67", 7, 8, "90", 10]
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'USA'),
    (55, 'Brazil'),
    (61, 'Australia'),
    (54, 'Argentina'),
    (81, 'Japan'),
    (92, 'Pakistan'),
]
dic_1 = { "a": 1, "b": 2, "c": 3 }
dic_2 = { "a": 10, "d": 2, "e": 3 }
dic_3 = dic_1 | dic_2

user_info = ("John", "Doe", "john.doe@example.com", "1234567890")
User = namedtuple("User_Info", "first_name, last_name, email, phone_number")
user_john = User(*user_info)


country_codes = {country: code for code, country in dial_codes}
rev_country_codes = {code: country.upper() for country, code in country_codes.items() if code == 55}
sorted_list_of_symbols = sorted(list_of_symbols, key = str)

loop_list = deque([i for i in range(10)],10)

list_of_books = [
    {"type": "book", "api": 2, "authors": "Martelli Ravenscroft Holden".split()},
    {"type": "book", "api": 2, "authors": "Parker Bell".split()},
    {"type": "book", "api": 1, "author": "Lewis Carroll"},
    {"type": "book", "api": 1, "author": "Stephen King"},
    {"type": "book", "api": 1, "author": "Alexander Pushkin"},
]
def get_creators(record: dict) -> list:
    match record:
        case {"type": "book", "api": 2, "authors": [*names] }:
            return names
        case {"type": "book", "api": 1, "author": name }:
            return [name]
        case _:
            raise ValueError(f"Invalid record {record}")

class StringKeysDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(f"Key {key} not found")
        return self[str(key)]
    def __contains__(self, key):
        return str(key) in self.data
    def __setitem__(self, key, value):
        self.data[str(key)] = value



if __name__ == '__main__':
    print(user_john.first_name)

    test = StringKeysDict()
    test["a"] = 10
    test[2] = 22
    print(test["a"])

    # temp = []
    # for record in list_of_books:
    #     temp.extend(get_creators(record))
    # print(temp)
    # print([author for record in list_of_books for author in get_creators(record)])

    # print(country_codes)
    # print(rev_country_codes)
    # print(sorted_list_of_symbols)
    # print(dic_3)

