from core.app import db, Post

db.drop_all()
db.session.rollback()
db.create_all()
post = Post("Introduction to Flask Part 1", "parsed_flask.html")
db.session.add(post)
db.session.commit()

post2 = Post("Intro to Flask Part 2 -- SQLAlchemy", "parsed_flask2.html")
db.session.add(post2)
db.session.commit()

post3 = Post("Dabbling in JavaScript", "intro_to_javascript.html")
db.session.add(post3)
db.session.commit()

""" Need to put in individual timestamps for each
individual post, try to see if most recent post
works then. I think the timestamp isnt working
and marking all posts as occuring at the same time,
for some reason."""
