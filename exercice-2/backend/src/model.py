from db import get_connection

class User:
    def __init__(self, id=None, username=None, password=None):
        self.id = id
        self.username = username
        self.password = password

    def get_all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        conn.close()
        return [User(id=row["id"], username=row["username"], password=row["password"]) for row in rows]

    def create(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        return User(id=user_id, username=username, password=password)
    
    def get_user_details(user_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id=?", (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(id=row["id"], username=row["username"], password=row["password"])
        return None
    
    def update(self, username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET username=?, password=? WHERE id=?", (username, password, self.id))
        conn.commit()
        conn.close()
        self.username = username
        self.password = password

    def delete(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id=?", (self.id,))
        conn.commit()
        conn.close()