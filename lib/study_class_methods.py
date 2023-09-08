import sqlite3
CONN = sqlite3.connect('resources.db')
CURSOR = CONN.cursor()

class Resources:
    def __init__ (self, topic, synopsis, example, relevant_content, id=None):
        self.topic = topic
        self.synopsis = synopsis
        self.example = example
        self.relevant_content = relevant_content
        self.id = id

    # Pull a list of topics
    @classmethod    
    def get_topics(cls):
        sql = 'SELECT * FROM resources'
        resources = CURSOR.execute(sql).fetchall()
        return Resources.show_topics(resources)
    
    @classmethod
    def show_topics(cls, records):
        return [Resources.show_topic(record) for record in records]

    @classmethod
    def show_topic(cls, record):
        return f"{record[0]}. {record[1]}"

#Selects a specific task based on user input
    @classmethod    
    def select_topic(cls, topic_id):
        sql = f'SELECT * FROM resources WHERE id = {topic_id}'
        topic = CURSOR.execute(sql).fetchone()
        if topic:
            return Resources.show_selected_topic(topic)
        else:
            raise Exception("You've entered a topic which does not exist.")
    
    @classmethod
    def show_selected_topic(cls, record):
        return f'''
            id: {record[0]}
            topic: {record[1]}
            synopsis: {record[2]}
            example: {record[3]}
            external_links: {record[4]}
        '''