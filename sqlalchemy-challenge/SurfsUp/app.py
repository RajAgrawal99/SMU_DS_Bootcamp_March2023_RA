# Import the dependencies.
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
from flask import Flask, jsonify
import json

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"""<h1>Available Routes:</h1><br/>
        <a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a><br/>
        <a href="/api/v1.0/stations">/api/v1.0/stations</a><br/>
        <a href="/api/v1.0/tobs">/api/v1.0/tobs</a><br/>
        <a href="/api/v1.0/2016-08-23">/api/v1.0/2016-08-23</a><br/>
        <a href="/api/v1.0/2016-08-23/2016-09-23">/api/v1.0/2016-08-23/2016-09-23</a><br/>"""
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Get Precipitation"""
    query = text("""
                SELECT
                    date,
                    station,
                    prcp
                FROM
                    measurement
                WHERE
                    date >= '2016-08-23';
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/stations")
def stations():
    """Get stations"""
    query = text("""
                SELECT
                    station,
                    count(*) as num_obs
                FROM
                    measurement
                group by
                    station
                order by
                    num_obs desc;
            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/tobs")
def temperature():
    """Get stations"""
    query = text("""
                SELECT
                    station,
                    date,
                    tobs as temperature
                FROM
                    measurement
                WHERE
                    station = 'USC00519281'
                    and date >= '2016-08-23'
                order by
                    date asc;

            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/<start>")
def temperature_start(start):
    """Get stations"""
    query = text(f"""
                SELECT
                    station,
                    min(tobs) as tmin,
                    avg(tobs) as tmean,
                    max(tobs) as tmax
                FROM
                    measurement
                WHERE
                    date >= '{start}';

            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

@app.route("/api/v1.0/<start>/<end>")
def temperature_start_end(start, end):
    """Get stations"""
    query = text(f"""
                SELECT
                    station,
                    min(tobs) as tmin,
                    avg(tobs) as tmean,
                    max(tobs) as tmax
                FROM
                    measurement
                WHERE
                    date >= '{start}'
                    and date <= '{end}';

            """)

    df = pd.read_sql(query, engine)
    data = json.loads(df.to_json(orient="records"))
    return(data)

# run the website
if __name__ == '__main__':
    app.run(debug=True)
