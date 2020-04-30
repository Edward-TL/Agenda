class Contact:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:

    def __init__(self):
        self.contacts = []

    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)

        numero = len(self.contacts)
        print(f'\nAhora hay {numero} contactos almacenados. \nContacto guardado:')
        print(f'Nombre: {contact.name}')
        print(f'Telefono: {contact.phone}')
        print(f'Correo: {contact.email}')

    def show_all(self):
        numero = len(self.contacts)
        print(f'Hay {numero} contactos almacenados')

        for contact in self.contacts:
            self._print_contact(contact)

    def _print_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- ')
        print('Nombre: {}'.format(contact.name))
        print('Telefono: {}'.format(contact.phone))
        print('Email: {}'.format(contact.email))
        print('--- * --- * --- * --- * --- * --- * --- ')

    def delete(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                print(f'\nContacto Eliminado:')
                print(f'Nombre: {contact.name}')
                print(f'Telefono: {contact.phone}')
                print(f'Correo: {contact.email}')
                del self.contacts[idx]
                break

    def search(self, name):
        gotcha = False
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(contact)
                gotcha = True
                break
        
        if gotcha == False:
            self._not_found()
                

    def _not_found(self):
        print('* * * * * * * * * * * *')
        print('Contacto no encontrado')
        print('* * * * * * * * * * * *')
        gotcha = False
        return gotcha


def run():

    contact_book = ContactBook()

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
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))

            contact_book.add(name, phone, email)

        elif command == '2':
            name = str(input('Qué contacto quieres actualizar?: '))
            contact_book.search(name)

            if gotcha == True:
                name = str(input('Escribe el nombre del contacto: '))
                phone = str(input('Escribe el telÃ©fono del contacto: '))
                email = str(input('Escribe el email del contacto: '))

                contact_book.update(name, phone, email)

        elif command == '3':

            name = str(input('¿A quién buscas?: '))

            contact_book.search(name)

        elif command == '4':
            name = str(input('Escribe el nombre del contacto: '))

            contact_book.delete(name)

        elif command == '5':

            contact_book.show_all()

        elif command == '0' or command == "s" or command == "S":
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('BIENVENIDO  A  LA  AGENDA')
    run()
