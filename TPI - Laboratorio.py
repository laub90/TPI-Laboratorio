u_medida = str(input("Ingrese la un de medida a utilizar: "))

longitud = int(input("Ingrese la longitud de la superficie: "))
ancho = int(input("Ingrese la anchura de la superficie: "))
altura = int(input("Ingrese la altura de la superficie: "))

metros_cubicos = longitud * ancho * altura

print("La cantidad de hormigon requerida es ", metros_cubicos, u_medida)