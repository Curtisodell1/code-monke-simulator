import sqlite3

CONN = sqlite3.connect('../users.db')
CURSOR = CONN.cursor()

class User:
    
    all = []

    def __init__(self, username, password, id=None):
        self.username = username
        self.password = password
        self.id = id
        User.all.append(self)
    
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
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS users
        """
        CURSOR.execute(sql)
        CONN.commit()

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
        print(user)

    @classmethod
    def new_from_db(cls, row):
        user = cls(username=row[1], password=row[2], id=row[0])
        return user
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM users
        """
        return [cls.new_from_db(row) for row in CURSOR.execute(sql).fetchall()]

    @classmethod
    def find_by_username(cls, username):
        sql = """
            SELECT * FROM users
            WHERE username = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (username,)).fetchone()
        if not row:
            return None
        return User(username=row[1], password=row[2], id=row[0])
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM users
            WHERE id = ?
            LIMIT 1
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        if not row:
            return None
        return User(username=row[1], password=row[2], id=row[0])
