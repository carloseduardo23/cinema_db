from mysql import connector

class Model:
    """
    *******************************************
    * A data model with MySQL for a cinema DB *
    *******************************************
    """
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    """
    *************************
    * Users methods        *
    *************************
    """
    def create_user(self, name, sname1, sname2, phone, email, credit_card):
        try:
            sql = 'INSERT INTO users (`u_name`, `u_sname1`, `u_sname2`, `u_phone`, `u_email`, `u_credit_card`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (name, sname1, sname2, phone, email, credit_card)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_user(self, id_user):
        try:
            sql = 'SELECT * FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_users(self):
        try:
            sql = 'SELECT * FROM users'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_user_name(self, name):
        try:
            sql = 'SELECT * FROM users WHERE u_name = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE users SET '+','.join(fields)+' WHERE id_user = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    *************************
    * Movies methods        *
    *************************
    """
    def create_movie(self, name, genre, description, duration, clasification):
        try:
            sql = 'INSERT INTO movies (`m_name`, `m_genre`, `m_description`, `m_duration`, `m_clasification`) VALUES (%s, %s, %s, %s, %s)'
            vals = (name, genre, description, duration, clasification)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_movie(self, id_movie):
        try:
            sql = 'SELECT * FROM movies WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM movies'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movie_name(self, name):
        try:
            sql = 'SELECT * FROM movies WHERE m_name = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movies SET '+','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_movie(self, id_movie):
        try:
            sql = 'DELETE FROM movies WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *************************
    * Halls methods         *
    *************************
    """
    def create_hall(self, id_hall, name, total_seats):
        try:
            sql = 'INSERT INTO halls (`id_hall`, `h_name`, `h_total_seats`) VALUES (%s, %s, %s)'
            vals = (id_hall, name, total_seats)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_hall(self, id_hall):
        try:
            sql = 'SELECT * FROM halls WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_halls(self):
        try:
            sql = 'SELECT * FROM halls'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_halls_name(self, name):
        try:
            sql = 'SELECT * FROM halls WHERE h_name = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records 
        except connector.Error as err:
            return err

    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE halls SET '+','.join(fields)+' WHERE id_hall = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_hall(self, id_hall):
        try:
            sql = 'DELETE FROM halls where id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *************************
    * Schedules methods     *
    *************************
    """
    def create_schedule(self, id_schedule, id_movie, id_hall, showtime):
        try:
            sql = 'INSERT INTO schedules (`id_schedule`, `id_movie`, `id_hall`, `s_showtime`) VALUES (%s, %s, %s, %s)'
            vals = (id_schedule, id_movie, id_hall, showtime)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_schedule(self, id_schedule):
        try:
            sql = 'SELECT movies.*, halls.*, schedules.* FROM schedules JOIN movies ON movies.id_movie = schedules.id_movie and schedules.id_schedule = %s JOIN halls ON halls.id_hall = schedules.id_hall'
            vals = (id_schedule,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_schedules(self):
        try:
            sql = 'SELECT movies.*, halls.*, schedules.* FROM schedules JOIN movies ON movies.id_movie = schedules.id_movie JOIN halls ON halls.id_hall = schedules.id_hall'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_schedule(self, fields, vals):
        try:
            sql = 'UPDATE schedules SET '+','.join(fields)+' WHERE id_schedule = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_schedule(self, id_schedule):
        try:
            sql = 'DELETE FROM schedules WHERE id_schedule = %s'
            vals = (id_schedule,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *************************
    * Seats methods         *
    *************************
    """
    def create_seat(self, id_seat, no_seat, state, id_hall):
        try:
            sql = 'INSERT INTO seats (`id_seat`, `no_seat`, `s_state`, `id_hall`) VALUES (%s, %s, %s, %s)'
            vals = (id_seat, no_seat, state, id_hall)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_seat(self, id_seat):
        try:
            sql = 'SELECT * FROM seats WHERE id_seat = %s'
            vals = (id_seat,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_seats(self, id_hall):
        try:
            sql = 'SELECT * FROM seats WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE seats SET '+','.join(fields)+' WHERE id_seat = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_seat(self, id_seat):
        try:
            sql = 'DELETE FROM seats WHERE id_seat = %s'
            vals = (id_seat,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ******************************
    * Type Tickets methods       *
    ******************************
    """
    def create_type_ticket(self, tt_name, tt_price):
        try:
            sql = 'INSERT INTO type_tickets (`tt_name`, `tt_price`) VALUES (%s, %s)'
            vals = (tt_name, tt_price)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_type_ticket(self, name):
        try:
            sql = 'SELECT * FROM type_tickets WHERE tt_name = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_type_tickets(self):
        try: 
            sql = 'SELECT * FROM type_tickets'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_type_ticket(self, fields, vals):
        try:
            sql = 'UPDATE type_tickets SET '+','.join(fields)+' WHERE tt_name = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_type_ticket(self, name):
        try:
            sql = 'DELETE FROM type_tickets WHERE tt_name = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *************************
    * Tickets methods       *
    *************************
    """ 
    def create_ticket_user(self, id_movie, id_hall, id_user, loanDate, id_seat, name):
        try:
            sql = 'INSERT INTO tickets (`id_movie`, `id_hall`, `id_user`, `t_date`, `id_seat`, `tt_name`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (id_movie, id_hall, id_user, loanDate, id_seat, name)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_ticket(self, id_ticket):
        try:
            sql = 'SELECT tickets.t_date, movies.m_name, movies.m_clasification, halls.id_hall, users.u_name, users.u_sname1, users.u_sname2, type_tickets.tt_price, seats.id_seat FROM tickets JOIN movies ON movies.id_movie = tickets.id_movie JOIN halls ON halls.id_hall = tickets.id_hall JOIN users ON users.id_user = tickets.id_user JOIN seats ON seats.id_seat = tickets.id_seat JOIN type_tickets ON type_tickets.tt_name = tickets.tt_name AND tickets.id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_tickets(self):
        try:
            sql = 'SELECT tickets.t_date, movies.m_name, movies.m_clasification, halls.id_hall, users.u_name, users.u_sname1, users.u_sname2, type_tickets.tt_price, seats.id_seat FROM tickets JOIN movies ON movies.id_movie = tickets.id_movie JOIN halls ON halls.id_hall = tickets.id_hall JOIN users ON users.id_user = tickets.id_user JOIN seats ON seats.id_seat = tickets.id_seat JOIN type_tickets ON type_tickets.tt_name = tickets.tt_name'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_date(self, date):
        try:
            sql = 'SELECT tickets.t_date, movies.m_name, movies.m_clasification, halls.id_hall, users.u_name, users.u_sname1, users.u_sname2, type_tickets.tt_price, seats.id_seat FROM tickets JOIN movies ON movies.id_movie = tickets.id_movie JOIN halls ON halls.id_hall = tickets.id_hall JOIN users ON users.id_user = tickets.id_user JOIN seats ON seats.id_seat = tickets.id_seat JOIN type_tickets ON type_tickets.tt_name = tickets.tt_name AND tickets.t_date = %s'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ticket(self, fields, vals):
        try:
            sql = 'UPDATE tickets SET '+','.join(fields)+' WHERE id_ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ticket(self, id_ticket):
        try:
            sql = 'DELETE FROM tickets WHERE id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count 
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ********************************
    * Administrators methods       *
    ********************************
    """ 
    def create_admin(self, name, sname1, sname2, phone, email, charge):
        try:
            sql = 'INSERT INTO administrators (`a_name`, `a_sname1`, `a_sname2`, `a_phone`, `a_email`, `a_charge`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals = (name, sname1, sname2, phone, email, charge)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_admin(self, id_admin):
        try:
            sql = 'SELECT * FROM administrators WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_admins(self):
        try:
            sql = 'SELECT * FROM administrators'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_admins_name(self, name):
        try:
            sql = 'SELECT * FROM administrators WHERE a_name = %s'
            vals = (name,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE administrators SET '+','.join(fields)+' WHERE id_admin = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    def delete_admin(self, id_admin):
        try:
            sql = 'DELETE FROM administrators WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
