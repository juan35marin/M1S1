alor1 = int(input("ingrese un numero: "))
valor2 = float(input("Ingrese un numero: "))

resul1 = print(type(valor1).__name__)
result2 = print(type(valor2).__name__)
print(f"el primer numero es un {resul1} y el segundo es un {result2}")

opcion = int(input("Ingrese opcion")) 

if opcion == 1:
    suma = valor1 + valor2
    print(f"El resultado es: {suma}")
elif opcion == 2:
    resta = valor1 - valor2
    print(f"El resultado es: {resta} ")
elif opcion == 3:
    multi = valor1 * valor2
    print(f"La respuesta es: {multi}")
elif opcion == 4:
    div = valor1 / valor2
    print(f"El resultado es: {div} ")
else:
    print("chaoooooo")
    
valor3 = str(input("ingrese palabra: "))
if valor3 == "hola":
    print("Son iguales")
    
print("Encienda dispositivo")
encendido = False
conectado = True

if not encendido and conectado:
    print("Encender el dispositivo")
