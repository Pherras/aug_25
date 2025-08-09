import sqlite3

create_table_query = '''
CREATE TABLE IF NOT EXISTS users(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NAME TEXT NOT NULL,
LAST_NAME TEXT,
AGE INTEGER
);
'''

connection = sqlite3.connect('users.db')

def create_table():
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_query)
        connection.commit()
        print(' база создана')
    except sqlite3.Error as error:
        print("база НЕ создана", error)

def insert_user(name, last_name, age):
    if name and last_name and age:
        try:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO users (NAME, LAST_NAME, AGE) VALUES (?, ?, ?)', (name, last_name, age))
            connection.commit()
            print(f'пользователь {name} добавлен')
        except sqlite3.Error as error:
            print("ошибка при добавлении пользователя", error)

def select_users():
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM USERS")
        result =  cursor.fetchall()
        connection.commit()
        return result
    except sqlite3.Error as error:
        print("ошибка при выборе пользователей", error)



if __name__ == '__main__':
    create_table()
    insert_user('Иван', 'Иванов', 25)
    users = select_users()
    for user in users:
        print(user)