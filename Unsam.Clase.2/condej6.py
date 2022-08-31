dia = input("ingrese un dia de la semana:  ")

if dia == "lunes" :

    print("El dia es lunes")

    exam = input("Se tomaron examenes?:  ")

    if exam == "si":

        aprov = int(input("Ingrese cantidad de alumnos aprobados:  "))
        desaprov = int(input("Ingrese cantidad de alumnos desaprobados:  "))

        porc = aprov * 100 / (aprov + desaprov)
        resp = round(porc, 2)
        print(f"El porcentaje de aprobados es %{resp}")

    elif exam == "no": print("Hasta pronto :)")   

    else: print("ERROR") 


elif dia == "martes" :
    
    print("El dia es martes")

    exam = input("Se tomaron examenes?:  ")

    if exam == "si":

        aprov = int(input("Ingrese cantidad de alumnos aprobados:  "))
        desaprov = int(input("Ingrese cantidad de alumnos desaprobados:  "))

        porc = aprov * 100 / (aprov + desaprov)
        resp = round(porc, 2)
        print(f"El porcentaje de aprobados es %{resp}")

    elif exam == "no": print("Hasta pronto :)")   

    else: print("ERROR") 

elif dia == "miercoles" :
    
    print("El dia es miercoles")

    exam = input("Se tomaron examenes?:  ")

    if exam == "si":

        aprov = int(input("Ingrese cantidad de alumnos aprobados:  "))
        desaprov = int(input("Ingrese cantidad de alumnos desaprobados:  "))

        porc = aprov * 100 / (aprov + desaprov)
        resp = round(porc, 2)
        print(f"El porcentaje de aprobados es %{resp}")

    elif exam == "no": print("Hasta pronto :)")   

    else: print("ERROR") 

elif dia == "jueves" :
    
    print("El dia es jueves")

    total = int(input("Ingrese total alumnos:  "))
    asist = int(input("Ingrese alumnos presentes:  "))

    porc2 = (asist * 100) / total 

    if porc2 <= 50 : print("No asistió la mayoría")
    else:  print("Asistió la mayoría")

elif dia == "viernes" :
    
    print("El dia es viernes")

    print("Clase de consulta")

    total = int(input("Ingrese total alumnos:  "))
    precio = 100

    ingreso = total * precio

    print(f"Ingreso por clase consulta = ${ingreso}")

else: print("ERROR")