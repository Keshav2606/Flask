from flask import Flask, request, jsonify;
from flask_pymongo import PyMongo;
from bson.objectid import ObjectId
import os;

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)

@app.route("/driver/<string:id>", methods=["GET"])
def home(id):
    try:
        driver = mongo.db.drivers.find_one({"_id": ObjectId(id)})

        if not driver:
            return jsonify({"message": "No data found"}), 404
        
        driver["_id"] = str(driver["_id"])

        return jsonify(driver), 200
    except:
        return jsonify({"message: Internal Server error"}), 500


if __name__ == "__main__":
    app.run(debug=True)