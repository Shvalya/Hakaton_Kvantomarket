import sqlite3

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()


#ДЕЙСТВИЯ С БД



# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()