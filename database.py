import sqlite3

databaseName = "chats.db"


def createDB():
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        message_id INTEGER PRIMARY KEY AUTOINCREMENT,
        text TEXT,
        sender TEXT,
        recipient TEXT,
        time TEXT,
        readCount INTEGER DEFAULT 0
    )
    """)

    
    conn.commit()
    conn.close()



def insert_message(text, sender, recipient, time, readCount):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO messages (text, sender, recipient, time, readCount)
        VALUES (?, ?, ?, ?, ?)
    """, (text, sender, recipient, time, readCount))

    conn.commit()
    conn.close() # we close the connection to the database if it isnt being used

def getMessages(recipient):
    conn = sqlite3.connect(databaseName)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM messages WHERE recipient = ?", (recipient,))
    messages = cursor.fetchAll()

    cursor.execute("""
            UPDATE messages 
            SET read_count = read_count + 1 
            WHERE recipient = ?
        """, (recipient))

    conn.commit()
    conn.close()
    return messages
