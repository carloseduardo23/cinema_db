from model.model import Model
from view.view import View
from datetime import date

class Controller:
    """
    ********************************
    * A controller for a cinema DB *
    ********************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.menu_users()

    """
    ***********************
    * General Controllers *
    ***********************
    """
    def menu_users(self):
        o = '0'
        while o != '3':
            self.view.menu_users()
            self.view.option('3')
            o = input()
            if o == '1':
                self.menu_for_user()
            elif o == '2':
                self.main_menu_admin()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return

    def update_list(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    """
    ********************************
    * Controllers for General Users*
    ********************************
    """
    def menu_for_user(self):
        o = '0'
        while o != '3':
            self.view.menu_for_user()
            self.view.option('3')
            o = input()
            if o == '1':
                self.read_all_schedules()
            elif o == '2':
                self.create_ticket_user()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def read_all_schedules(self):
        schedules = self.model.read_all_schedules()
        if type(schedules) == list:
            self.view.show_schedule_header('Todas las funciones')
            for schedule in schedules:
                self.view.show_schedule(schedule)
                self.view.show_schedule_midder()
            self.view.show_schedules_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LA CARTELERA. REGRESA LUEGO')
        return
    
    def ask_ticket_user(self):
        self.view.ask('ID Pelicula: ')
        id_movie = input()
        self.view.ask('Sala: ')
        id_hall = input()
        self.view.ask('Usuario: ')
        id_user = input()
        today = date.today()
        loanDate = today.strftime('%d-%m-%y')
        self.view.ask('Asiento: ')
        id_seat = input()
        self.view.ask('Tipo boleto: ')
        name = input()
        return [id_movie,id_hall,id_user,loanDate,id_seat,name]

    def create_ticket_user(self):
        id_movie, id_hall, id_user, loanDate, id_seat, name = self.ask_ticket_user()
        out = self.model.create_ticket_user(id_movie, id_hall, id_user, loanDate, id_seat, name)
        if out == True:
            self.view.ok(id_user, 'compro')
        else:
            self.view.error('NO SE PUDO REALIZAR LA COMPRA. REVISA')
        return
        
    """
    *********************************
    * Controllers for Administrator *
    *********************************
    """
    def main_menu_admin(self):
        o = '0'
        while o != '9':
            self.view.main_menu_admin()
            self.view.option('9')
            o = input()
            if o == '1':
                self.users_menu()
            elif o == '2':
                self.movies_menu()
            elif o == '3':
                self.halls_menu()
            elif o == '4':
                self.seats_menu()
            elif o == '5':
                self.schedules_menu()
            elif o == '6':
                self.type_tickets_menu()
            elif o == '7':
                self.tickets_menu()
            elif o == '8':
                self.admins_menu()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
        return

    """
    ********************************
    * Controllers for admin. users *
    ********************************
    """
    def users_menu(self):
        o = '0'
        while o != '7':
            self.view.users_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_user()
            elif o == '2':
                self.read_user()
            elif o == '3':
                self.read_all_users()
            elif o == '4':
                self.read_user_name()
            elif o == '5':
                self.update_user()
            elif o == '6':
                self.delete_user()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_user(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno: ')
        sname2 = input()
        self.view.ask('Telefono: ')
        phone = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Tarjeta de Credito: ')
        credit_card = input()
        return [name,sname1,sname2,phone,email,credit_card]

    def create_user(self):
        name, sname1, sname2, phone, email, credit_card = self.ask_user()
        out = self.model.create_user(name, sname1, sname2, phone, email, credit_card)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agrego')
        else:
            self.view.error('PROBLEMAS AGREGAR EL USUARIO. REVISA')
        return

    def read_user(self):
        self.view.ask('ID usuario: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario '+id_user+' ')
            self.view.show_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL USUARIO. REVISA.')
        return

    def read_all_users(self): 
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_user_header('Todos los usuarios')
            for user in users:
                self.view.show_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR TODOS LOS USUARIOS. REVISA.')

    def read_user_name(self):
        self.view.ask('Nombre: ')
        name = input()
        names = self.model.read_user_name(name)
        if type(names) == list:
            self.view.show_user_header('Usuarios con nombre '+name+' ')
            for name in names:
                self.view.show_user(name)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTAR LOS USUARIOS. REVISA')
        return

    def update_user(self):
        self.view.ask('ID de usuario a modificar: ')
        id_user = input()
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Datos del usuario '+id_user+' ')
            self.view.show_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL USUARIO NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL USUARIO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_list(['u_name', 'u_sname1', 'u_sname2', 'u_phone', 'u_email', 'u_credit_card'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields, vals)
        if out == True:
            self.view.ok(id_user, 'actualizo')
        else:
            self.view.error('PROBLEMAS ACTUALIZAR EL USUARIO. REVISA.')
        return

    def delete_user(self):
        self.view.ask('ID de usuario a eliminar: ')
        id_user = input()
        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, 'elimino')
        else:
            if count == 0:
                self.view.error('EL USUARIO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR EL USUARIO. REVISA.')
        return

    """
    *********************************
    * Controllers for admin. movies *
    *********************************
    """

    def movies_menu(self):
        o = '0'
        while o != '7':
            self.view.movies_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4':
                self.read_movie_name()
            elif o == '5':
                self.update_movie()
            elif o == '6':
                self.delete_movie()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_movie(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Genero: ')
        genre = input()
        self.view.ask('Descripcion: ')
        description = input()
        self.view.ask('Duracion: ')
        duration = input()
        self.view.ask('Clasificacion: ')
        clasification = input()
        return [name,genre,description,duration,clasification]

    def create_movie(self):
        name, genre, description, duration, clasification = self.ask_movie()
        out = self.model.create_movie(name, genre, description, duration, clasification)
        if out == True:
            self.view.ok(name, 'agrego')
        else:
            self.view.error('PROBLEMAS AL AGREGAR LA PELICULA. REVISA.')
        return

    def read_movie(self):
        self.view.ask('ID pelicula: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula'+id_movie+' ')
            self.view.show_movies(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR LA PELICULA. REVISA.')
        return

    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) == list:
            self.view.show_movie_header('Todas las peliculas')
            for movie in movies:
                self.view.show_movies(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR TODAS LAS PELICULAS. REVISA.')
        return

    def read_movie_name(self):
        self.view.ask('Nombre: ')
        name = input()
        names = self.model.read_movie_name(name)
        if type(names) == list:
            self.view.show_movie_header('Datos de la pelicula '+name+' ')
            for name in names:
                self.view.show_movies(name)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR LAS PELICULAS. REVISA.') 
        return

    def update_movie(self):
        self.view.ask('ID de la pelicula a actualizar: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Datos de la pelicula'+id_movie+' ')
            self.view.show_movies(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR LA PELICULA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_list(['m_name', 'm_genre', 'm_description', 'm_duration', 'm_clasification'], whole_vals)
        vals.append(id_movie)
        vals = tuple(vals)
        out = self.model.update_movie(fields, vals)
        if out == True:
            self.view.ok(id_movie, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTUALIZAR LA PELICULA. REVISA.')
        return

    def delete_movie(self):
        self.view.ask('ID de pelicula a eliminar: ')
        id_movie = input()
        count = self.model.delete_movie(id_movie)
        if count != 0:
            self.view.ok(id_movie, 'elimino')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR LA PELICULA. REVISA.')
        return

    """
    ********************************
    * Controllers for admin. halls *
    ********************************
    """
    def halls_menu(self):
        o = '0'
        while o != '7':
            self.view.halls_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_hall()
            elif o == '3':
                self.read_all_halls()
            elif o == '4':
                self.read_halls_name()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                self.delete_hall()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_hall(self):
        self.view.ask('Sala: ')
        id_hall = input()
        self.view.ask('Nombre: ')
        h_name = input()
        self.view.ask('Total de asientos: ')
        total_seats = input()
        return [id_hall,h_name,total_seats]

    def create_hall(self):
        id_hall, h_name, total_seats = self.ask_hall()
        out = self.model.create_hall(id_hall, h_name, total_seats)
        if out == True:
            self.view.ok(id_hall, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA SALA YA EXISTE.')
            else:
                self.view.error('PROBLEMAS AL AGREGAR. REVISA.')
        return
    
    def read_hall(self):
        self.view.ask('Sala: ')
        id_hall = input()
        hall = self.model.read_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header('Datos de la sala '+id_hall+' ')
            self.view.show_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('LA SALA NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR LA SALA. REVISA.')
        return
    
    def read_all_halls(self):
        halls = self.model.read_all_halls()
        if type(halls) == list:
            self.view.show_hall_header('Todas las salas')
            for hall in halls:
                self.view.show_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('PROBLEMAS AL LEER TODAS LAS SALAS. REVISA.')

    def read_halls_name(self):
        self.view.ask('Nombre de la sala: ')
        h_name = input()
        halls = self.model.read_halls_name(h_name)
        if type(halls) == list:
            self.view.show_hall_header('Salas con nombre '+h_name+' ')
            for hall in halls:
                self.view.show_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('PROBLEMAS AL LEER LAS SALAS. REVISA.') 
        return

    def update_hall(self):
        self.view.ask('Sala a actualizar: ')
        id_hall = input()
        hall = self.model.read_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header('Datos de la sala '+id_hall+' ')
            self.view.show_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('LA SALA NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR LA SALA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_hall()
        fields, vals = self.update_list(['id_hall', 'h_name', 'h_total_seats'], whole_vals)
        vals.append(id_hall)
        vals = tuple(vals)
        out = self.model.update_hall(fields, vals)
        if out == True:
            self.view.ok(id_hall, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTULIZAR LA SALA. REVISA.')
        return

    def delete_hall(self):
        self.view.ask('Sala a eliminar: ')
        id_hall = input()
        count = self.model.delete_hall(id_hall)
        if count != 0:
            self.view.ok(id_hall, 'elimino')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR LA SALA. REVISA.') 
        return

    """
    ************************************
    * Controllers for admin. schedules *
    ************************************
    """
    def schedules_menu(self):
        o = '0'
        while o != '6':
            self.view.schedules_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_schedule()
            elif o == '2':
                self.read_schedule()
            elif o == '3':
                self.read_all_schedules()
            elif o == '4':
                self.update_schedule()
            elif o == '5':
                self.delete_schedule()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_schedule(self):
        self.view.ask('ID Funcion: ')
        id_schedule = input()
        self.view.ask('ID pelicula: ')
        id_movie = input()
        self.view.ask('Sala: ')
        id_hall = input()
        self.view.ask('Hora de funcion: ')
        showtime = input()
        return[id_schedule,id_movie,id_hall,showtime]

    def create_schedule(self):
        id_schedule, id_movie, id_hall, showtime = self.ask_schedule()
        out = self.model.create_schedule(id_schedule, id_movie, id_hall, showtime)
        if out == True:
            self.view.ok(id_schedule, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('LA FUNCION YA EXISTE.')
            else:
                self.view.error('PROBLEMAS AL AGREGAR LA FUNCION. REVISA.')
        return

    def read_schedule(self):
        self.view.ask('ID Funcion: ')
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header('Datos de la funcion')
            self.view.show_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedules_footer()
        else:
            if schedule == None:
                self.view.error('LA FUNCION NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR LA FUNCION. REVISA.')
        return

    def update_schedule(self):
        self.view.ask('ID Funcion: ')
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header('Datos de la funcion')
            self.view.show_schedule(schedule)
            self.view.show_schedule_midder()
            self.view.show_schedules_footer()
        else:
            if schedule == None:
                self.view.error('LA FUNCION NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR LA FUNCION. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_schedule()
        fields, vals = self.update_list(['id_schedule', 'id_movie', 'id_hall', 's_showtime'], whole_vals)
        vals.append(id_schedule)
        vals = tuple(vals)
        out = self.model.update_schedule(fields, vals)
        if out == True:
            self.view.ok(id_schedule, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTUALIZAR LA FUNCION. REVISA.')
        return

    def delete_schedule(self):
        self.view.ask('ID Funcion a eliminar: ')
        id_schedule = input()
        count = self.model.delete_schedule(id_schedule)
        if count != 0:
            self.view.ok(id_schedule, 'elimino')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR LA FUNCION. REVISA.')
        return

    """
    ********************************
    * Controllers for admin. seats *
    ********************************
    """
    def seats_menu(self):
        o = '0'
        while o != '6':
            self.view.seats_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_seat()
            elif o == '2':
                self.read_seat()
            elif o == '3':
                self.read_all_seats()
            elif o == '4':
                self.update_seat()
            elif o == '5':
                self.delete_seat()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_seat(self):
        self.view.ask('ID Asiento: ')
        id_seat = input()
        self.view.ask('Asiento: ')
        no_seat = input()
        s_state = 'free'
        self.view.ask('Sala: ')
        id_hall = input()
        return[id_seat,no_seat,s_state,id_hall]

    def create_seat(self):
        id_seat, no_seat, s_state, id_hall = self.ask_seat()
        out = self.model.create_seat(id_seat, no_seat, s_state, id_hall)
        if out == True:
            self.view.ok(id_seat, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL ASIENTO YA EXISTE.')
            else:
                self.view.error('PROBLEMAS AL AGREGAR EL ASIENTO. REVISA.') 
        return

    def read_seat(self):
        self.view.ask('Asiento: ')
        id_seat = input()
        seat = self.model.read_seat(id_seat)
        if type(seat) == tuple:
            self.view.show_seat_header('Datos del asiento'+id_seat+' ')
            self.view.show_seat(seat)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if seat == None:
                self.view.error('EL ASIENTO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL ASIENTO. REVISA.')
        return
    
    def read_all_seats(self):
        self.view.ask('Sala: ')
        id_hall = input()
        seats = self.model.read_all_seats(id_hall)
        if type(seats) == list:
            self.view.show_seat_header(' Todos los asientos de la sala '+id_hall+' ')
            for seat in seats:
                self.view.show_seat(seat)
                self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR TODOS LOS ASIENTOS. REVISA.')
        return

    def update_seat(self):
        self.view.ask('Asiento a actualizar: ')
        id_seat = input()
        seat = self.model.read_seat(id_seat)
        if type(seat) == tuple:
            self.view.show_seat_header('Datos del asiento '+id_seat+' ')
            self.view.show_seat(seat)
            self.view.show_seat_midder()
            self.view.show_seat_footer()
        else:
            if seat == None:
                self.view.error('EL ASIENTO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL ASIENTO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_seat()
        fields, vals = self.update_list(['id_seat', 'no_seat', 's_state', 'id_hall'], whole_vals)
        vals.append(id_seat)
        vals = tuple(vals)
        out = self.model.update_seat(fields, vals)
        if out == True:
            self.view.ok(id_seat, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTULIZAR EL ASIENTO. REVISA.')
        return

    def delete_seat(self):
        self.view.ask('ID del Asiento a eliminar: ')
        id_seat = input()
        count = self.model.delete_seat(id_seat)
        if count != 0:
            self.view.ok(id_seat, 'elimino')
        else:
            if count == 0:
                self.view.error('EL ASIENTO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR EL ASIENTO. REVISA.')
        return

    """
    ***************************************
    * Controllers for admin. type tickets *
    ***************************************
    """
    def type_tickets_menu(self):
        o = '0'
        while o != '6':
            self.view.type_ticket_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_type_ticket()
            elif o == '2':
                self.read_type_ticket()
            elif o == '3':
                self.read_all_type_tickets()
            elif o == '4':
                self.update_type_ticket()
            elif o == '5':
                self.delete_type_ticket()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_type_ticket(self):
        self.view.ask('Nombre: ')
        tt_name = input()
        self.view.ask('Precio: ')
        tt_price = input()
        return[tt_name,tt_price]

    def create_type_ticket(self):
        tt_name, tt_price = self.ask_type_ticket()
        out = self.model.create_type_ticket(tt_name, tt_price)
        if out == True:
            self.view.ok(tt_name, 'agrego')
        else:
            if out.errno == 1062:
                self.view.error('EL TIPO DE BOLETO YA EXISTE.')
            else:
                self.view.error('PROBLEMAS AL AGREGAR EL TIPO DE BOLETO. REVISA.')
        return

    def read_type_ticket(self):
        self.view.ask('Tipo de boleto: ')
        tt_name = input()
        name = self.model.read_type_ticket(tt_name)
        if type(name) == tuple:
            self.view.show_type_ticket_header('Datos del tipo '+tt_name+' ')
            self.view.show_type_ticket(name)
            self.view.show_type_ticket_midder()
            self.view.show_type_ticket_footer()
        else:
            if name == None:
                self.view.error('EL TIPO DE BOLETO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL TIPO DE BOLETO. REVISA.')
        return

    def read_all_type_tickets(self):
        names = self.model.read_all_type_tickets()
        if type(names) == list:
            self.view.show_type_ticket_header('Todos los tipos de boletos')
            for name in names:
                self.view.show_type_ticket(name)
                self.view.show_type_ticket_midder()
            self.view.show_type_ticket_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR TODOS LOS TIPOS DE BOLETOS. REVISA.')
        return

    def update_type_ticket(self):
        self.view.ask('Tipo de boleto a actualizar: ')
        tt_name = input()
        name = self.model.read_type_ticket(tt_name)
        if type(name) == tuple:
            self.view.show_type_ticket_header('Datos del tipo '+tt_name+' ')
            self.view.show_type_ticket(name)
            self.view.show_type_ticket_midder()
            self.view.show_type_ticket_footer()
        else:
            if name == None:
                self.view.error('EL TIPO DE BOLETO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL TIPO DE BOLETO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_type_ticket()
        fields, vals = self.update_list(['tt_name', 'tt_price'], whole_vals)
        vals.append(tt_name)
        vals = tuple(vals)
        out = self.model.update_type_ticket(fields, vals)
        if out == True:
            self.view.ok(tt_name, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTUALIZAR EL TIPO DE BOLETO. REVISA.')
        return

    def delete_type_ticket(self):
        self.view.ask('Tipo de boleto a eliminar: ')
        tt_name = input()
        count = self.model.delete_type_ticket(tt_name)
        if count != 0:
            self.view.ok(tt_name, 'elimino')
        else:
            if count == 0:
                self.view.error('EL TIPO DE BOLETO NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR EL TIPO DE BOLETO. REVISA.')
        return

    """
    **********************************
    * Controllers for admin. tickets *
    **********************************
    """
    def tickets_menu(self):
        o = '0'
        while o != '6':
            self.view.tickets_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_ticket()
            elif o == '2':
                self.read_all_tickets()
            elif o == '3':
                self.read_tickets_date()
            elif o == '4':
                self.update_ticket()
            elif o == '5':
                self.delete_ticket()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_ticket(self):
        self.view.ask('Fecha: ')
        t_date = input()
        self.view.ask('ID Pelicula: ')
        id_movie = input()
        self.view.ask('Sala: ')
        id_hall = input()
        self.view.ask('Usuario: ')
        id_user = input()
        self.view.ask('Tipo boleto: ')
        name = input()
        self.view.ask('Asiento: ')
        id_seat = input()
        return [t_date,id_movie,id_hall,id_user,name,id_seat]

    def read_ticket(self):
        self.view.ask('ID Ticket: ')
        id_ticket = input()
        ticket = self.model.read_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header('Datos del ticket '+id_ticket+' ')
            self.view.show_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_total(ticket)
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL TICKET. VUELVE MAS TARDE')
        return
    
    def read_all_tickets(self):
        tickets = self.model.read_all_tickets()
        if type(tickets) == list:
            self.view.show_ticket_header('Todos los tickets')
            for ticket in tickets:
                self.view.show_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
            self.view.show_ticket_total(ticket)
        else:
            self.view.error('PROBLEMAS A MOSTRAR TODOS LOS TICKETS. REVISA.')
        return

    def read_tickets_date(self):
        self.view.ask('Fecha: ')
        date = input()
        dates = self.model.read_tickets_date(date)
        if type(dates) == list:
            self.view.show_ticket_header('Tickets del dia '+date+' ')
            for date in dates:
                self.view.show_ticket(date)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
            self.view.show_ticket_total(date)
        else:
            self.view.error('PROBLEMAS AL MOSTRAR LOS TICKETS. REVISA.')
        return
    
    def update_ticket(self):
        self.view.ask('ID Ticket a actualizar: ')
        id_ticket = input()
        ticket = self.model.read_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header('Datos del ticket '+id_ticket+' ')
            self.view.show_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_total(ticket)
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL TICKET NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL LEER EL TICKET. VUELVE MAS TARDE')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_ticket()
        fields, vals = self.update_list(['t_date', 'id_movie', 'id_hall', 'id_user', 'name', 'id_seat'], whole_vals)
        vals.append(id_ticket)
        vals = tuple(vals)
        out = self.model.update_ticket(fields, vals)
        if out == True:
            self.view.ok(id_ticket, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTUALIZAR EL TICKET. REVISA.')
        return

    def delete_ticket(self):
        self.view.ask('ID Ticket a eliminar: ')
        id_ticket = input()
        count = self.model.delete_ticket(id_ticket)
        if count != 0:
            self.view.ok(id_ticket, 'elimino')
        else:
            if count == 0:
                self.view.error('EL TICKET NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR EL TICKET. REVISA.')
        return

    """
    **********************************
    * Controllers for administrators *
    **********************************
    """
    def admins_menu(self):
        o = '0'
        while o != '7':
            self.view.admins_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_admin()
            elif o == '2':
                self.read_admin()
            elif o == '3':
                self.read_all_admins()
            elif o == '4':
                self.read_admins_name()
            elif o == '5':
                self.update_admin()
            elif o == '6':
                self.delete_admin()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_admin(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        sname1 = input()
        self.view.ask('Apellido materno: ')
        sname2 = input()
        self.view.ask('Telefono: ')
        phone = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Cargo: ')
        charge = input()
        return[name,sname1,sname2,phone,email,charge]

    def create_admin(self):
        name, sname1, sname2, phone, email, charge = self.ask_admin()
        out = self.model.create_admin(name, sname1, sname2, phone, email, charge)
        if out == True:
            self.view.ok(name+' '+sname1+' '+sname2, 'agrego')
        else:
            self.view.error('PROBLEMAS AL AGREGAR EL ADMINISTRADOR. REVISA.')
        return

    def read_admin(self):
        self.view.ask('ID Admin: ')
        id_admin = input()
        admin = self.model.read_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header('Datos del admin '+id_admin+' ')
            self.view.show_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL ADMINISTRADOR. REVISA.')
        return

    def read_all_admins(self):
        admins = self.model.read_all_admins()
        if type(admins) == list:
            self.view.show_admin_header('Todos los administradores')
            for admin in admins:
                self.view.show_admin(admin)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR TODOS LOS ADMINISTRADORES. REVISA.')
        return

    def read_admins_name(self):
        self.view.ask('Nombre: ')
        name = input()
        names = self.model.read_admins_name(name)
        if type(names) == list:
            self.view.show_admin_header('Administradores con nombre '+name+' ')
            for name in names:
                self.view.show_admin(name)
                self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            self.view.error('PROBLEMAS AL MOSTRAR LOS ADMINISTRADORES. REVISA.')
        return

    def update_admin(self):
        self.view.ask('ID Admin a actualizar: ')
        id_admin = input()
        admin = self.model.read_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header('Datos del admin '+id_admin+' ')
            self.view.show_admin(admin)
            self.view.show_admin_midder()
            self.view.show_admin_footer()
        else:
            if admin == None:
                self.view.error('EL ADMINISTRADOR NO EXISTE')
            else:
                self.view.error('PROBLEMAS AL MOSTRAR EL ADMINISTRADOR. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_admin()
        fields, vals = self.update_list(['a_name', 'a_sname1', 'a_sname2', 'a_phone', 'a_email', 'a_charge'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields, vals)
        if out == True:
            self.view.ok(id_admin, 'actualizo')
        else:
            self.view.error('PROBLEMAS AL ACTUALIZAR EL ADMINISTRADOR. REVISA.')
        return

    def delete_admin(self):
        self.view.ask('ID Admin a eliminar: ')
        id_admin = input()
        count = self.model.delete_admin(id_admin)
        if count != 0:
            self.view.ok(id_admin, 'elimino')
        else:
            if count == 0:
                self.view.error('EL ADMINISTRADOR NO EXISTE.')
            else:
                self.view.error('PROBLEMAS AL ELIMINAR EL ADMINISTRADOR. REVISA.')
        return