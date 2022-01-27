from http import HTTPStatus
from flask import Blueprint, request, jsonify
from backend.utils.api_checker import api_checker
from backend.utils.util import validateJSON
from backend.utils.validate_payload import validate_json
from database.mongo import MongoDatabase
from utils.constants import url_local

dbTest = Blueprint("dbTest", __name__, url_prefix="/dbTest")


@dbTest.route('/', methods=["OPTIONS", "GET"])
@api_checker
def home():
    return jsonify({
        "status": HTTPStatus.OK,
        "message": "home of dbTest"
    })


@dbTest.route("/insert", methods=["OPTIONS", "POST"], strict_slashes=False)
@api_checker
@validate_json
def insert():
    if request.method == 'GET':
        return jsonify({"Response": 405, "Data": "please use POST methods"})
    else:
        try:
            if validateJSON(request.get_data()):
                data = request.get_json()
                db_url = url_local
                db_name = data['db_name']
                collection_name = data['collection_name']
                query = data['query']

                result = MongoDatabase(db_url, db_name, collection_name).insert_one(query)

            return jsonify({
                "status": HTTPStatus.OK,
                "data": "Record Uploaded"
            })
        except Exception as e:
            return jsonify({
                "status": HTTPStatus.OK,
                "data": "Please check the data. Something missing !!",
                "error": e
            })
