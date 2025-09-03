#Calculadora de áreas
#Autor: Erick Alfredo Ponce Rubio
#Grupo: 6010

print("Bienvenido a la calculadora matemática")

#Mostrar el menú de operaciones
print("\nElige la figura que deseas analizar:")
print("1. Rectángulo")
print("2. Cuadrado")
print("3. Círculo")
print("4. Triángulo")
print("5. Rombo")
print("6.Romboide")

opcion=input("Ingresa el número de la figura que deseas analizar:")

#Evaluar la opción seleccionada
if opcion == "1":
    base = float(input("Ingresa el valor de la base:"))
    altura = float(input("Ingresa el valor de la altura:")) 
    resultado = base*altura
    print("El área de tu figura es:", resultado)
elif opcion == "2":
    lado_1 = float(input("Ingresa el valor del primer lado:"))
    resultado = lado_1*lado_1
    print("El área de tu figura es:", resultado)
elif opcion == "3":
    radio = float(input("Ingresa el valor del radio:"))
    resultado = radio*radio*3.1416
    print("El área de tu figura es:", resultado)
elif opcion == "4":
    base = float(input("Ingresa el valor de la base:"))
    altura = float(input("Ingresa el valor de la altura:")) 
    resultado = (base * altura)/2
    print("El área de tu figura es:", resultado)
elif opcion == "5":
    diagonal_mayor = float(input("Ingresa el valor de la diagonal mayor:"))
    diagonal_menor = float(input("Ingresa el valor de la diagonal menor:"))
    resultado = (diagonal_mayor*diagonal_menor)/2
    print("El área de tu figura es:", resultado)
elif opcion == "6":
    base = float(input("Ingresa el valor de la base:"))
    altura = float(input("Ingresa el valor de la altura:")) 
    resultado = base*altura
    print("El área de tu figura es:", resultado)