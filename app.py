import os
import time

from flask import Flask, request, jsonify
from extensions import db
from models import Data

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

#Default endpoint for testing
@app.route("/")
def test():
    return "Matt's TagUp Challenge"

#Create endpoint to create new record
@app.route("/api/create", methods=['POST'])
def add_book():
    print(request.json.get("value1"))
    try:
        data = Data(
            value1=request.json.get("value1"),
            value2=request.json.get("value2"),
            value3=request.json.get("value3"),
            timestamp=request.json.get("timeStamp")
        )
        db.session.add(data)
        db.session.commit()
        return "Data added. data id={}".format(data.id)
    except Exception as e:
        return str(e)

#List endpoint that returns all records
@app.route("/api/list")
def get_list():
    try:
        data = Data.query.all()
        return jsonify([e.serialize() for e in data])
    except Exception as e:
        return str(e)

#Read endpoint that returns specific record by id
@app.route("/api/read/<id_>")
def get_by_id(id_):
    try:
        data = Data.query.filter_by(id=id_).first_or_404()
        return jsonify(data.serialize())
    except Exception as e:
        return str(e)

#Delete endpoint that deletes specific record by id
@app.route("/api/delete/<id_>")
def delete_by_id(id_):
    try:
        Data.query.filter_by(id=id_).delete()
        db.session.commit()
        return "Data with id = {} deleted.".format(id_)
    except Exception as e:
        return str(e)

#Modify endpoint that modifies specific record by id
@app.route("/api/modify/<id_>", methods=['POST'])
def modify_by_id(id_):
    try:
        data = Data.query.filter_by(id=id_).first_or_404()
        data.value1 = request.json.get("value1"),
        data.value2 = request.json.get("value2"),
        data.timeStamp = request.json.get("timeStamp")
        if bool(request.json.get("value3")):
            data.value3 = True
        else:
            data.value3 = False
        data.lastModificationDate = int(time.time())
        db.session.commit()
        return "Data with id = {} updated.".format(id_)
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run()
