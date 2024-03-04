# El registro de usuarios corresponde a un diccionario que contiene el nombre de los usuarios registrados y los valores asociados a cada usuario, un segundo diccionario con el correo electrónico y el pin de acceso.


## Definir los componentes del diccionario (inicialmente vacío)

usuariosRegistrados = {}
                
# Primera opción del software: 
## Extraer la información de un usuario existente
 
def usuarioExistente():
    global usuariosRegistrados
    usuarioNombre = input("\nIntroduzca su nombre de usuario: ")
    if usuarioNombre in usuariosRegistrados.keys():       
        # Verificación del usuario
        pin = input("Introduzca su pin: ")
        if usuariosRegistrados[usuarioNombre]['pin'] == int(pin):
            print("\n ¡Hola " + usuarioNombre + "!\n")
            print("Tu correo electrónico registrado es: ")
            print(usuariosRegistrados[usuarioNombre]['correo'])
        else:
            print("El pin proporcionado no corresponde con el usuario")
    # Si el usuario no existe en el diccionario:
    else:
        print("\n MENSAJE: El usuario no existe. Intente de nuevo o ingrese nuevo usuario\n")
        
                       
# Segunda opción del software;
## Crear un nuevo usuario

def nuevoUsuario():
    global usuariosRegistrados
    nuevoUsuario = input("Ingrese el nombre de usuario: ")
    correo = input("Ingrese el correo electrónico: ")
    pin = input("Ingrese el pin: ")
    usuariosRegistrados[nuevoUsuario] = {'correo': correo, 'pin': int(pin)}
    print("Registro exitoso. Ahora puede iniciar sesión.")    

    

while True: 
    print("\n Bienvenido a SmartHome.\n")
    print("¿Qué deseas hacer?")
    print("1. Ingresar con tu usuario")
    print("2. Agregar usuario")
    print("3. Salir")
    opcion = input("Por favor seleccione una opción: ")
    
    if opcion == "1":
        usuarioActual = usuarioExistente()
        if usuarioActual:
            otraOpcion = input("Elija una opción: ")
            if otraOpcion == "2":
                nuevoUsuario()
            elif otraOpcion == "3":
                print("Sesión finalizada. ¡Hasta luego!")
                break
            else:
               print("Su selección no es compatible. Intente de nuevo")
    elif opcion == "2":
        nuevoRegistro = nuevoUsuario()
        
    elif opcion == "3":
        print("\n Sesión finalizada. ¡Hasta luego!")
        break
        
    else:
        print("Su selección no es compatible. Intente de nuevo")
      

