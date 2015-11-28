from app import db, Post

post = Post.query.get(1)
db.session.remove(post)
db.session.commit()
post = Post('Introduction to Flask', 'parsed_flask.html')
db.session.add(post)
db.session.commit()
