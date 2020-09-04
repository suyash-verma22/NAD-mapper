from flask import Flask
from flask_wtf import FlaskForm
from wtforms import SelectField
from standard_columns import std_col
from main import p_colName

class MapperForm(FlaskForm):
    map_with  = {}
    
    __init__(map_with):
