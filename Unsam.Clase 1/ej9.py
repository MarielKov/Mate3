gramosp = 112
gramosm = 75

payasos = int(input("Cantidad de payasos: "))
muniecas = int(input("Cantidad de muñecas: "))

pesop = payasos * gramosp
pesom = muniecas * gramosm

envio = (pesop + pesom) / 1000


print(f"El envio pesa: {envio} kg")