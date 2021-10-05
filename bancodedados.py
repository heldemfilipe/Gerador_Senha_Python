import sqlite3

MASTER_PASSWORD = "123456"

conn = sqlite3.connect('senhas.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')


def mostrar_senha(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não cadastrado (Visualizar senha do usuario para ver os usuarios).")
    else:
        for user in cursor.fetchall():
            print(user)


def inserir_senha(site, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{site}', '{username}', '{password}')
    ''')
    conn.commit()


def mostrar_sites():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


def close():
    conn.close()
