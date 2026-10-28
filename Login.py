#1_Login

def registrar_usuario():
    print("    CINEMATIC - CREAR CUENTA    ")

    while True:
        usuario = input("Ingrese su nombre de usuario: ")
        if usuario.isalpha():
            usuario_guardado = usuario
            break
        print("El usuario debe contener solo letras. Intente nuevamente.")

    while True:
        contraseña = input("Ingrese su contraseña: ")
        if contraseña.isdigit() and len(contraseña) == 4:
            contraseña_guardada = contraseña
            break
        print("La contraseña debe contener solo 4 números. Intente nuevamente.")

    rol_guardado = "cliente"
    print("¡Cuenta creada con éxito!.")
    return usuario_guardado, contraseña_guardada, rol_guardado

def iniciar_sesion(usuario_guardado, contraseña_guardada, rol_guardado):
    print("   CINEMATIC - INICIAR SESIÓN    ")

    usuario = input("Introduce tu Usuario: ").strip()
    contraseña = input("Introduce tu Contraseña: ").strip()

    if usuario.lower() == "PRAC" and contraseña == "2026":
        print("Acceso concedido com ADMINISTRADOR. Cargando base de datos...")
        return True, "administrador"

    if usuario_guardado == "":
        print("No hay usuarios registrados. Por favor, regístrate primero.")
        return False

    if usuario == usuario_guardado and contraseña == contraseña_guardada:
        print("Acceso concedido. Cargando tu perfil...")
        print("")
        return True, rol_guardado

    print("El usuario o la contraseña son incorrectos. Intenta nuevamente.")
    return False