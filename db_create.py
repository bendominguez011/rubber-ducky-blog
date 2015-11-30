from app import db, Post

db.session.rollback()
db.create_all()
post = Post("Introduction to Flask Part 1", "parsed_flask.html")
db.session.add(post)
db.session.commit()
