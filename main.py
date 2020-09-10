from flask import *
import pandas as pd
from werkzeug.exceptions import HTTPException
from standard_columns import std_col,checkMandatoryFields,columnSequencing,randomName
from standard_columns import dbf_to_csv
from datetime import datetime
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 50*1024        # setting a limit on file size

std_colName  = std_col                            #standard colums names
filename = ""                                     #to store name of input file
p_colName = []                                    #list to add columns of input csv file
input_file = ""                                   #variable to store name of input csv file



#######################################
################ HOME #################
#######################################

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


#######################################
######## Column Mapper Page ###########
#######################################

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
    elif file_extension == "DBF":
        file_input = dbf_to_csv(filename)
        input_file = pd.read_csv(file_input) 
        for col in input_file.columns:
             p_colName.append(col)
        return render_template('update_col.html',cols = p_colName,std_cols = std_col)
    else:
        return render_template('wrongFileType.html',file_extension=file_extension)


#######################################
######## File Downloaded Page #########
#######################################

save_state = {}                                # dictionary to save state of mapped columns
col_list = []
@app.route("/download_csv",methods = ['GET','POST'])
def download_csv():
    global col_list
    global filename
    col_list = request.form.getlist('col')
    i=0
    for each_col in input_file:
        save_state[each_col] = col_list[i]     # storing current mapping to dictionary
        i+=1
    temp = checkMandatoryFields(col_list)      # check mandotory fields
    if temp == "true":
        col_list = columnSequencing(col_list)
        name = randomName()
        file = pd.read_csv(filename,header=None,skiprows=1,names=col_list)
        file.to_csv(name,index=False)
        return render_template("download.html",name=name)
    else:
         return render_template("update_col.html",cols = col_list,std_cols = std_col,error=temp,state=save_state)
        

######################################
############### 403 ##################
######################################

@app.errorhandler(403)
def forbidden(e):
    return render_template("forbidden.html"),404

######################################
############### 404 ##################
######################################

@app.errorhandler(404)
def page_not_found(e):
    app.logger.info(f"Page not found: {request.url}")
    return render_template("404.html"),404


######################################
############### Main ##################
######################################

if __name__ == "__main__":
    app.run(debug=False)