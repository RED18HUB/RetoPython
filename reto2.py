num_usuarios = int(input("¿Cuántos nuevos usuarios deseas registrar? "))

for i in range(num_usuarios):
    nombre = input(" Ingrese el Nombre: ")
    apellidos = input("Inngrese el Apellidos: ")
    telefono = input("Ingrese  su Numero de Teléfono: ")
    correo = input("C Ingrese su correo electrónico: ")

    while len(nombre) < 5 or len(nombre) > 50 or len(apellidos) < 5 or len(apellidos) > 50 or len(correo) < 5 or len(correo) > 50 or len(telefono) == 10 or not telefono.isdigit():
        print("Por favor, asegúrate de que nombre, apellidos y correo tengan una longitud mínima de 5 caracteres y máxima de 50, y que el teléfono tenga 10 dígitos.")
        nombre = input(" Ingrese el Nombre: ")
    apellidos = input("Inngrese el Apellidos: ")
    telefono = input("Ingrese  su Numero de Teléfono: ")
    correo = input("C Ingrese su correo electrónico: ")

    print("-----***-----")
    print(f"Hola: {nombre}")
    print(f"  {apellidos}")
    print(f"en breve recibirás un correo a: {correo}")


