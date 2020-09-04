from flask import Flask,render_template,request
import pandas as pd
from werkzeug.exceptions import HTTPException
from standard_columns import std_col

app = Flask(__name__)

std_colName  = std_col  
filename = ""

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/map_col",methods = ['GET','POST'])
def map_col():
    global std_colName
    global filename
    filename = request.form.get('myfile')
    file_extension = filename.split(".")[1]
    if file_extension == "csv":
        input_file = pd.read_csv(filename)
        p_colName = []
        for col in input_file.columns:
             p_colName.append(col)
        return render_template('update_col.html',cols = p_colName,std_cols = std_col)
    else:
        return render_template('wrongFileType.html',file_extension=file_extension)


col_list = []
@app.route("/download_csv",methods = ['GET','POST'])
def download_csv():
    global col_list
    global filename
    col_list = request.form.getlist('col')
    file = pd.read_csv(filename,header=None,skiprows=1,names=col_list)
    file.to_csv("output.csv",index=False)
    return render_template("download.html")

# 403 FORBIDDEN
@app.errorhandler(403)
def forbidden(e):
    return render_template("forbidden.html"),404

# 404 PAGE NOT FOUND
@app.errorhandler(404)
def page_not_found(e):
    app.logger.info(f"Page not found: {request.url}")
    return render_template("404.html"),404


if __name__ == "__main__":
    app.run(debug=True)