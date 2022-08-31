#!/usr/bin/env python
# coding: utf-8

# # Introduccion a NumPy - Ejercicios
# Empezamos a trabajar como data Analyst en una empresa de la ciudad, y el gerente requiere de nuestra ayuda...

# #### 1. Comienza importando NumPy como `np`

# In[ ]:





# La empresa recaba datos de usuarios de internet: 
# - 'duracion,paginas,acciones,valor,clase'. 
# 
# Por ejemplo, un usuario navega: |duracion|paginas|acciones|valor|clase|, o sea:
# 
# |2.34 minutos/segundos de navegación |8 páginas|4 acciones|1 valor|5 (clasificación de usuario)|
#     
# #### 2.Crea un array de NumPy que represente los datos anteriores. Cada elemento debe ser un numero (por ejemplo `2.34` para "2.34 minutos/segundos"). Guarda este array como `un_usuario`

# In[ ]:





# El asistente ha compilado los datos de un día en un archivo `csv` llamado `usuarios.csv`. Este archivo fue suministrado.
# 
# #### 3. Carga este archivo en una variable llamada `usuarios`

# In[ ]:





# #### 4. Emite 'usuarios'

# In[ ]:


usuarios


# Cada fila representa un usuario diferente. Cada columna representa una característica diferente.
# 
# La tercera columna representa el numero de 'acciones' que realiza cada usuario. 
# 
# #### 5. Selecciona todos los elementos de la tercera columna y guárdalos en una variable llamada 'acciones'

# In[ ]:





# #### 6. Cuáles usuarios realizaron 4 acciones? Usa una sentencia lógica para obtener 'True' o 'False' para cada valor de acciones

# In[ ]:





# El gerente necesita los datos de la tercera fila...
# 
# #### 7. Crea una variable para los datos de la tercera fila y emite los datos

# In[ ]:





# #### 8. Los datos del quinto usuario se guardaron mal, en realidad es el doble en todo. Guarda la operación en nueva variable en  'doble_usuario5'

# In[ ]:





# #### 9. El gerente necesita saber de cuántos usuarios se obtuvo información:

# In[ ]:





# #### 10. Cómo quedó muy contento con nuestro trabajo necesita saber:
# 
# 1. El máximo de tiempo que estuvo un usuario navegando.
# 2. El mínimo de tiempo que estuvo un usuario navegando.
# 3. La media de tiempo de navegación y de páginas navegadas.
# 4. El total de tiempo de navegación y de páginas navegadas.
# 5. La mediana de acciones registradas.
# 6. Calcula la moda de las acciones (puedes necesitar: from scipy import stats)

# In[ ]:




