
# to have access to environmental variables.
import os
from flask import Flask

#initialising our new flask application
app = Flask(__name__)

#creating app route decorator for index page
@app.route("/")
#this is the function which will be bound to our decorator
def index():
    
    """Main page with instructions"""
    #removing <Hello There>. 
    #don't use <> for sending message, as this will be interpreted by html and won't display properly.
    return "To send a message use: /USERNAME/MESSAGE"

#creating routes/views using @app decorator, using <>, this then gets treated as a variable.
@app.route("/<username>")
#argument of username
def user(username):
    return "Hi " + username
    
#creating another @app route decorator for sending message.
@app.route("/<username>/<message>")
#creating function which binds to decorator, taking 2 arguments (username and message)
def send_message(username, message):
    #using .format method to display message.
    return "{0}: {1}".format(username, message)

#environmental variables in cloud9 and also which we set ourselves in Heroku.    
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)


