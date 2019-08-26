def mostrar_menu(saldo=0):
    op  = 0    

    print(saldo)
    print("Bienvenido al portal del Banco Amigo. Escoja una opción: ")
  
    while op != 4:

        print("1. Consultar saldo ")
        print("2. Hacer depósito ")
        print("3. Realizar giro")
        print("4. Salir") 

        op = int(input())

        if op not in [1, 2, 3, 4]:
            print("Opcion no contemplada")
            continue

        if op ==1 :
            print("Su saldo es: {} ".format(saldo))
        
        elif op == 2:
            monto = float(input())
            saldo = depositar(saldo, monto) 
            print("Su saldo actualizado es: {}".format(saldo)) 
        
        elif op ==3:
            if saldo<=0:
                print("Su saldo es 0, no se puede realizar la transferencia")     
            else:
                saldo_aux = False
                while saldo_aux is False:

                    monto = float(input("Ingrese monto a girar: "))
                    saldo_aux = girar(saldo, monto)
                
                    if type(saldo_aux)== type(True) and not saldo_aux:
                        print("No disponer de suficientes fondos.")
                        print("Su saldo es:{}".format(saldo))
                    else:
                        saldo = saldo_aux    
        elif op != 4:
            print("Esa opcion no es valida")
    print()



def depositar(saldo, cantidad):
    return saldo + cantidad

def girar(saldo, cantidad):
    if cantidad>saldo:
        return False
    return saldo - cantidad   

if __name__ == "__main__":
    mostrar_menu()


