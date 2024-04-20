from mysql import connector

connection = connector.connect(
    host="localhost",
    user="root",
    password="YOUR PASSWORD", #პაროლი
    database="it_step34"
)

cursor = connection.cursor()

create_user_table = """
CREATE TABLE IF NOT EXISTS user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL
)
"""

create_profile_table = """
CREATE TABLE IF NOT EXISTS profile (
    id INT PRIMARY KEY AUTO_INCREMENT,
    bio VARCHAR(200),
    profile_picture VARCHAR(200),
    user_id INT UNIQUE,
    FOREIGN KEY (user_id) REFERENCES user(id)
)
"""

cursor.execute(create_user_table)
cursor.execute(create_profile_table)

user_data = [
    ("Alice", "alice@example.com"),
    ("Bob", "bob@example.com"),
    ("Charlie", "charlie@example.com"),
    ("David", "david@example.com"),
    ("Eve", "eve@example.com")
]

insert_user_query = "INSERT INTO user (username, email) VALUES (%s, %s)"
cursor.executemany(insert_user_query, user_data)

cursor.execute("SELECT LAST_INSERT_ID()")
last_inserted_id_row = cursor.fetchone()
last_inserted_id = last_inserted_id_row[0] if last_inserted_id_row else None

profile_data = [
    ("Alice's bio", "alice_profile_picture.jpg", last_inserted_id),
    ("Bob's bio", "bob_profile_picture.jpg", last_inserted_id + 1),
    ("Charlie's bio", "charlie_profile_picture.jpg", last_inserted_id + 2),
    ("David's bio", "david_profile_picture.jpg", last_inserted_id + 3),
    ("Eve's bio", "eve_profile_picture.jpg", last_inserted_id + 4)
]

insert_profile_query = "INSERT INTO profile (bio, profile_picture, user_id) VALUES (%s, %s, %s)"
cursor.executemany(insert_profile_query, profile_data)

connection.commit()

cursor.close()