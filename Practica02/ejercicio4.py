#Ejercicio 4: Declarar variables de diferentes tipos de datos basicos y mostrar su informacion

#Declaracion de variables
edad = 20             #int
promedio = 8.5        #float
nombre = "Juan"       #str
activo = True         #bool

#Mostrar valor y tipo de cada variable usando type()
print(f"Variable: edad = {edad}, tipo: {type(edad)}")
print(f"Variable: promedio = {promedio}, tipo: {type(promedio)}")
print(f"Variable: nombre = {nombre}, tipo: {type(nombre)}")
print(f"Variable: activo = {activo}, tipo: {type(activo)}")

#Operaciones basicas entre variables compatibles 
print("\n--- Operaciones Basicas ---")
print(f"Suma de edad + promedio = {edad + promedio}")  #int + float
print(f"Multiplicacion de edad * 2 = {edad * 2}")   #int * int
print(f"Concatenacion de nombre + ' Perez' = {nombre + ' Perez'}")  #str + str
print(f"Negacion de activo = {not activo}")  #Operacion logica con bool

