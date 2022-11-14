import json
import sys
from unicodedata import category
from flask import jsonify
from flask import current_app as app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from sqlalchemy.inspection import inspect

db = SQLAlchemy()

# Dummy table to show the model standard
class Dummy(db.Model):
    __tablename__ = 'dummy'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True, index=True)
    description = db.Column(db.String(64), unique=True, index=True)

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.id = self.add()

    def __repr__(self):
        return self.id

    def add(self):
        app.logger.info('Adding new Dummy record: %s', self.name)
        _id = None
        db.session.add(self)
        try:
            db.session.commit()
            app.logger.info('Dummy Record Added: %s', self.name)
        except IntegrityError:
            app.logger.error('New dummy record addition failed: %s', self.name)
            db.session.rollback()

        if self.id is None:
            _resp = Dummy.query.with_entities(Dummy.id).filter(Dummy.name == self.name).first()
            _id = _resp["id"]
        else:
            _id = self.id

        return _id

    @staticmethod
    def get():
        result = db.session.query(Dummy).all()
        return result





