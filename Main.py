#4_Main 

import Login
import Funciones
import Administrador

print("")
print(" BIENVENIDO A CINEMATIC ")
print("")

while True:
    print("1. Iniciar sesión")
    print("2. Crear cuenta nueva")
    print("3. Cerrar programa")
    print("-" * 40)

    print("")    
    opcion_inicio = input("Seleccione una opción para empezar: ").strip()
    print('')

    if opcion_inicio == "1":
        while True:

            cuenta_activa = Login.iniciar_sesion()

            if cuenta_activa:
                if cuenta_activa["rol"] == "administrador":
                    print(f"Bienvenido, Administrador: {cuenta_activa['usuario']}")
                    Administrador.menu_administrador()

                else:
                    print(f"Bienvenido Cliente: {cuenta_activa['usuario']}")
                    Funciones.menu_cliente(cuenta_activa["usuario"])

                break

            else:
                print("")
             
    elif opcion_inicio == "2":

        Login.registrar_usuario()
        print("Ya puede iniciar sesión.")
        print('')
        
    elif opcion_inicio == "3" or opcion_inicio.upper() == "SALIR":
        print("Apagando servidores de Cinematic...")
        print("Que pases una buena noche de películas. Bye")
        break
    else:
        print("Opción inválida. Por favor, selecciona 1, 2 o 3.")
        print("-" * 40)