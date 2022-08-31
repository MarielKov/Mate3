lista = [1,1,3,2,3]
conj = {1}
x = {1, 2, 1}
y = {2, 3, 2, 4}

conj.update(lista)

print(f"Lista a conjunto: {conj}")

z = x.difference(y)

print(f"Diferencia: {z}")

v = x.union(y)

print(f"Union: {v}")

n = x.intersection(y)

print(f"Interseccion: {n}")

m = x.update(y)

print (f"Iguales: {x}")


