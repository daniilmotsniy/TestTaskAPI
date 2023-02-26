"""
this module contains main web framework setup
"""


import os

from flask import Flask
from domain import db
from api.analytics import analytics_blueprint

basedir = os.path.abspath(
    os.path.dirname(__file__)
).split('/gateway')[0] + '/dump'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    basedir,
    'database.db',
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(analytics_blueprint)

db.init_app(app)

with app.app_context():
    db.create_all()
