
from datetime import datetime
from extensions import db as db

class Data(db.Model):
    __tablename__ = 'data'

    id = db.Column(db.Integer, primary_key=True)
    value1 = db.Column(db.String())
    value2 = db.Column(db.Float)
    value3 = db.Column(db.Boolean)
    creationDate = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)
    timeStamp = db.Column(db.DateTime, nullable=False)
    lastModificationDate = db.Column(db.DateTime, nullable=False)

    def __init__(self, value1, value2, value3,timeStamp):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.timeStamp = timeStamp
        self.creationDate = datetime.utcnow()
        self.lastModificationDate = datetime.utcnow()

    def serialize(self):
        return {
            '_id': self.id,
            'timestamp': self.timeStamp,
            'value1':self.value1,
            'value2': self.value2,
            'value3': self.value3,
            'creationDate': self.creationDate,
            'lastModificationDate': self.lastModificationDate
        }