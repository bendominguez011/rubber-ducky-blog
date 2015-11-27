# rubber-ducky-blog
This is a blogging application made with Python and the Flask web framework. The application consists of a core module, app.py, that contains both the views and the models for the application. There is also another module called parser.py, that I wrote to automate the process of writing html code for all of the code snippets I include in a post. The parser finds python code, parses it by assigning a word to it's "type", for example, keywords, built in functions, exceptions, etc., and then wraps the word with a div tag with an id equal to the type. There is then a respective css file for styling the div. There may have been more convenient options for the parser instead of writing it myself, but I wanted to be able to control the styling completely.

Note that the "clobbered" contributions page full of contributions titled "update" is due to me testing out a repository known as greenhat, a repository I recently started a fork of.

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
