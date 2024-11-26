import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv
import pandas as pd
from pandas import DataFrame
import os

load_dotenv()

DBHOST = os.getenv("DBHOST")
DBNAME = os.getenv("DBNAME")
DBUSER = os.getenv("DBUSER")
PASSWORD = os.getenv("PASSWORD")

def connect_to_database():
    return psycopg2.connect(host= DBHOST,
                            database= DBNAME,
                            user= DBUSER,
                            password= PASSWORD)
    
def save_product(conn, product):
    cursor = conn.cursor()
    cursor.execute(''' 
        INSERT INTO compras (produto, preco, local_de_compra, promocao, data_de_compra) VALUES(%s, %s, %s, %s, %s)
    ''', (product['Produto'], product['Preço'], product['Mercado'], product['Promoção'], product['Data']))

    conn.commit()
    cursor.close()

