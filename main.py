import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)   # create a Flask app

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>")
def GetTempStationByDate(station, date):
    station_path = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(station_path, skiprows=20, parse_dates=["    DATE"])    
    temperature = df.loc[df['    DATE'] ==  str(date)] ['   TG'].squeeze() /10
    
    return {"Station": station, "Date": date, "Temperature": temperature}

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)   # run the app on port 5000