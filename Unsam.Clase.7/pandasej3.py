"""3. Escribe una función que reciba los datos siguientes en un DataFrame, una lista de meses, 
y devuelva el balance (ventas - gastos) total en los meses indicados.
"""
import pandas as pd

datos = {'Mes':['Enero', 'Febrero', 'Marzo', 'Abril'], 
        'Ventas':[30500, 35600, 28300, 33900], 
        'Gastos':[22000, 23400, 18100, 20700]}


datos_ventas = datos['Ventas']
datos_gastos = datos['Gastos']   

print(datos_ventas)
print(datos_gastos)

datos_balance = []

for n in range(4):
    datos_balance.append(datos_ventas[n] - datos_gastos[n])
    
print(datos_balance)

datos.update({"Balance" : datos_balance})

df = pd.DataFrame(datos)
print(df)
