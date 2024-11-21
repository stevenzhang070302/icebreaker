# Flask Web server

from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from ice_breaker import ice_break_with

load_dotenv()

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process():
    name = request.form["name"]
    res, linkedin_pic_url = ice_break_with(name=name)

    print(res.to_dict())

    return jsonify(
        {
            "summary_and_facts": res.to_dict(),  # turn the summary object into a dictionary
            "picture_url": linkedin_pic_url,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
