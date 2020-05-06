import time

from extensions import db as db


class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    value1 = db.Column(db.String())
    value2 = db.Column(db.Float)
    value3 = db.Column(db.Boolean)
    creationDate = db.Column(db.Integer, nullable=False)
    timeStamp = db.Column(db.Integer, nullable=False)
    lastModificationDate = db.Column(db.Integer, nullable=False)

    def __init__(self, value1, value2, value3, timestamp):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.timeStamp = timestamp
        self.creationDate = int(time.time())
        self.lastModificationDate = int(time.time())

    def serialize(self):
        return {
            '_id': self.id,
            'timestamp': self.timeStamp,
            'value1': self.value1,
            'value2': self.value2,
            'value3': self.value3,
            'creationDate': self.creationDate,
            'lastModificationDate': self.lastModificationDate
        }
