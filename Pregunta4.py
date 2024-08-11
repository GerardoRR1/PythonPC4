#/workspaces/ProgramacionPython202407/Modulo4/src/temperaturas.txt

from pprint import pprint
with open('/workspaces/PythonPC4/temperaturas.txt', 'r') as f:
    lista = f.readlines()

temperaturas = []
fechas = []
for linea in lista:
    fecha,temperatura = linea.strip().split(',')
    
    fechas.append(fecha)
    temperaturas.append(float(temperatura))

temp_prom = sum(temperaturas)/len(temperaturas)
temp_max = max(temperaturas)
temp_min = min(temperaturas)

with open('resumen_temperaturas', 'w') as f: 
    f.write(f"Temperatura promedio: {temp_prom:.2f}°C\n")
    f.write(f"Temperatura promedio: {temp_max:.2f}°C\n")
    f.write(f"Temperatura promedio: {temp_min:.2f}°C\n")



