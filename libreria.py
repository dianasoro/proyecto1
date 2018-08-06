listaUsers = []

def registro(nickname,password):
    nuevoUser = {"nickname":nickname,
                 "password":password,}
    listaUsers.append(nuevoUser)


def login(nickname, password):
    for user in listaUsers:
        if user ["nickname"] == nickname:
            if user["password"] == password:
                return ("Bienvenido al sistema!")
            else:
                return "El password no coincide."
    return "El user no existe."


def menu():
    print("MENU \n"
          "1) Logearse.\n"
          "2) Registrarse.\n"
          "3) Salir.")
    opcion = input("Ingrese el número de accion a realizar:")

    if opcion == "1":
        nickname = input("Ingrese su user.")
        password = input("Ingrese su password.")
        print(login(nickname, password))

    elif opcion == "2":
        nickname = input("Ingrese su user.")
        password = input("Ingrese su password.")
        registro(nickname, password)
    menu()

menu()