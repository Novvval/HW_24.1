import os
from typing import Optional, Any

from flask import Flask, request, abort, Response
from utils import query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")


@app.route("/perform_query", methods=["POST"])
def perform_query() -> Response:
    cmd1: Optional[str] = request.args.get("cmd1")
    value1: Optional[str] = request.args.get("value1")
    file_name: Any = request.args.get("file_name")
    cmd2: Optional[str] = request.args.get("cmd2")
    value2: Optional[str] = request.args.get("value2")
    if not (cmd1, value1, file_name):
        abort(400)

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        abort(400)

    with open(file_path) as file:
        result = query(cmd1, value1, file)
        if cmd2 and value2:
            result = query(cmd2, value2, result)
        result = "\n".join(result)

    return app.response_class(result, content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
