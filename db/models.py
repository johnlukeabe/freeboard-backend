# Common
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class database:
    @staticmethod
    def init(app):
        db.init_app(app)

    @staticmethod
    def get_db():
        return db

class User(db.Model):
    __tablename__ = 'user_list'
    
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    email = db.Column('email', db.String)

    @property
    def serialize(self):
        return {
                'id': str(self.id).strip(),
                'name': str(self.name).strip(),
                'email': str(self.email).strip()
               }

