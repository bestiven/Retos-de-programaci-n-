#Ejercicio 4
# Escribir un programa que muestre por pantalla el resultado de la siguiente operación aritmética 
# resultado = (((3+2)/(2*5))**2)
# print("El resutado de la operacion aritmetica es :", resultado)

#Ejercicio 5
#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
# Después debe mostrar por pantalla la paga que le corresponde.
# horasTrabajo = int(input("Numero de horas trabajadas : "))
# costo = float(input("Ingresa el costo por hora : "))
# pago = horasTrabajo*costo
# print("El costo de las horas trabajadas son : ", pago)

#Ejercicio 6
# Escribir un programa que lea un entero positivo,n ,introducido por el usuario 
# y después muestre en pantalla la suma de todos los enteros desde 1 hasta n
#La suma de los primeros enteros positivos puede ser calculada de la siguiente forma:
# n = int(input("ingrese un numero entero positivo : "))
# suma = ((n*(n+1))/2)
# print("el resultado de la suma de 1 hasta ",n, "es : " ,suma )

#Ejercicio 7
#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
#calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase
#  Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
#  redondeado con dos decimales.
# peso = float(input("ingrese su peso en kg : "))
# estatura = float(input("ingrese su estatura en m : "))
# imc = (peso/estatura**2)
# print(f'Tu indice de masa corporal es {round(imc, 2)}')

#Ejercicio 9
#Escribir un programa que pregunte al usuario una cantidad a invertir,
#el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
# monto = float(input("cantidad a invertir : "))
# interes = float(input("interes anual : "))
# n_años = int(input("numero de años : "))
# capital = (monto * ((1)+(interes/100)*(n_años)))
# print(capital)


#Ejercicio 10 
# muñecas = int(input("cantidad de muñecas vendidas : "))
# payasos = int(input("cantidad de payasos vendidos : "))
# peso_total = (muñecas * 75) +(payasos * 112)
# print(f'pesos total del paquete enviado {peso_total} g')



#Ejercicio 12
#Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience 
# leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual
#  de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total.

# n = int(5)
# precio = float(3.49)
# descuento = ((precio/100)*60)
# costoFinal = descuento*n
# print("Barras de pan vendidas : ", n)
# print("precio habitual de una barra de pan : ", precio ,"Euros" )
# print( "descuento por unidad del pan : " , descuento,"Euros")
# print(f"coste final total de {n} panes {round(costoFinal, 2)}" )

#----------------------------------------------------------------------------------------------------------------

