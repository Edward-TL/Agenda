class Contact:

    def __init__(self, name, phone, email):
        self._name = name
        self._phone = phone
        self._email = email


class ContactBook:

    def __init__(self):
        self._contacts = []

    def add(self, name, phone, email):
        print(f'nombre: {name}, telefono: {phone} correo: {email}.')


def run():
    while True:
        command = str(input('''
        ¿Qué deseas hacer?
        [1] Añadir contacto
        [2] Actualizar contacto
        [3] Buscar contacto
        [4] Eliminar contacto
        [5] Listar contactos
        [0 o S] Salir
        '''))

        if command == '1':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el telefono del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            
            ContactBook().add(name, phone, email)
        elif command == '2':
            print('Actualizar contacto')
        elif command == '3':
            print('Buscar contacto')
        elif command == '4':
            print('Eliminar contacto')
        elif command == '5':
            print('istar contactos')
        elif command == '0' or command == "s" or command == "S":
            break
        else:
            print("Comando no encontrado.")

if __name__ == '__main__':
    print('BIENVENIDO A LA AGENDA')
    run()
