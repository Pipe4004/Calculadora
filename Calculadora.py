num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: ")) 

valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 
            2- Restar
            3- Multiplicar
            4- dividir 
        """)

    valor = int(input("Elija una de las opciones: ") )     

    if valor == 1:
        print("El resultado de la suma es",num1+num2)
        break;
    if valor == 2:
        print("El resultado de la resta es",num1-num2)
        break;
    if valor == 3:
        print("la multiplicacion es",num1*num2)
        break;
    if valor == 4:
        print("la division es",num1/num2)
        break;
    else:
        print("Opcion incorrecta")
        break;
