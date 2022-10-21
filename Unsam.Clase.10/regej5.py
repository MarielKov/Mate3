
import re

txt = open("pedidos.txt","w").read()


patron = r''


def buscar(patron, n):


 print(re.findall(patron, n))

buscar(patron, txt)
 
print(txt)