import os
import psycopg

DB_CONFIG = {
    'dbname': os.environ.get('DB_NAME', ''),
    'user': os.environ.get('DB_USER', ''),
    'password': os.environ.get('DB_PASSWORD', ''),
    'host': os.environ.get('DB_HOST', ''),
    'port': int(os.environ.get('DB_PORT', 5432))
}

def get_connection():
    return psycopg.connect(**DB_CONFIG)
