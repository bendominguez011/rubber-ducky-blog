from app import db, Post

post = Post('Introduction to Flask', 'parsed_flask.html')
db.session.add(post)
db.session.commit()
