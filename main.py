from flask import Flask, request, jsonify, render_template

app = Flask(__name__)   # create a Flask app

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def GetTempStationByDate(station, date):
    temperature = 92
    return {"Station": station, "Date": date, "Temperature": temperature}

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)   # run the app on port 5000