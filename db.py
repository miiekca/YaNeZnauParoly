import sqlite3 as sql

def post_count():
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = "SELECT COUNT(id) FROM posts"
    c = cursor.execute(query)
    count_post = c.fetchone()[0]

    connect.close()

    return count_post

def select_post(id):
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = f"SELECT data FROM posts WHERE posts.id = {id}"
    c = cursor.execute(query)
    post = c.fetchone()[0]

    connect.close()

    return post

def insert_post(year, month, post):
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = """INSERT INTO posts (year, month, data) VALUES(?, ?, ?)"""
    cursor.execute(query, (year, month, post,))
    connect.commit()

    connect.close()
    return 0

def create_secure_table():
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = f"""CREATE TABLE IF NOT EXISTS secure_class(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class STRING,
            UNIQUE (id)
            )"""
    cursor.execute(query)
    connect.commit()

    connect.close()
    return 0

def create_health_table():
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = f"""CREATE TABLE IF NOT EXISTS health_class(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            class STRING,
            UNIQUE (id)
            )"""
    cursor.execute(query)
    connect.commit()

    connect.close()
    return 0

def create_posts_table():
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = """CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                year INTEGER NOT NULL,
                month INTEGER NOT NULL, 
                data TEXT,
                label STRING,
                secure_id INTEGER,
                health_id INTEGER,
                UNIQUE(id)
                FOREIGN KEY(secure_id) REFERENCES secure_class(id)
                FOREIGN KEY(health_id) REFERENCES health_class(id)
                )"""
    cursor.execute(query)
    
    cursor.execute(query)
    connect.commit()

    connect.close()
    return 0

def insert_label(label, id):
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = f"""UPDATE posts SET label = '{label}' WHERE posts.id = {id}"""
    cursor.execute(query)
    connect.commit()

    connect.close()
    return 0

def select_label(post_id):
    connect = sql.connect("my_data.sqlite")
    cursor = connect.cursor()

    query = f"SELECT label FROM posts WHERE posts.id = {post_id}"
    c = cursor.execute(query)
    label = c.fetchone()

    connect.close()

    return label
