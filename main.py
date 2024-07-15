import pandas as pd
import numpy as np
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)   # create a Flask app

stations = pd.read_csv("data/stations.txt", skiprows=17)
# clear up columns not needed in station view
stations["Station ID"] = stations[["STAID"]]
stations["Station Name"] = stations[[
    "STANAME                                 "]]
stations = stations[["Station ID", "Station Name"]]


@app.route("/")
def Home():
    return render_template("home.html", data=stations.to_html(justify="center", index=False))


@app.route("/api/v1/<station>/<date>")
def get_temp_by_station_and_date(station, date):
    station_path = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(station_path, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == str(date)]['   TG'].squeeze() / 10

    return {"Station": station, "Date": date, "Temperature": temperature}


@app.route("/api/v1/<station>/")
def all_data(station):
    station_path = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(station_path, skiprows=20, parse_dates=["    DATE"])
    return df.to_dict(orient="records")

@app.route("/api/v1/yearly/<station>/<year>")
def all_data_by_year(station, year):
    station_path = "data/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(station_path, skiprows=20, parse_dates=["    DATE"])
    result = df.loc[df['    DATE'].dt.year == int(year)]
    
    return result.to_dict(orient="records")

if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)   # run the app on port 5000
