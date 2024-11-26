import sqlite3


conn = sqlite3.connect("users_dz.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
""")
conn.commit()


def add_users(users):
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
    conn.commit()


def get_user_by_index(index):
    cursor.execute("SELECT name, age FROM users WHERE id = ?", (index,))
    result = cursor.fetchone()
    if result:
        return f"{result[0]} {result[1]}"
    else:
        return "Пользователь с таким индексом не найден."


cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    users_data = [("Олег", 35), ("Егор", 33), ("Игорь", 32)]
    add_users(users_data)


index_to_find = 2
result = get_user_by_index(index_to_find)
print(result)


conn.close()
