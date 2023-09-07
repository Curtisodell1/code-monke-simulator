#If table doesn't exist create table
import sqlite3
# from studyCoding import topic_id
# from login import login
# user_id = login()

CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()
# Class Variable for the info we want.
class Topics_By_User:

    def __init__ (self, user_id, topic_id, id = None):
        self.user_id = user_id
        self.topic_id = topic_id
        self.id = id

    @classmethod
    def create_table(cls) :
        sql = '''
            CREATE TABLE IF NOT EXISTS topic_by_user (
                id INTEGER PRIMARY KEY,
                user_id INT,
                topic_id INT,
                note TEXT
            )
        '''
        CURSOR.execute(sql)

    @classmethod
    def add_to_table(cls, user_id, topic_id) :
        sql = 'INSERT INTO topic_by_user (user_id, topic_id) VALUES (?, ?)'
        CURSOR.execute(sql, (user_id, topic_id) )
        CONN.commit()

# Self.ID = user id global variable
# self.topic = topic currently being studied
# INSERT INTO using this info