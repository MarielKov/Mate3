kilos = float(input("Ingrese kilos: "))
altura = float(input("Ingrese altura: "))

imc = kilos / altura

masa = round(imc , 2)

print(f"Usted tiene {masa} de IMC")

