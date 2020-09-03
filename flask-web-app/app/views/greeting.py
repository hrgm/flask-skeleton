from flask import Blueprint, render_template, request

greeting = Blueprint("greeting", __name__, template_folder="templates")


@greeting.route("/", methods=("GET", "POST"))
@greeting.route("/<string:greeting>", methods=("GET", "POST"))
def greeting_user(greeting="Hello"):
    if request.method == "POST":
        user_name = request.form["user_name"]
    else:
        user_name = request.args.get("user_name", "")

    return render_template(
        "greeting/greeting.html", greeting=greeting, user_name=user_name
    )
