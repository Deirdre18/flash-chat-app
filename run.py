
# to have access to environmental variables.
import os
from flask import Flask

#initialising our new flask application
app = Flask(__name__)

#creating app route decorator for index page
@app.route("/")
#this is the function which will be bound to our decorator
def index():
    return "<h1>Hello There</h1>"
#environmental variables in cloud9 and also which we set ourselves in Heroku.    
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)

   
