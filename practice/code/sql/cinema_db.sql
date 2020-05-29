drop database if exists cinema_db;
create database if not exists cinema_db;

use cinema_db;

create table if not exists users(
	id_user int not null auto_increment,
    u_name varchar(35) not null,
    u_sname1 varchar(35) not null,
    u_sname2 varchar(35),
    u_phone varchar(10),
    u_email varchar(80) not null,
    u_credit_card varchar(16) not null,
    primary key(id_user)
)engine=innoDB;

create table if not exists movies(
	id_movie int not null auto_increment,
    m_name varchar(60) not null,
    m_genre varchar(35) not null,
    m_description varchar(200),
    m_duration varchar(15) not null,
    m_clasification varchar(10) not null,
    primary key(id_movie)
)engine=innoDB;

create table if not exists halls(
	id_hall int not null,
    h_name varchar(35) not null,
    h_total_seats varchar(3),
    primary key(id_hall)
)engine=innoDB;

create table if not exists schedules(
	id_schedule int not null,
	id_movie int not null,
    id_hall int,
    s_showtime varchar(5) not null,
    primary key(id_schedule),
    constraint fkmovie_schedule foreign key (id_movie) references movies(id_movie),
    constraint fkhall_schedule foreign key (id_hall) references halls(id_hall)
    on delete cascade
    on update cascade
)engine=innoDB;

create table if not exists seats(
	id_seat varchar(4) not null,
    no_seat varchar(3) not null,
    s_state enum('free', 'occupied') not null,
    id_hall int,
    primary key(id_seat),
    constraint fkseat_hall foreign key (id_hall) references halls(id_hall)
    on delete cascade
    on update cascade
)engine=innoDB;

create table if not exists type_tickets(
    tt_name varchar(10) not null,
    tt_price varchar(5) not null,
    primary key(tt_name)
)engine=innoDB;

create table if not exists tickets(
	id_ticket int not null auto_increment,
    id_movie int,
    id_hall int,
    id_user int,
    t_date date not null,
    id_seat varchar(4),
    tt_name varchar(10),
	primary key(id_ticket),
    constraint fkmovie_ticket foreign key (id_movie) references movies(id_movie),
    constraint fkhall_ticket foreign key (id_hall) references halls(id_hall),
    constraint fkuser_ticket foreign key (id_user) references users(id_user),
    constraint fktotal_ticket foreign key (id_seat) references seats(id_seat),
    constraint fktt_ticket foreign key (tt_name) references type_tickets(tt_name)
    on delete cascade
    on update cascade
)engine=innoDB;

create table if not exists administrators(
	id_admin int not null auto_increment,
    a_name varchar(35) not null,
    a_sname1 varchar(35) not null,
    a_sname2 varchar(35),
    a_phone varchar(10) not null,
    a_email varchar(80) not null,
    a_charge varchar(35) not null,
    primary key(id_admin)
)engine=innoDB;