
# to have access to environmental variables.
import os
from flask import Flask

#initialising and defining our new flask application
app = Flask(__name__)
#creating empty list
messages = []

#now creating a function (add_messages) which takes username and message and appends to the list.
def add_messages(username, message):
    #then calling append method to messages list and append a string, using format method. Positional indicators {0}{1} are omitted, as in python3, it's optional to include them or not. If left out, first set of curley brackets automatically refers to 1st argument, 2nd set of curley brackets refer to 2nd argument.  
    messages.append("{}:{}".format(username, message))

#creating app route decorator for index page
@app.route("/")
#this is the function which will be bound to our decorator
def index():
    
    """Main page with instructions"""
    #removing <Hello There>. 
    #don't use <> for sending message, as this will be interpreted by html and won't display properly.
    return "To send a message use /USERNAME/MESSAGE"

#creating routes/views using @app decorator, using <>, this then gets treated as a variable.
@app.route("/<username>")
#argument of username
def user(username):
    #using docstring to document. Good practice to document functions.
    """Display chat messages"""
    #changing message using positional indicator and curley brackets, using .format method and sending in username and messages list.
    return "Welcome, {0}".format(username, messages)
    
#creating another app route decorator for sending message.
@app.route("/<username>/<message>")
#creating function which binds to decorator, taking 2 arguments (username and message)
def send_message(username, message):
    
    #Now want to store message in a list. Using docstring here to document.
    """Create a new message and redirect back to the chat page"""
    
    #using .format method to display message.
    return "{0}: {1}".format(username, message)

#environmental variables in cloud9 and also which we set ourselves in Heroku.    
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)


