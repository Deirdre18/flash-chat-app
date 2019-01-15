
# to have access to environmental variables.
import os
#importing redirect module from flask library and datetime module.
from datetime import datetime
#importing modules from flask.
from flask import Flask, redirect, render_template, request, session

#initialising and defining our new flask application
app = Flask(__name__)
#creating empty list
#setting a session ID, using random list of letters, numbers and characters. Usually it is set as environmental variable (like IP address), but here we're setting it as a string. 
app.secret_key = "randomstring123"
messages = []

#now creating a function (add_messages) which takes username and message as arguments and appends to the list.

def add_messages(username, message):
    #then calling append method to messages list and append a string, using format method. Positional indicators {0}{1} are omitted, as in python3, it's optional to include them or not. If left out, first set of curley brackets automatically refers to 1st argument, 2nd set of curley brackets refer to 2nd argument. 
    #.creating 'now' variable using .now() method to get current time).
    now = datetime.now().strftime("%H:%M:%S")
    
    #creating dictionary in key-value pairs to store variables, rather than list (as can only access limited info).
    messages_dict = {"timestamp": now, "from": username, "message": message}
    #presenting our messages video: adding docstring.
    """add messages to 'messages' list"""
    #adding brackets, {} and now() method to get current time. 
    #modifiying messages.append, so as to append whole dictionary. 
    messages.append(messages_dict)
    #messages.append("({}) {}:{}".format(now, username, message))
    
#creating function that will get all messages for us.
def get_all_messages():
    """get all messages and separate using <br> - break tag"""
    #using <br> to join all elements in messages together.
    return"<br>".join(messages)



#creating app route decorator for index page
@app.route("/", methods = ["GET", "POST"])
#this is the function which will be bound to our decorator
def index():
    #creating if statement to say tht if request method = POST, then we want to create a new variable called username. 
    if request.method == "POST":
        
        # So we're going to create our session username variable - session["username"]. And we want that to be equal to request.form["username"], so the username that we typed and posted from our form.
        session["username"] = request.form["username"]
        
        #then we want to an another if statement to check if the username exists, and if so then we're going to redirect to personal chat page. So our username here and our username in session are both the same.
        if "username" in session:
            return redirect(session["username"])
    
    """Main page with instructions"""
    #removing <Hello There>. 
    #don't use <> for sending message, as this will be interpreted by html and won't display properly.
    return render_template("index.html")
    #return "To send a message use /USERNAME/MESSAGE"


#creating routes/views using @app decorator, using <>, this then gets treated as a variable.
#adding ability to accept post method in user view.
@app.route('/<username>', methods = ["GET", "POST"])
#argument of username
def user(username):
    #using docstring to document. Good practice to document functions.
    """Display chat messages"""
    #changing message using positional indicator and curley brackets, using .format method and sending in username and messages list.
        #correcting error, as 2 arguments listed but referenced only 1, so adding {1}. This will now display messages list.
    #changing message arguments to call the messages list.
    
    #USERS PERSONALISED WELCOME PAGE(route decorator)
    #messages appear on separate lines.
    
    #return "<h1>Welcome, {0}</h1>{1}".format(username, get_all_messages())
    #return "<h1>Welcome, {0}</h1>{1}".format(username, messages)
    
   
    #Creating a Message Textbox Video: Checking if message sent and adding to messages list.
    if request.method == "POST":
        #obtaining 2 variables, username and message and sending both in to add_messages function to add to messages list.
        username = session["username"]
        #messages came from form, so using request method.
        message = request.form["message"]
        #return to username
        add_messages(username, message)
        return redirect(session["username"])
    
    #adding template to pass in chat.html, using two variables (username, messages) as arguments.
        
    return render_template("chat.html", username = username, chat_messages = messages)
    
    

#creating another app route decorator for sending message.
@app.route("/<username>/<message>")
#creating function which binds to decorator, taking 2 arguments (username and message)

def send_message(username, message):
   
    #Now want to store message in a list. Using docstring here to document.
    """Create a new message and redirect back to the chat page"""
    
    #using .format method to display message.
    
    #presenting our messages video: removing format method and calling add_messages function with username, message as arguments.
    #return "{0}: {1}".format(username, message)
    add_messages(username, message)
    #redirecting back to users welcome page.
    return redirect(username)

    



#environmental variables in cloud9 and also which we set ourselves in Heroku.    
app.run(host=os.getenv("IP"), port=int(os.getenv("PORT")), debug=True)

