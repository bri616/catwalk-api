from app import db
from sqlalchemy.dialects.postgresql import JSON


class CatSighting(db.Model):
    __tablename__ = 'catsightings'

    id = db.Column(db.Integer, primary_key=True)
    photo_url = db.Column(db.String())
    location = db.Column(JSON)

    def __init__(self, photo_url, location):
        self.photo_url = photo_url
        self.location = location

    def __repr__(self):
        return '<location {}>'.format(self.location)
