from task34_1 import User, Profile, engine
from sqlalchemy.orm import sessionmaker

engine = engine
Session = sessionmaker(bind=engine)
session = Session()

user_data = [
    User(user_name='alice', email='alice@example.com'),
    User(user_name='bob', email='bob@example.com'),
    User(user_name='charlie', email='charlie@example.com'),
    User(user_name='david', email='david@example.com'),
    User(user_name='eve', email='eve@example.com')
]
session.add_all(user_data)
session.commit()

profile_data = [
    Profile(user_name='alice', bio="Alice's bio", profile_picture="alice_profile_picture.jpg"),
    Profile(user_name='bob', bio="Bob's bio", profile_picture="bob_profile_picture.jpg"),
    Profile(user_name='charlie', bio="Charlie's bio", profile_picture="charlie_profile_picture.jpg"),
    Profile(user_name='david', bio="David's bio", profile_picture="david_profile_picture.jpg"),
    Profile(user_name='eve', bio="Eve's bio", profile_picture="eve_profile_picture.jpg")
]
session.add_all(profile_data)
session.commit()

# Close session
session.close()