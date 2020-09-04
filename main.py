from flask import *
import pandas as pd
from werkzeug.exceptions import HTTPException
from standard_columns import std_col,checkMandatoryFields
#from mapper_forms import MapperForm

app = Flask(__name__)

std_colName  = std_col              #standard colums names
filename = ""                       #to store name of input file
p_colName = []                      #list to add columns of input csv file
input_file = ""                    #variable to store name of input csv file

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


#################################################################################################################################
@app.route("/map_col",methods = ['GET','POST'])
def map_col():
    global std_colName
    global filename
    global input_file
    filename = request.form.get('myfile')
    file_extension = filename.split(".")[1]
    if file_extension == "csv":
        input_file = pd.read_csv(filename) 
        for col in input_file.columns:
             p_colName.append(col)
        return render_template('update_col.html',cols = p_colName,std_cols = std_col)
    else:
        return render_template('wrongFileType.html',file_extension=file_extension)
#####################################################################################################################################
save_state = {} # dictionary to the states of mapped columns
col_list = []
#temp_col_list = []
@app.route("/download_csv",methods = ['GET','POST'])
def download_csv():
    global col_list
    global filename
    #global temp_col_list
    #temp_col_list = col_list
    col_list = request.form.getlist('col')
    i=0
    for each_col in input_file:
        save_state[each_col] = col_list[i]
        i+=1
    temp = checkMandatoryFields(col_list)      # check mandotory fields
    if temp == "true":
            file = pd.read_csv(filename,header=None,skiprows=1,names=col_list)
            file.to_csv("output.csv",index=False)
            return render_template("download.html")
    else:
         return render_template("update_col.html",cols = col_list,std_cols = std_col,error=temp,state=save_state)
        
##########################################################################################################################################################
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