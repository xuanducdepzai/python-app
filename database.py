import sqlite3

def dict_factory(cursor,row):
    d =  {}
    for idx,col in enumerate ( cursor.description):
            d[col[0]] =row [idx]
            return d
    
def connect_db():
    conn = sqlite3.connect('data/database.db')
    conn.row_factory = dict_factory
    return conn

def create_user(name,email,password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name,email,password) VALUES (?,?,?)",(name,email,password))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users where id = ?", (id,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email(email):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?",(email,))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_by_email_and_password(email, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

# create_user("jon","hell","lala")
print(get_user_by_id(2))
print(get_user_by_email("hell"))