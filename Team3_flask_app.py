###############################################################################
##
## This starter code was taken from Lab  6 Flask application and modified
## for the team 3 application
##
## The **prefix.py** code is included to allow you to develop your code within
## the **csel.io** environment.  There is a required prefix to be used when
## pages access the **csel.io** virtual machine from your local machine browser.
## 
## The prefix code will have no effect when running Flask on your local machine
## as it looks to make sure you are running on **csel.io** virtual machine.
##
## Author: Knox - Sept 2022
## Contributor: Fall 2023 Team 3 Members
##
###############################################################################


###############################################################################
## Import "prefix" code into your Flask app to make your app usable when running
## Flask either in the csel.io virtual machine or running on your local machine.
## The module will create an app for you to use
import prefix

from flask import Flask, url_for

# create app to use in this Flask application
app = Flask(__name__)

# Insert the wrapper for handling PROXY when using csel.io virtual machine
# Calling this routine will have no effect if running on local machine
prefix.use_PrefixMiddleware(app)   

# test route to show prefix settings
@app.route('/prefix_url')  
def prefix_url():
    return 'The URL for this page is {}'.format(url_for('prefix_url'))

###############################################################################
##
## Begin Routes for Team 3 Exercise Food Application

from flask import Flask

@app.route('/')
def index():
    resp = '''<pre>
           <pre> '''
    return resp

@app.route('/login')
def login():
    resp = '''<pre>
           <pre> '''
    return resp

@app.route('/create_aaccount')
def create_account():
    resp = '''<pre>
           <pre> '''
    return resp


###############################################################################

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

###############################################################################


from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
    
@app.get('/login')
def login_get():
    return show_the_login_form()

@app.post('/login')
def login_post():
    return do_the_login()

###############################################################################


from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_temp(name=None):
    return render_template('hello.html', name=name)

###############################################################################
## Place your optional routes here


###A_1 Static ascii text page, text read from known filename(story.txt) uses template (a_1.html). ('/a_1')###
from flask import Flask, render_template

@app.route('/a_1')
def a_1():
    with open("story.txt", "r") as f:
        content = f.read()
    return render_template("a_1.html", content=content) 



###B_1 Static HTML page, HTML source read from known filename (b_1.html in static)###
from flask import Flask, render_template

@app.route('/b_1')
def b_1():
    with open("static/b_1.html", "r") as f:
        content = f.read()
    return content




###B_4 Static HTML Page, the HTML displays a table of static data (Didnt realize this wasnt an option, but did it anyway)###
from flask import Flask

@app.route('/b_4')
def b_4():
    
    return table



###C_1 Dynamic text, read, increment, and write a value in a file (hits.txt in static), value added to page.###
@app.route('/c_1')
def c_1():
    with open("static/hits.txt", "r") as f:
        hits = int(f.read())
    hits += 1
    with open("static/hits.txt", "w") as f:
        f.write(str(hits))
    return "There have been " + str(hits) + " visits to our web page!"


###############################################################################
# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server using port 3308 instead of port 5000.
    app.run(host='0.0.0.0', port=3308)


