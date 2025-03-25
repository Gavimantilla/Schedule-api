import os
import psycopg

DB_CONFIG = {
    'dbname': os.environ.get('DB_NAME', 'schedules'),
    'user': os.environ.get('DB_USER', 'postgres'),
    'password': os.environ.get('DB_PASSWORD', 'Gavi_2003@'),
    'host': os.environ.get('DB_HOST', 'db'),
    'port': int(os.environ.get('DB_PORT', 5432))
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)
