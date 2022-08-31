dinero = float(input("Cantidad de dinero a depositar: "))

primeranio = dinero * (1 + 0.04)
primer = round(primeranio , 2)
segundoanio = dinero * (1 + 0.08) 
segundo = round(segundoanio , 2)
terceranio = dinero * (1 + 0.12)
tercer = round(terceranio , 2)

print(f"ingresos del primer año: {primer} $")
print(f"ingresos del segundo año: {segundo} $")
print(f"ingresos del tercer año: {tercer} $")