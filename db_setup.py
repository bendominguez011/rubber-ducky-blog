from app import db, Post

db.drop_all()
db.session.rollback()
db.create_all()
post = Post("Introduction to Flask Part 1", "parsed_flask.html")
post2 = Post("Intro to Flask Part 2 -- SQLAlchemy", "parsed_flask2.html")
post3 = Post("Dabbling with JavaScript", "intro_to_javascript.html")
db.session.add_all([post, post2, post3])
db.session.commit()
