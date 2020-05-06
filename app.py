import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from extensions import db
from models import Data

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

from models import Data


@app.route("/")
def hello():
    print("Hello WORLD")
    return "Hello World!"


@app.route("/api/create", methods=['POST'])
def add_book():
    print(request.json.get("value1"))
    try:
        data = Data(
            value1=request.json.get("value1"),
            value2=request.json.get("value2"),
            value3=request.json.get("value3"),
            timeStamp=request.json.get("timeStamp")
        )
        db.session.add(data)
        db.session.commit()
        return "Data added. data id={}".format(data.id)
    except Exception as e:
        return (str(e))


@app.route("/api/list")
def get_all():
    try:
        data = Data.query.all()
        return jsonify([e.serialize() for e in data])
    except Exception as e:
        return (str(e))


@app.route("/read/<id_>")
def get_by_id(id_):
    try:
        book = Book.query.filter_by(id=id_).first()
        return jsonify(book.serialize())
    except Exception as e:
        return (str(e))


if __name__ == '__main__':
    app.run()
