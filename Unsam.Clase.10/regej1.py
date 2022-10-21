import re

a = "abc bca xxx x (xxx) (z+ 1a2b3 b34c 123* pan"
b = "pa Pan PanN  PpAa  Pan* Xan\* |A| \.\ .\.* .\\an*"
c = "(ab) b7 b52s [^ab] (x b2s (pe bas? (( xxx"

patronA = ["[^abc]?", "([^a][^b][^c])*","[^(abc)]+","\([^abc]\)*"]

patronB = ["(Pp)(Aa)(Nn)*", "[P\p][A\a][N\n]","\.\.*","[^Aa](an)\*"]

patronC = ["\([^ab)]", "b[3-37]s","(([^a][^b])*)+","b[^0-59]s?"]


def buscar(patron, n):
 for i in patron:

     print(re.findall(i, n))
     print ("\n")


buscar(patronA, a) 
print("------------------")   
buscar(patronB, b)
print("------------------")  
buscar(patronC, c)




