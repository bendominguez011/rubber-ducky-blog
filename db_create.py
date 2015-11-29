from app import db, Post

db.session.add(Post('Introduction to Flask', 'parsed_flask.html'))
db.session.commit()
