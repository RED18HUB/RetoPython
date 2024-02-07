num_usuarios = int(input("¿Cuántos nuevos usuarios deseas registrar? "))
lista_usuarios = []

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
