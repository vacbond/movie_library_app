from dotenv import load_dotenv
import os
load_dotenv()

import psycopg2  # pyright: ignore[reportMissingModuleSource]


def get_connection():
    conn = psycopg2.connect(
    host=os.getenv("DB_HOST"),
    database=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    port=os.getenv("DB_PORT")
)
    cur = conn.cursor()
    return cur, conn

print("Connection is OK")
