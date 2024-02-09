
lista_usuarios = []


while True:
    print("Menu de Inicio:")
    print("1. Agregar Usuario")
    print("2. Listar Id de los Usuarios")
    print("3. Ver el usuario segun el ID")
    print("4. Editar el usuario segun el ID")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        num_usuarios = int(input("¿Cuántos nuevos usuarios deseas registrar? "))
        for _ in range(num_usuarios):
            nombre = input("Ingrese el Nombre: ")
            apellidos = input("Ingrese el Apellido: ")
            telefono = input("Ingrese su Numero de Teléfono: ")
            correo = input("Ingrese su correo electrónico: ")

            while not (5 <= len(nombre) <= 50 and 5 <= len(apellidos) <= 50 and len(telefono) == 10 and 5 <= len(correo) <= 50):
                print("Por favor, asegúrate de que nombre, apellidos y correo tengan una longitud mínima de 5 caracteres y máxima de 50, y que el teléfono tenga 10 dígitos.")
                nombre = input("Ingrese el Nombre: ")
                apellidos = input("Ingrese el Apellido: ")
                telefono = input("Ingrese su Numero de Teléfono: ")
                correo = input("Ingrese su correo electrónico: ")

            usuario = {
                "id": len(lista_usuarios) + 1,
                "nombre": nombre,
                "apellidos": apellidos,
                "telefono": telefono,
                "correo": correo
            }
            lista_usuarios.append(usuario)

            print("-----***-----")
            print(f"Hola {nombre} {apellidos}, en breve recibirás un correo a: {correo}")
            print("-----***-----")

        print(lista_usuarios)
    elif opcion == "2":
        print("Listado de IDs de Usuarios:")
        for usuario in lista_usuarios:
            print(usuario["id"])
    elif opcion == "3":
        id_usuario=int(input("Ingrese el id a Buscar"))
        encontrado = False
        for usuario in lista_usuarios:
            if usuario["id"] == id_usuario:
                encontrado = True
                print("Información del Usuario:")
                print(f"ID: {usuario['id']}")
                print(f"Nombre: {usuario['nombre']}")
                print(f"Apellidos: {usuario['apellidos']}")
                print(f"Teléfono: {usuario['telefono']}")
                print(f"Correo electrónico: {usuario['correo']}")
                break

        if not encontrado:
            print("No se encontró ningún usuario con el ID proporcionado.")

    elif opcion == "4":
        id_usuario=int(input("Ingrese el id a Editar"))
        encontrado = False
        for usuario in lista_usuarios:
            if usuario["id"] == id_usuario:
                encontrado = True
                print("Editar información del Usuario:")
                nombre = input("Ingrese el nuevo Nombre: ")
                apellidos = input("Ingrese los nuevos Apellidos: ")
                telefono = input("Ingrese el nuevo Número de Teléfono: ")
                correo = input("Ingrese el nuevo correo electrónico: ")

                while not (5 <= len(nombre) <= 50 and 5 <= len(apellidos) <= 50 and len(telefono) == 10 and 5 <= len(correo) <= 50):
                    print("Por favor, asegúrate de que nombre, apellidos y correo tengan una longitud mínima de 5 caracteres y máxima de 50, y que el teléfono tenga 10 dígitos.")
                    nombre = input("Ingrese el nuevo Nombre: ")
                    apellidos = input("Ingrese los nuevos Apellidos: ")
                    telefono = input("Ingrese el nuevo Número de Teléfono: ")
                    correo = input("Ingrese el nuevo correo electrónico: ")

                usuario["nombre"] = nombre
                usuario["apellidos"] = apellidos
                usuario["telefono"] = telefono
                usuario["correo"] = correo
                print("Información actualizada correctamente.")
                break

        if not encontrado:
            print("No se encontró ningún usuario con el ID proporcionado.")


    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")


