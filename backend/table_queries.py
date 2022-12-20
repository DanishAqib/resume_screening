users_table = """
    create table if not exists users
    (
        u_id uuid not null primary key,
        u_name varchar(50) not null,
        u_email varchar(50) not null,
        u_password varchar(50) not null,
        u_created_at timestamp default current_timestamp
    )"""