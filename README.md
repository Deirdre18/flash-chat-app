(Lessons as transcribed from Code Institute online tutorials).

# Flask Chat Application - Introduction

LESSON:

I'm happy to welcome you back to our Flask mini-project.
The internet was built for communication.
In fact, the first online chat application dates right back to 1973.
But this was only for a limited number of users at the University of Illinois.
In 1980, CompuServe released the first widely available chat application.
But in more recent times, since the Internet has become ubiquitous, chat rooms and chat applications have popped up everywhere.
If you play any multiplayer game, then chances are it has a chat room.
In this lesson, we're going to build our mini-project, which will be a simplified chat application using the Flask framework.
Purpose of the project and throughout the project we're going to:-

(1) learn how to create and run our Flask project.

(2) We'll look at how to take information from URLs and store it in some manner.
 
(3) And then we want to learn how to present that information back to the user so that they can read our chat messages.

So let's dive straight in and start creating our Flask chat app.

# Beginning The Project

## What is it?

Beginning a Flask project


## What does it do?

Gives us a starting point for our project


## How do you use it?

By creating a new Flask project

LESSON:

So let's get started with our Flask chat application.
To do that, we need to create a new workspace.
And I'm just going to call this flask-chat.
And I'm going to use the blank workspace template.
So the idea behind our chat application is that we're going to create these URLs based around usernames.
And when the user puts a chat message up, we'll be able to display that in the browser along with the timestamp.
Now that our application has been created, let's just add some information to our README.md file to indicate what we're going to do.
So I'll put a hashtag in here and a space.
Remember that that is a <h1> heading when the README.md file is converted to HTML.
And I'm going to say Flask Chat App as my heading.
And then a little paragraph as explanation of what we're going to do: This is a chat application written in Flask.
And then just explain the purpose of our application.
Okay, now that that's been done then, we can run a git init command so that our empty Git repository is initialized.
And then we'll create a new file, which we're going to call run.py.
Just as we did before, we're going to create a new Flask application.
So the first thing we want to do is import os so that we'll have access to the environment variables.
And then on our second line: from flask import Flask.
On line 4, we'll initialize our new Flask application: app = Flask(__name__)
We'll then create our app root decorator, which is going to be for our index page, so that will just be ('/').
And then on line 7, we'll define the function that is going to be bound to our decorator: def index().
It doesn't take any arguments.
And just for now, we're going to return a <h1> that says Hello There!.
So we'll put that text in the return and close my <h1>.
Underneath that then, we can do app.run.
This is similar to what we did before, but this time I'm going to pass it all in in the bracket so that it's a shorter version.
We're going to use os.getenv('IP') to get the IP address.
That's an environment variable set by Cloud9, and also one that we set for ourselves in Heroku you'll remember.
And then os.getenv('PORT').
And I just need to supply the names here.
So host=os.getenv('IP'), port=int(os.getenv('PORT')
And then we'll set debug to true.
Okay, so if we try to run that, that will tell us that we haven't installed Flask yet.
So we need to go back to our terminal window and do sudo pip3 install flask.
Okay, so Flask is now installed.
We'll run our Python file, go to the URL that's provided, and open up the application.
And we can see that we have Hello There! displayed.
Now, before I add my files to Git and commit them, what I'm just going to do is create my requirements.txt file.
We did this at the end last time as we were deploying to Heroku.
We're going to do it at the beginning now.
So pip3 freeze --local > requirements.txt
And when we open it, we can see that all of the requirements we have installed.
Now, we only installed Flask, but Flask itself installed Jinja and all of the other different libraries that it depends on.
So now if I run git status, we can see I have three files here.
So I'm going to add my README.md file, add my requirements.txt file, and my run.py file.
Then I can commit them with the message of "Initial commit".
Now that we have our basic Flask app up and working, just as we did before, in our next video, we're going to see how to start building some functionality into that.


