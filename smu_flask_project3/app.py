from flask import Flask, render_template, redirect
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text
import json

# Create an instance of Flask
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///data/wildfires.sqlite")


# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")


@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")


@app.route("/plots")
def plots():
    # Return template and data
    return render_template("plots.html")

@app.route("/resources")
def resources():
    # Return template and data
    return render_template("resources.html")


##########################################################################

@app.route("/api/v1.0/<min_size>/<max_size>/<state>")
def wildfire_start_end(min_size, max_size, state):
    """Get stations"""
    query = text(f"""
                SELECT
                    *
                FROM
                    wildfires
                WHERE
                    fire_size >= {min_size}
                    AND fire_size <= {max_size}
                    AND state = {state};
            """)

    df = pd.read_sql(query, engine)
    df = df.sort_values(by=['fire_size'], ascending=False)
    df2 = df.discovery_month.value_counts().reset_index()
    df2.columns = ["month", "counts"]

    data = json.loads(df.to_json(orient="records"))
    data2 = json.loads(df2.to_json(orient="records"))

    return {"raw_data": data, 'month_data': data2}


#############################################################

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r


# main
if __name__ == "__main__":
    app.run(debug=True)
