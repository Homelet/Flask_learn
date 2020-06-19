import json

from flask import Blueprint, Flask, jsonify, make_response, render_template, \
    request

app = Flask(__name__)

index_page = Blueprint("Index", __name__)


@index_page.route("get")
def get():
    var_a = request.values.get("a", "")
    return f"request {request.method}, var_a {var_a}"


@index_page.route("post", methods=["POST"])
def post():
    var_a = request.values.get("a", "")
    var_a_get = request.args.get("a", "")
    var_a_post = request.form.get("a", "")
    return f"request {request.method}, " \
           f"a {var_a}, a_get {var_a_get}, a_post {var_a_post}"


@index_page.route("upload", methods=["POST"])
def upload():
    f = request.files.get("file", "")
    return f"request {request.method}, files {request.files}, file {f}"


@index_page.route("text")
def text():
    response = make_response("Index_page", 200)
    return response


@index_page.route("json")
def json_():
    data = {"a": "b"}
    response = make_response(json.dumps(data))
    response.headers["Content-Type"] = "application/json"
    return response


@index_page.route("jsonify")
def json_jsonify():
    data = {"a": "Hello"}
    response = make_response(jsonify(data))
    return response


@index_page.route("template")
def template():
    user = {"nickname": "HomeletW", "email": "homeletwei@gmail.com"}
    context = {
        "name": "Homelet",
        "user": user,
        "num_list": [i for i in range(20)],
    }
    return render_template("index.html", **context)


@index_page.route("extend_template")
def inherit_template():
    return render_template("extend_template.html")


app.register_blueprint(index_page, url_prefix="/")

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
