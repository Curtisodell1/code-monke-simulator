study_loop = True
study_coding_points = 0 
import sqlite3
CONN = sqlite3.connect('resources.sql')
CURSOR = CONN.cursor()

class topics:
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
        return topics.show_topics(resources)
    
    @classmethod
    def show_topics(cls, records):
        return [topics.show_topic(record) for record in records]

    @classmethod
    def show_topic(cls, record):
        return f"id: {record[0]},topic:{record[1]} |"
    

    @classmethod    
    def select_topic(cls):
        sql = f'SELECT * FROM resources WHERE id = {topic_id}'
        topic = CURSOR.execute(sql).fetchone()
        return topics.show_selected_topic(topic)
    
    @classmethod
    def show_selected_topic(cls, record):
        return f'''
            id: {record[0]}
            topic: {record[1]}
            synopsis: {record[2]}
            example: {record[3]}
            external_links: {record[4]}
        '''

while(study_loop):
    print("How will you study?:")
    # these options will be replaced by a SQL database of topics to study
    # users can either query the database to choose a topic or get something new
    print("1. Study Option 1")
    print("2. Choose to learn about a topic")
    print("x. Return to main menu")
    command = input("Input your command here:")
    if command == "1":
        #print list of things to study
        print(topics.get_topics())
    elif command == "2":
        topic_id = input("Select the study topic by ID:")
        print(topics.select_topic())
        study_coding_points += 1
        print(f"Your coding points have increased you now have: {study_coding_points}")    
    elif command == "x":
        study_loop = False
    else:
        print("your input is not recognized")



