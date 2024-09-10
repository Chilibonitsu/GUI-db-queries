import psycopg2
import json

def get_connection():
    # Чтение конфигурации из JSON файла
    with open('db_config.json', 'r') as config_file:
        config = json.load(config_file)

    # Подключение к базе данных с использованием конфигурации
    conn = psycopg2.connect(
        dbname=config['dbname'],
        user=config['user'],
        password=config['password'],
        host=config['host'],
        port=config['port']
    )

    conn.set_client_encoding('UTF8')
    
    # Возвращаем соединение и курсор
    return conn, conn.cursor()
