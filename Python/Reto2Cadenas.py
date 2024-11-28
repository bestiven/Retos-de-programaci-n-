#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla
#en líneas distintas el nombre del usuario tantas veces como el número introducido.
# nombre =input("ingrese su nombre :  ")
# numero = int(input("ingrese un numero : "))
# puede ser de esta forma o de la otra forma 
# conta = 1 
# while conta <= numero:
#     print(nombre)
#     conta+=1
#-------------------------------------------
# for i in range(0,numero): 
#     print(nombre)

# nombre = input("¿Cómo te llamas? ")
# n = input("Introduce un número entero: ")
# print((nombre + "\n") * int(n))
     
# nombre =input("ingrese su nombre :  ")
# numero = int(input("ingrese un numero : "))
# print((nombre + "\n")*numero)


#Ejercicio 2
# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla 
# el nombre completo del usuario tres veces, una con todas las letras minúsculas, 
# otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
# El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
# nombre = input("ingresa el nombre completo : ")
# print(nombre.lower()+"\n"+nombre.upper()+"\n"+ nombre.title()) #lower letras minusculas


#Ejercicio 3
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario
#lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario
#en mayúsculas y <n> es el número de letras que tienen el nombre.
# nombre = input("Ingresa tu nombre : ")
# print(f"{nombre.upper()} tiene {len(nombre)} letras ")


#Ejercicio 4
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension 
#donde el prefijo es el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56).
#Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla
#el número de teléfono sin el prefijo y la extensión.
# telefono = input("ingrese el numero de telefono en el siguiente formato \n prefijo-número-extension \n ")
# numero = telefono.split('-') # me separa en un arreglo segun el caracter especificado (-) solo en el caso de String
# numeroFinal = numero [1]
# print(f"el numero de telefono es {numeroFinal}")


#Ejercicio 5
#Escribir un programa que pida al usuario que introduzca una frase en la consola 
#y muestre por pantalla la frase invertida.
# frase = input("ingrese la frase a invertir : ")
# inversion = frase[::-1]
# print(inversion)
# print(f"frase invertida : {inversion}")


#Ejercicio 6
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal,
#y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
# frase = input("ingrese una frase")
# vocal = input("ingrese una vocal")
# print (f"{frase} con vocal {vocal.upper()}")


#Ejercicio 7
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla 
# otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
# correo = input("ingrese su correo electronico : ")
# nuevo = correo.split('@')
# correoNuevo = nuevo [0]
# print(f"{correoNuevo}@ceu.es")


#Ejercicio 8
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre
#por pantalla el número de euros y el número de céntimos del precio introducido. //pendiente por revisión 
# precio = (input("precio del producto  con solo dos decimales : "))
# resultado = precio.split('.')
# euros = resultado [0]
# centimos  = resultado[1]
# print(f'{euros} euros con {centimos} centimos ')


#Ejercicio 9
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
#el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes 
#se introduzcan con un solo carácter.




#Ejercicio 10
#Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla
# una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, 
# el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.


# producto = input("Ingrese el nombre de el producto : ")
# precio = float(input("Precio : "))
# nUnidades = input("Numero de unidades del producto : ")

# print (f'nombre : {producto} \n precio unitario : $ {round(precio,2)} \n ')
#pendiente.......................................


#has un programa que ingrese un numero y ese numero me valide si esta en un rango 
#especifico me capture el valor en ese rango  

altura = int(input('ingrese la altura en mm'))
tanque  = int(input('ingrese el tanque'))

if (tanque == 1):
    if (altura > 0 and altura <= 2165):
        print('busque en la tabla el valor y compare 1')
    else:
        print('el valor especificado no se encuentra en el rango de valores dentro de la tabla ')
        print("ingrese otro valor")
elif(tanque == 2):
    if (altura > 0 and altura <= 1505):
        print('busque en la tabla el valor y compare 2')
    else:
        print('el valor especificado no se encuentra en el rango de valores dentro de la tabla ')
        print("ingrese otro valor")
elif(tanque == 3):
    if (altura > 0 and altura <= 2130):
        print('busque en la tabla el valor y compare 3')
    else:
        print('el valor especificado no se encuentra en el rango de valores dentro de la tabla ')
        print("ingrese otro valor")
else:
    print('el valor ingresado no es valido ')





# def programa(altura):
#     match tanque:
#         case 1:
#             altura = int(input('ingrese la altura en mm'))
            
#         case 2:
#             altura = int(input('ingrese la altura en mm'))
#             if (altura > 0 and altura < 2200):
#                 print('busque en la tabla el valor y compare')

#             else:
#                 print('el valor especificado no se encuentra en el rango de valores dentro de la tabla ')
#                 print("ingrese otro valor")

#         case 3:
#             altura = int(input('ingrese la altura en mm'))
#             if (altura > 0 and altura < 2200):
#                 print('busque en la tabla el valor y compare')

#             else:
#                 print('el valor especificado no se encuentra en el rango de valores dentro de la tabla ')
#                 print("ingrese otro valor")

#         case _:
#             print("Ese tanque no existe")








