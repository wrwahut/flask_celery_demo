from backend.app import flask_app
from flask import jsonify
from celery_worker import handle

@flask_app.route("/index", methods=["POST", "GET"])
def index():
    handle.delay()
    return jsonify({"re": "200", "msg": "success", "data": {}})

if __name__ == "__main__":
    flask_app.run(host="localhost", port=9000)