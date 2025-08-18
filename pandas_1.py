import sqlite3

import pandas as pd

film_dict = {
    "film_ID": [1, 2, 3],
    "year": [1990, 1991, 1992],
    "name": ["Имя Фильма Один", "Имя Фильма Два", "Имя Фильма Три"]
}


pd_data = pd.DataFrame(film_dict,)
connection = sqlite3.connect("films.db")



if __name__ == '__main__':
    # print(pd_data)
    pd_data.to_sql("films",connection, if_exists="replace")
    films_data = pd.read_sql("SELECT * FROM films", connection)
    print(films_data)