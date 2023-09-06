import sqlite3

CONN = sqlite3.connect('./users.db')
CURSOR = CONN.cursor()

class User:
    
    all = []

    def __init__(self, username, password, id=None):
        self.username = username
        self.password = password
        self.id = id
    
    def __repr__(self):
        return f'(Username: {self.username}), (Password: {self.password})'

    def save(self):
        sql = """
            INSERT INTO users (username, password)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.username, self.password))
        CONN.commit()
        self.id = CURSOR.lastrowid

    @classmethod
    def create_table ( cls ) :
        sql = '''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT,
                password TEXT
                );
        '''
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def create(cls, username, password):
        user = cls(username, password)
        user.save()
        return user
