from flask import Flask, request
import requests

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# Task 2
# Write a return statement such that it displays 'Welcome to <course_name>'
# when you navigate to localhost:5000/course/<course_name>
# Remember to get rid of the pass statement
@app.route('/course/<course>')
def course(course):
   return '<h1>Welcome to '+course+'</h1>'

# Task 3.1
# Edit the HTML form such that form data is sent to localhost:5000/result using POST method
@app.route('/form')
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<form action="/result" method="POST">
  INGREDIENT:<br>
  <input type="text" name="ingredient" value="Enter text">
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
# Note that by default eggs would be entered in the input field
    return s


## Task 3.2
## Modify the function code and return statement
## to display recipes for the ingredient entered
@app.route('/result',methods = ['POST', 'GET'])
def displayData():
    if request.method == 'POST':
      baseurl = 'http://www.recipepuppy.com/api/'
      params ={'i':request.form['ingredient']}
      res = requests.get(baseurl, params = params)
      
    
      return(res.text)

## Task 4
## Note : Since this is a dyanmic URL, recipes function should recieve a paramter called `ingredient` 
@app.route('/recipe/<ingredient>')
def recipes(ingredient):
    baseurl ='http://www.recipepuppy.com/api/'
    params ={'i': ingredient}
    res = requests.get(baseurl,params=params)

    return(res.text)

if __name__ == '__main__':
    app.run()
