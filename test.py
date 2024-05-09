
"""
-Hacer un programa que muestre todos los números impares entre dos numeros que elija o decida el usuario
"""

numero1= int(input("Introduce un número: "))
numero2= int(input("Introduce un segundo número: "))

if numero1 < numero2:
    for i in range(numero1,(numero2+1)):
        if i%2 == 0:                      
            print(f"{i} es PAR")
        else:
            print(f"{i} es IMPAR")            
         


else:
    print("numero 1 debe ser mayor al numero 2")