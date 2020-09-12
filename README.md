# NAD Mapper Tool

## Folder Structure

* Templates
  * home.html
  * update_col.html
  * download.html
  * ....
* main .py
* standard_columns.py

## Main.py

```python
  def home():
    return render_template("home.html")
```
> * On starting server it will return home page which has select file tag. 
> * On selecting a file and clicking submit button it will send name of file to map_col method.

```python
  def map_col():
    # code     
```
> * from the file name it recives from home method it extract the header names and transfer it to update_col.html
> * update_col.html show all header names on one side and drop down menu on exactly opposite to each column name for user to map each with respective ones.
> * After user map columns with standard col the result get back to map_col function as form of python dictionary to check that mandatory column are mapperd or not
> * if mapped then new column name are send to download method other wise back to updat_col.html page with error stating the mandatory standard column name which are left from mapping


```python
  def download():
    # code     
```

> * this method recives the list of new headers and it remove the first row(header row) from csv and enter a new header row (the updated mapped one)