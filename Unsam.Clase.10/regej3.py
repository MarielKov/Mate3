import re

texto ="""Maria tiene 5 años, y su hermana Valeria tiene 2.
Rita y Pedro, sus primos, tienen 3."""

patron = "[A-Z]\w+"

def buscar(patron, n):


 print(re.findall(patron, n))

buscar(patron, texto)

