from flask import Flask
import jinja2
from flask import render_template, redirect, request, flash, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
from datetime import datetime
import os

search_enabled = os.environ.get('HEROKU') is None
if search_enabled:
    import flask.ext.whooshalchemy as whoosh

app = Flask(__name__)
#SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
app.secret_key = os.urandom(7)
WTF_CRSF_ENABLED = True
SECRET_KEY = os.urandom(7)
base = os.path.abspath(os.path.dirname(__file__))
whoosh_base = os.path.join(base, 'search.db')
posts_per_page = 10

class SubmissionForm(Form):
    submission = StringField('submission', widget=TextArea(), validators=[DataRequired()])

class SearchForm(Form):
    query = StringField('query', validators=[DataRequired()])

class Post(db.Model):
    __searchable__ = ['title']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    filename = db.Column(db.String())
    time_created = db.Column(db.DateTime)

    def __init__(self, title, filename):
        self.title = title
        self.filename = filename
        self.time_created = datetime.utcnow()

    def __repr__(self):
        return "<Title %r>" % self.title

if search_enabled:
    whoosh.whoosh_index(app, Post)

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submission = db.Column(db.String(140))

    def __init__(self, submission):
        self.submission = submission

    def __repr__(self):
        return "<Submission %r>" % self.submission

@app.before_request
def before_request():
    g.post = Post.query.order_by("time_created").first()
    g.search_form = SearchForm()

@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    posts = Post.query.all()
    posts = Post.query.paginate(page, posts_per_page, False)
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get(post_id)
    template = post.filename
    return render_template(template, post=post)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = SubmissionForm()
    if form.validate_on_submit():
        submission = Submission(submission=request.form['submission'])
        db.session.add(submission)
        db.session.commit()
        flash("Request submitted!")
        return redirect(url_for('index'))
    return render_template('submission.html', form=form)

@app.route('/search', methods=['GET', 'POST'])
def search():
    if not g.search_form.validate_on_submit():
        flash("no query")
        return redirect(url_for('index'))
    query = request.form['query']
    results = Post.query.whoosh_search(query)
    if results.count() == 0:
        flash('no results came up for "{0}"'.format(query))
        return redirect(url_for('index'))
    return render_template('search_results.html', query=query, results=results)

@app.route('/post/<int:post_id>')
def most_recent_post(post_id):
    post = Post.query.order_by(Post.time_created).first()
    template = post.filename
    return render_template(template, post=post)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
