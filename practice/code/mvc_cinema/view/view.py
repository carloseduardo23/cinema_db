class View:
    """
    **************************
    * A view for a cinema DB *
    **************************
    """
    def start(self):
        print('===============================')
        print('= Bienvenido a Cinemex Via Alta')
        print('===============================')

    def end(self):
        print('===============================')
        print('=      Vuelva pronto :D!      =')
        print('===============================')

    def menu_users(self):
        print('************************************')
        print('* --Selecciona el tipo de usuario-- *')
        print('************************************')
        print('1. Usuario General')
        print('2. Administrador')
        print('3. Salir')

    def menu_for_user(self):
        print('************************')
        print('* --Cinemex Via Alta-- *')
        print('************************')
        print('1. Consultar cartelera')
        print('2. Comprar un boleto')
        print('3. Salir')

    def main_menu_admin(self):
        print('*****************************')
        print('* --Menu de administrador-- *')
        print('*****************************')
        print('1. Usuarios')
        print('2. Peliculas')
        print('3. Salas')
        print('4. Asientos')
        print('5. Cartelera')
        print('6. Tipos de boleto')
        print('7. Tickets')
        print('8. Administradores')
        print('9. Salir')

    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')

    def ask(self, output):
        print(output, end = '')

    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    
    """
    ************************
    * Views for Users      *
    ************************
    """
    def users_menu(self):
        print('************************')
        print('* --Submenu Usuarios-- *')
        print('************************')
        print('1. Agregar un usuario')
        print('2. Mostrar un usuario')
        print('3. Mostrar todos los usuarios')
        print('4. Mostrar usuarios por nombre')
        print('5. Actualizar un usuario')
        print('6. Eliminar un usuario')
        print('7. Regresar')

    def show_user(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido paterno: ', record[2])
        print('Apellido materno: ', record[3])
        print('Telefono: ', record[4])
        print('Email: ', record[5])
        print('Tarjeta de credito: ', record[6])

    def show_user_header(self, header):
        print(header.center(55,'*'))
        print('-'*55)

    def show_user_midder(self):
        print('-'*55)

    def show_user_footer(self):
        print('*'*55)

    """
    *************************
    * Views for Movies      *
    *************************
    """
    def movies_menu(self):
        print('*************************')
        print('* --Submenu Peliculas-- *')
        print('*************************')
        print('1. Agregar una pelicula')
        print('2. Mostrar una pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas por nombre')
        print('5. Actualizar una pelicula')
        print('6. Eliminar una pelicula')
        print('7. Regresar')

    def show_movies(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1])
        print('Genero: ', record[2])
        print('Descripcion: ', record[3])
        print('Duracion: ', record[4])
        print('Clasificacion: ', record[5])

    def show_movie_header(self, header):
        print(header.center(76,'*'))
        print('-'*76)

    def show_movie_midder(self):
        print('-'*76)

    def show_movie_footer(self):
        print('*'*76)

    """
    ************************
    * Views for Halls      *
    ************************
    """
    def halls_menu(self):
        print('*********************')
        print('* --Submenu Salas-- *')
        print('*********************')
        print('1. Agregar una sala')
        print('2. Mostrar una sala')
        print('3. Mostrar todas las salas')
        print('4. Mostrar salas por nombre')
        print('5. Actualizar una sala')
        print('6. Eliminar una sala')
        print('7. Regresar')

    def show_hall(self, record):
        print(f'{record[0]:<2}|{record[1]:<35}|{record[2]:<12}')

    def show_hall_header(self, header):
        print(header.center(51,'*'))
        print('ID'.ljust(2)+'|'+'Nombre'.ljust(35)+'|'+'No. Asientos'.ljust(12))
        print('-'*51)

    def show_hall_midder(self):
        print('-'*51)

    def show_hall_footer(self):
        print('*'*51)

    """
    ****************************
    * Views for Schedules      *
    ****************************
    """
    def schedules_menu(self):
        print('*************************')
        print('* --Submenu Funciones-- *')
        print('*************************')
        print('1. Agregar una funcion')
        print('2. Mostrar una funcion')
        print('3. Mostrar todas las funciones')
        print('4. Actualizar una funcion')
        print('5. Eliminar una funcion')
        print('6. Regresar')

    def show_schedule(self, record):
        print(f'{record[1]:<60}|{record[5]:<13}|{record[6]:<4}|{record[12]:<5}')

    def show_schedule_header(self, header):
        print(header.center(86,'*'))
        print('Nombre'.ljust(60)+'|'+'Clasificacion'.ljust(13)+'|'+'Sala'.ljust(4)+'|'+'Hora'.ljust(5))
        print('-'*86)

    def show_schedule_midder(self):
        print('-'*86)

    def show_schedules_footer(self):
        print('*'*86)

    """
    ************************
    * Views for Seats      *
    ************************
    """
    def seats_menu(self):
        print('************************')
        print('* --Submenu Asientos-- *')
        print('************************')
        print('1. Agregar un asiento')
        print('2. Mostrar un asiento')
        print('3. Mostrar todos los asientos por sala')
        print('4. Actualizar un asiento')
        print('5. Eliminar un asiento')
        print('6. Regresar')

    def show_seat(self, record):
        print(f'{record[0]:<3}|{record[1]:<7}|{record[2]:<8}|{record[3]:<4}')
    
    def show_seat_header(self, header):
        print(header.center(81,'*'))
        print('ID'.ljust(3)+'|'+'Asiento'.ljust(7)+'|'+'Estado'.ljust(8)+'|'+'Sala'.ljust(4))
        print('-'*81)

    def show_seat_midder(self):
        print('-'*81)

    def show_seat_footer(self):
        print('*'*81)

    """
    *******************************
    * Views for Type Tickets      *
    *******************************
    """
    def type_ticket_menu(self):
        print('*******************************')
        print('* --Submenu Tipo de Boletos-- *')
        print('*******************************') 
        print('1. Agregar un tipo de boleto')
        print('2. Mostrar un tipo de boleto')
        print('3. Mostrar todos los tipos de boletos')
        print('4. Actualiza un tipo de boleto')
        print('5. Elimina un tipo de boleto')
        print('6. Regresar')

    def show_type_ticket(self, record):
        print(f'{record[0]:<10}|{record[1]:<5}')

    def show_type_ticket_header(self, header):
        print(header.center(17,'*'))
        print('Tipo'.ljust(10)+'|'+'Precio'.ljust(5))
        print('-'*17)

    def show_type_ticket_midder(self):
        print('-'*17)

    def show_type_ticket_footer(self):
        print('*'*17)

    def show_ticket_total(self, record):
        print('Total del ticket: '+str(record[7]))

    """
    **************************
    * Views for Tickets      *
    **************************
    """
    def tickets_menu(self):
        print('***********************')
        print('* --Submenu Tickets-- *')
        print('***********************')
        print('1. Mostrar un ticket')
        print('2. Mostrar todos los tickets')
        print('3. Mostrar los tickets de un dia')
        print('4. Actualizar un ticket')
        print('5. Eliminar un ticket')
        print('6. Regresar')

    def show_ticket(self, record):
        print('Fecha: ', record[0])
        print('Pelicula: ', record[1])
        print('Clasificacion: ', record[2])
        print('Sala: ', record[3])
        print('Asiento: ', record[8])
        print('Datos del Usuario')
        print('Nombre: ', record[4])
        print('Apellido parterno: ', record[5])
        print('Apellido Maternos: ', record[6])

    def show_ticket_header(self, header):
        print(header.center(60,'+'))

    def show_ticket_midder(self):
        print('/'*60)

    def show_ticket_footer(self):
        print('+'*60)

    """
    *********************************
    * Views for Administrators      *
    *********************************
    """
    def admins_menu(self):
        print('*******************************')
        print('* --Submenu Administradores-- *')
        print('*******************************')
        print('1. Agregar un administrador')
        print('2. Mostrar un administrador')
        print('3. Mostrar todos los administradores')
        print('4. Buscar un administrador por nombre')
        print('5. Actualizar un administrador')
        print('6. Eliminar un administrador')
        print('7. Regresar')

    def show_admin(self, record):
        print('ID Admin: ', record[0])
        print('Nombre: ', record[1])
        print('Apellido paterno: ', record[2])
        print('Apellido materno: ', record[3])
        print('Telefono: ', record[4])
        print('Email: ', record[5])
        print('Cargo: ', record[6])

    def show_admin_header(self, header):
        print(header.center(55,'*'))
        print('-'*55)

    def show_admin_midder(self):
        print('-'*55)

    def show_admin_footer(self):
        print('*'*55)