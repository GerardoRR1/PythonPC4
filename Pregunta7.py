import requests
import sqlite3
from pymongo import MongoClient
from datetime import datetime, timedelta

# Paso 1: Obtener los datos del API de SUNAT
base_url = "https://api.apis.net.pe/v1/tipo-cambio-sunat?fecha="
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
delta = timedelta(days=1)

# Lista para almacenar los datos de cada día
datos_sunat = []

while start_date <= end_date:
    fecha_str = start_date.strftime('%Y-%m-%d')
    response = requests.get(base_url + fecha_str)
    if response.status_code == 200:
        data = response.json()
        datos_sunat.append((fecha_str, data['compra'], data['venta']))
    start_date += delta

# Paso 2: Almacenar los datos en SQLite
conn = sqlite3.connect('base.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info
                  (fecha TEXT PRIMARY KEY, compra REAL, venta REAL)''')

# Insertar los datos en la tabla sunat_info
cursor.executemany('INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)', datos_sunat)
conn.commit()

# Paso 3: Almacenar los datos en MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sunat_db']
collection = db['sunat_info']

# Convertir los datos a formato de diccionario y almacenar en MongoDB
for dato in datos_sunat:
    document = {'fecha': dato[0], 'compra': dato[1], 'venta': dato[2]}
    collection.insert_one(document)

# Paso 4: Mostrar el contenido de la tabla sunat_info en SQLite
cursor.execute('SELECT * FROM sunat_info')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Cerrar la conexión con SQLite
conn.close()

# Cerrar la conexión con MongoDB
client.close()
