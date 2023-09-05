import sqlite3

CONN = sqlite3.connect('./resources.db')
CURSOR = CONN.cursor()

class Resource: 
    def __init__(self, topic, synopsis, example, relevant_content, id=None):
        self.topic = topic
        self.synopsis = synopsis
        self.example = example
        self.relevant_content = relevant_content
        self.id = id

    @classmethod
    def create_table ( cls ) :
        sql = '''
            CREATE TABLE IF NOT EXISTS resources (
                id INTEGER PRIMARY KEY,
                topic TEXT,
                synopsis TEXT,
                example TEXT,
                relevant_content TEXT
            );
        '''
        CURSOR.execute( sql )