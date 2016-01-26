from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea
import os, datetime

from app import db
from app import app

search_enabled = os.environ.get('HEROKU') is None
if search_enabled:
    import flask.ext.whooshalchemy as whoosh

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
        self.time_created = datetime.datetime.utcnow()

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
