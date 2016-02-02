from flask import Flask
import jinja2
from flask import render_template, redirect, request, flash, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')


if os.environ.get('DATABASE_URL') is not None:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
app.secret_key = os.urandom(7)
WTF_CRSF_ENABLED = True
SECRET_KEY = os.urandom(7)
base = os.path.abspath(os.path.dirname(__file__))
whoosh_base = os.path.join(base, 'search.db')
posts_per_page = 10

from models import Post, SubmissionForm, SearchForm


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

@app.route('/recent')
def most_recent_post():
    post = Post.query.order_b
    y(Post.time_created)\
    .all().pop()
    return redirect(url_for('post', post_id=post.id))

@app.route('/about')
def about():
    return render_template('about.html')
