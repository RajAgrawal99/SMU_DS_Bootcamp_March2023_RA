# Import the dependencies.
# import datetime as dt
import numpy as np
import pandas as pd 
import json
# from sqlalchemy import create_engine, text, inspect
from flask import Flask, render_template, redirect, request, jsonify
from modelHelper import modelHelper
# from sqlHelper import SQLHelper


#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#################################################
# Database Setup
#################################################
# engine = create_engine("sqlite:///data/Map_data.sqlite")

# Route to render index.html template and other pages
@app.route("/")
def home():
    # Return template and data
    return render_template("index.html")
    

@app.route("/about_us")
def about_us():
    # Return template and data
    return render_template("about_us.html")

@app.route("/sampledata")
def sampledata():
    # Return template and data
    return render_template("sampledata.html")

@app.route("/tableau")
def tableau():
    # Return template and data
    return render_template("tableau.html")

@app.route("/tableau1")
def tableau1():
    # Return template and data
    return render_template("tableau_1.html")

@app.route("/datatable")
def datatable():
    # Return template and data
    return render_template("Data_table.html")

@app.route("/dashboard")
def plotly():
    # Return template and data
    return render_template("dashboard.html")


@app.route("/df1_profile")
def df_profile():
    # Return template and data
    return render_template("df1_profile.html")

@app.route("/resources")
def resources():
    # Return template and data
    return render_template("resources.html")
@app.route("/ml_form")
def ml():
    # Return template and data
    return render_template("ml_form.html")

@app.route("/makePredictions", methods=["POST"])
def predictions():
    content = request.json["data"]
    print(content)
    # return(jsonify({"ok": True}))# test the readin of the logic.js file
    
    # parse
    year = int(content["year"])
    age = int(content["age"])
    population = int(content["population"])
    sex = content["sex"]
    race = content["race"]
    month = content["month"]
    weekday = content["weekday"]
    season = content["season"]
    city = content["city"]
    state = content["state"]

    preds = modelHelper.makePredictions(year,age,population,sex,race,month,weekday,season,city,state)
    return(jsonify({"ok": True, "no_arrest": preds[0],"arrest": preds[1]}))
   
    

##########################################################################


# #######################################################################
# @app.route("/api/v1.0/dashboard_data/<show>")
# def dashboard_data(show):
#     """Get show"""
#     if show != "All":
#         query = text(f"""
#                     SELECT
#                         *
#                     FROM
#                         Map_data
#                     WHERE
#                     Show = "{show}";
#                 """)
#     else:
#         query = text(f"""
#             SELECT
#                 *
#             FROM
#                 Map_data;
#         """)

#     df = pd.read_sql(query, engine)
    
#     df2 = df.Season.value_counts().reset_index()
#     df2.columns = ["season", "counts"]

#     df3 = df.Region.value_counts().reset_index()
#     df3.columns = ["region", "counts"]

#     data = json.loads(df.to_json(orient="records"))
#     data2 = json.loads(df2.to_json(orient="records"))
#     data3 = json.loads(df3.to_json(orient="records"))

#     return({"raw_data": data, "seasons": data2, "regions": data3})
    
##########################################################################

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

#main
if __name__ == "__main__":
    app.run(debug=True)
