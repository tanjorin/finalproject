from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        genre = request.form["genre"]
        return redirect(url_for("movies", gre=genre))
    else:
        return render_template("index.html")

@app.route("/<gre>")
def movies(gre):
    return f"<h1>{gre}</h1>"





if __name__ == "__main__":
    app.run(debug=True)
