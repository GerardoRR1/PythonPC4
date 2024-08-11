import csv
import sqlite3

# Crear las tablas en la base de datos SQLite
def crear_tablas():
    conn = sqlite3.connect('tipo_cambio.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ventas (
        fecha DATE,
        producto TEXT,
        cantidad INTEGER,
        precio_unitario REAL
    );
    ''')
    
    # Eliminar la tabla tipo_cambio ya que no la necesitamos para este caso
    cursor.execute('DROP TABLE IF EXISTS tipo_cambio')
    
    conn.commit()
    conn.close()

# Leer el archivo ventas.csv e insertar los datos en la base de datos
def insertar_datos_ventas():
    conn = sqlite3.connect('tipo_cambio.db')
    cursor = conn.cursor()
    
    with open('ventas.csv', mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera si la hay
        for row in reader:
            fecha, producto, cantidad, precio_unitario = row
            cursor.execute('''
            INSERT INTO ventas (fecha, producto, cantidad, precio_unitario)
            VALUES (?, ?, ?, ?);
            ''', (fecha, producto, int(cantidad), float(precio_unitario)))
    
    conn.commit()
    conn.close()

# Procesar los datos para calcular el total de ventas por producto
def calcular_totales():
    tipo_cambio_fijo = 3.72  # Tipo de cambio fijo
    
    conn = sqlite3.connect('tipo_cambio.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT fecha, producto, cantidad, precio_unitario
    FROM ventas
    ''')
    
    totales_por_producto = {}
    for fecha, producto, cantidad, precio_unitario in cursor.fetchall():
        total_dolares = cantidad * precio_unitario
        total_soles = total_dolares * tipo_cambio_fijo
        
        if producto not in totales_por_producto:
            totales_por_producto[producto] = {'total_dolares': 0, 'total_soles': 0}
        
        totales_por_producto[producto]['total_dolares'] += total_dolares
        totales_por_producto[producto]['total_soles'] += total_soles
    
    conn.close()
    return totales_por_producto

# Escribir los resultados en total_ventas.txt
def escribir_resultados(totales_por_producto):
    try:
        with open('total_ventas.txt', mode='w') as file:
            file.write('Producto\tTotal Dólares\tTotal Soles\n')
            for producto, totales in totales_por_producto.items():
                file.write(f"{producto}\t{totales['total_dolares']:.2f}\t{totales['total_soles']:.2f}\n")
        print("Archivo total_ventas.txt creado con éxito.")
    except Exception as e:
        print(f"Error al crear el archivo: {e}")

# Ejecutar los pasos
crear_tablas()
insertar_datos_ventas()
totales_por_producto = calcular_totales()
escribir_resultados(totales_por_producto)
