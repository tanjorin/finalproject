from flask import Flask, redirect, url_for, render_template, request


app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        genre = request.form["genre"]
        year = request.form["year"]
        if genre == "Action" and year == "1990's":
            return render_template("MovieFile.html")

        elif genre == "Action" and year == "2000's":
            return render_template("Action_2000.html")

        elif genre == "Action" and year == "2010's":
            return render_template("Action_2010.html")

        elif genre == "Comedy" and year == "1990's":
            return render_template("Comedy_1990.html")

        elif genre == "Comedy" and year == "2000's":
            return render_template("Comedy_2000.html")

        elif genre == "Comedy" and year == "2010's":
            return render_template("Comedy_2010.html")

        elif genre == "Romance" and year == "1990's":
            return render_template("Romance_1990.html")

        elif genre == "Romance" and year == "2000's":
            return render_template("Romance_2000.html")

        elif genre == "Romance" and year == "2010's":
            return render_template("Romance_2010.html")

        elif genre == "Horror" and year == "1990's":
            return render_template("Horror_1990.html")

        elif genre == "Horror" and year == "2000's":
            return render_template("Horror_2000.html")

        elif genre == "Horror" and year == "2010's":
            return render_template("Horror_2010.html")

        elif genre == "Drama" and year == "1990's":
            return render_template("Drama_1990.html")

        elif genre == "Drama" and year == "2000's":
            return render_template("Drama_2000.html")

        elif genre == "Drama" and year == "2010's":
            return render_template("Drama_2010.html")
        
    else:
        return render_template("index.html")

#@app.route("/<gre>")
#def movies(gre):
    #return render_template("index.html")





if __name__ == "__main__":
    app.run(debug=True)
