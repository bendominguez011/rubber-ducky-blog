# rubber-ducky-blog

#included extensions
* [Flask-SQLAlchemy](https://pythonhosted.org/Flask-SQLAlchemy/) -- SQLAlchemy toolkit with built in ORM layer
* [Flask-WhooshAlchemy](https://github.com/gyllstromk/Flask-WhooshAlchemy) -- searching posts

#getting started..
clone the repository..
```
$ mkdir blog
$ git clone https://github.com/bendominguez011/rubber-ducky-blog
$ pip install virtualenv
$ virtualenv flask
```
install the appropriate extensions listed above..
```
$ flask/bin/pip install flask-sqlalchemy
$ flask/bin/pip install flask-whooshalchemy
```
to run the devolepment server, run the app.py script
```
$ flask/bin/python app.py
>* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
>* Restarting with stat
```
