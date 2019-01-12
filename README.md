(Lessons as transcribed from Code Institute online tutorials).

# Flask Chat Application - Introduction

LESSON:

I'm happy to welcome you back to our Flask mini-project.
The internet was built for communication.
In fact, the first online chat application dates right back to 1973.
But this was only for a limited number of users at the University of Illinois.
In 1980, CompuServe released the first widely available chat application.
But in more recent times, since the Internet has become ubiquitous, chat rooms and chat applications have popped up everywhere. If you play any multiplayer game, then chances are it has a chat room.
In this lesson, we're going to build our mini-project, which will be a simplified chat application using the Flask framework. Purpose of the project and throughout the project we're going to:-

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

# Basic Routes And Views (using advanced routing in Flask)
 
## What is it?

The main routes and views that we'll be using in our project

## What does it do?

Allows us to send messages via our URLs

## How do you use it?

By creating views that will handle those URLs

LESSON:
In our previous video, we got our basic project structure in place for our simple Flask chat app.
Now we can go ahead and start adding some views.
Right now in our index view, all we're doing is returning the phrase Hello There!
But what I'd like is for it to return some instructions.
So if we go to our index page, it tells us how to use our app.
So I'm going to put a message in here that says "To send a message use /<USERNAME>/<MESSAGE>"
Unfortunately, the angle brackets will be interpreted by the browser as HTML, so this won't actually display properly.
I'll demonstrate that in a minute.
And then I'm going to add in a docstring, which just says """Main page with instructions""".
Remember, we encountered docstrings before in the boggle solver.
And it's good practice to use this format to give some information as to what each function our module in your project does.
Now that that's been done, I can go to Cloud9 again, refresh it, and we see I have: To send a message use //.
So we'll take out the angle brackets, so it just says: "To send a message use /USERNAME/MESSAGE".
Very good, because the way that we want our little chat app to work is that we'll be able to supply a "/" and a username, such as Aaron, a "/" and then a message, such as "hi there".
At the moment, this doesn't do anything because we haven't created any routes or views to handle that.
So let's create one first of all.
We'll create a new app root decorator, and this one is going to have /<username>
Remember, then, this gets treated as a variable.
We're going to create a function that's going to bind to our root decorator.
I'm just going to actually call it user, rather than username.
And that's going to take the argument of username.
And then what I want to do is return to the user a string that just says "Hi: and then the username that we provided.
So we'll just append the username here: "Hi" + username.
If I try this now and go to /Aaron, then it says hi Aaron.
So that works.
Let's create another one now to allow us to create a message.
So again, another app root decorator.
This time we're going to have: @app.route('/<username>/<message>')
We're going to create a function and bind it to our decorator, and that's going to be called send_message().
And that will take two arguments, both the username and the message.
We put a ":" on the end here.
And I'm just going to use the format method here to format what we're returning.
So we'll return a string.
And the first part is going to be the username.
Then we'll have a ":", and then we'll display our message.
So we're going to use the .format() method.
And as we said, firstly we're going to format the username and then the message.
So now if I test this by doing /Aaron /hi, then I can see it displays the username first, then a ":", and then the message.
Now, this is on a new page completely. It's cleared out the rest of the page.
We'll have a look at how to fix that later on.
But now I'm just going to add run.py to my local Git repository.
And I'm going to commit that with the message of "Implement basic views and routing".
So that completes our second video showing how we can implement basic views, but still using advanced routing in Flask.
In our next video, we're going to have a look at how to store our messages.

In our previous video, we got our basic project structure in place for our simple Flask chat app.
Now we can go ahead and start adding some views.
Right now in our index view, all we're doing is returning the phrase Hello There!
But what I'd like is for it to return some instructions.
So if we go to our index page, it tells us how to use our app.
So I'm going to put a message in here that says "To send a message use /<USERNAME>/<MESSAGE>"
Unfortunately, the angle brackets will be interpreted by the browser as HTML, so this won't actually display properly.
I'll demonstrate that in a minute.
And then I'm going to add in a docstring, which just says """Main page with instructions""".
Remember, we encountered docstrings before in the boggle solver.
And it's good practice to use this format to give some information as to what each function our module in your project does.
Now that that's been done, I can go to Cloud9 again, refresh it, and we see I have: To send a message use //.
So we'll take out the angle brackets, so it just says: "To send a message use /USERNAME/MESSAGE".
Very good, because the way that we want our little chat app to work is that we'll be able to supply a "/" and a username, such as Aaron, a "/" and then a message, such as "hi there".
At the moment, this doesn't do anything because we haven't created any routes or views to handle that.
So let's create one first of all.
We'll create a new app root decorator, and this one is going to have /<username>
Remember, then, this gets treated as a variable.
We're going to create a function that's going to bind to our root decorator.
I'm just going to actually call it user, rather than username.
And that's going to take the argument of username.
And then what I want to do is return to the user a string that just says "Hi: and then the username that we provided.
So we'll just append the username here: "Hi" + username.
If I try this now and go to /Aaron, then it says hi Aaron.
So that works.
Let's create another one now to allow us to create a message.
So again, another app root decorator.
This time we're going to have: @app.route('/<username>/<message>')
We're going to create a function and bind it to our decorator, and that's going to be called send_message().
And that will take two arguments, both the username and the message.
We put a ":" on the end here.
And I'm just going to use the format method here to format what we're returning.
So we'll return a string.
And the first part is going to be the username.
Then we'll have a ":", and then we'll display our message.
So we're going to use the .format() method.
And as we said, firstly we're going to format the username and then the message.
So now if I test this by doing /Aaron /hi, then I can see it displays the username first, then a ":", and then the message.
Now, this is on a new page completely. It's cleared out the rest of the page.
We'll have a look at how to fix that later on.
But now I'm just going to add run.py to my local Git repository.
And I'm going to commit that with the message of "Implement basic views and routing".
So that completes our second video showing how we can implement basic views, but still using advanced routing in Flask.
In our next video, we're going to have a look at how to store our messages.

# Storing Our Messages
 
## What is it?

A Python list


## What does it do?

Allows us to store our messages as strings


## How do you use it?

By appending an item to the list everytime a new message is created.


LESSON:
In our previous video, we got our basic views and routes in place for our little Flask chat application.
But what we want to be able to do is to take the message and store it in a list.
Now before I do that, I just want to add in some docstrings here to my functions, just to document them properly.
So: """Create a new message and redirect back to the chat page"""
Again, for my username root, I'm going to pass in """Display chat messages""".
It's very good practice to document your functions like this using a docstring.
So now we'll create an empty list under where we define our Flask app.
We're going to put messages = [ ].
We'll now create a function called add_messages(), which will take our user name and message and append it to the list.
To do this, we're going to create this function that takes two arguments, username and message.
And then we're going to call the append() method on our messages list.
So messages.append(), and we'll append a string.
I'm going to use the format method again.
So ("{}: {}".format(username, message)).
Now you might be wondering why I've missed out the 0 and the 1 there, the positional indicators in those curly brackets.
The reason is that since Python 2.7, it's been optional to supply those positional indicators.
If I leave them out, then the first set of curly brackets automatically refers to the first argument, and the second set of curly brackets automatically refers to the second argument.
So just as a shortcut, I can leave those out.
Now that that's in place, I just want to update line 20 here, so that instead of just saying Hi and the username, it says Welcome.
And then I'm going to put in a positional indicator: {0}, use the .format() method, and send in the username and the messages list.
Okay, then I refresh this and try again.
So I'm going to say /aaron/hello aaron, then we can see that that's displayed.
I'll do another message: /aaron/how are you
So the messages are being displayed.
But when I go back to my welcome page, we can see that it says "Welcome, Aaron", but it's not actually displaying any of the messages.
That's because we're not actually calling our add_message() function to store the messages in our list yet.
We'll have a look at that in our next video and see how we can nicely present the messages to the user.
  
  
# Presenting Our Messages
 
## What is it?

Displaying our chats messages


## What does it do?

Renders our messages in the browser


## How do you use it?

By outputting the messages as a string

LESSON:
In our previous videos, we got the basic structure of our Flask app up and running, including our roots, our views and our add_messages() function.
But our messages weren't displaying to the user.
The reason was that we weren't actually calling this function from anywhere in our project.
To do this, I'm going to edit my send_message() function and remove the format() method.
Instead, I'm going to call our new add_messages() function with username and message as the arguments.
I'm then going to add in a return.
And I'm going to redirect back to the user's personalized welcome page.
So that's: return redirect(username).
We used redirect() before when we were redirecting after filling out our contact form.
And this will redirect us back to this decorator here, which is the user's personalized welcome page.
In order for this to work, I also need to import the redirect module from the Flask library.
Now you'll notice we have an error message here on line 20.
That's because we're passing in two arguments to format, but we're only actually referencing one field.
So let's put: - {1}
This will then display our messages list.
When I run our application and go to the preview of this, then we can see that we now have an empty list here.
If I create a message that says hi, then now it'll say 'aaron: hi'.
Let's create another one.
I'm going to say how are you?
And now the appended to the list as well.
So we have 'aaron: hi' and 'aaron: how are you'.
Now this is displaying okay, but it's not very pretty.
What we'd like to be able to do is to display that in a nice way for the user.
So before we do that, I just want to add a docstring to my add_messages() function here.
Again, as we said, it's very good practice to add docstrings to all of your functions.
And my doc string is just going to say """Add messages to the `messages` list""".
So now let's create a function that's going to display those messages for us.
It's going to be called get_all_messages().
And this one doesn't need to take any arguments.
We'll create a docstring straight away that says: """Get all of the messages and separate them with a `br`"""
And what we're going to do, then, is just a return.
And we'll use the join() method.
We're going to use a <br> tag to join all of the elements in our messages list together.
So return "<br>".join(messages).
And then finally, in my personalized user page, I need to change the messages list to actually call our get_all_messages() function.
So we'll save that, go back to our preview window, and refresh the page.
And now our empty list has vanished.
So now if I pass in a message that just says hi, then that display is much nicer.
If I send in another message, then it should appear in a separate line because now this has been separated using our <br> tag.
And then a third message.
So already this has been presented much nicer.
What I'd like to do, though, is to put my welcome message in <h1> tags.
That will make sure that the welcome banner always appears at the top of the screen on its own and any subsequent messages appear on a separate line.
So we can put our <h1> tags in here surrounding our welcome message and take out the "-".
Now if I refresh the page and pass in a couple of messages, we can see that our chat app is displaying them much nicer.
We have our heading at the top and then the messages underneath.
So our chat app is working as we would want it in this very basic way.
What we can do then is use Git and add our run.py file.
And then we will commit that with the message "Add the ability to write to and read from a list and display the messages to the user"
And that completes the basic functionality of our chat app.
There's much more that we want to be able to do with it, though, including the ability to display our messages with timestamps.
We'll look at that in our next series of videos.

# Adding Timestamps

## What is it?

A timestamp

## What does it do?

It will enable us to show the time at which the message was sent

## How do you use it?

By using Python's datetime module

LESSON:
In our previous videos, we set up the basics of our chat app in Flask.
In this series, we want to expand that functionality.
And the first thing we want to do is to see what time the message was sent.
We want to add a timestamp.
Currently, as we can see from our app, whenever we have a conversation, no timestamps are being added.
I'll open the application here and start a conversation.
So Aaron is going to say hi, and the message just appears.
It's a sign of loneliness, but I'm going to have a conversation with myself and respond from Yoni, who also says hi.
But we can see that we don't know when what time those messages were actually sent.
To add a timestamp, then, on line 2, we need to import the datetime module from the datetime library, which is a built in module in Python's standard library that allows us to work specifically with dates and times.
So on line 10, I'm going to create a new variable: now = datetime.strftime()
The strftime() method takes a date/time object and then converts that to a string according to a given format.
So what I need to do, then, is provide a format.
And that's what we're doing in the brackets here.
%H is for the hour in 24 hour format.
%M is for the minutes.
And %S is for the seconds.
I also need to add the now() method here because that's going to get the current time.
I had to correct some typos, it's strftime().
Then on line 11, I'm going to add some brackets with some curly braces inside and then add the now variable that we've just created.
I have two other typos I need to correct.
Now is a method; there shouldn't be a full stop there.
And I'm just calling my variable now.
So if I carry on this lonely conversation with myself, then Aaron says hello.
And now we have a timestamp.
Yoni will respond with hi, and we can see that the number of seconds has advanced.
As I carry on talking to myself, the time changes on the timestamp, so we can see what time the messages were actually left.
Very good, so this is working as expected.
In our next video, we're going to tidy things up a little bit by adding an index.html page, instead of just returning a welcome string.

# Creating An Index.Html Page
 
## What is it?

The index.html page

## What does it do?

It will display a form that will ask users for a username

## How do you use it?

By creating the HTML page and handling the form submission on the backend

LESSON:

In our previous video, we got our timestamps up and working so that we could see what time a message was left.
In this video, we're going to create a template for our index page.
And in future videos, we'll create more templates too.
So to do that, the first thing that we need to do is create a templates folder in our project.
I'm going to right click on my flask- chat folder, create a new directory, and call it templates.
Inside that, we need to create a new file, which is going to be called index.html.
You'll remember from our previous projects that in order to render a template, rather than return a string, we need to import the render_template module from our Flask library.
So we'll do that on line 3.
After redirect, we'll add a comma and then render_template.
Now, we can go down to my index view, and, instead of returning a message, we'll return render_template("index.html").
Let's start adding some content to our index.html file.
It's going to be very straightforward code.
Just some <html> tags, a <head> section, the title is going to be just Home Page for now.
Outside of the <head>, we'll create some <body> tags and then some <p> elements to display our message.
And the <p> elements will contain the same instruction that we had before.
In actual fact, rather than type all of this out, I'm going to go back to my run.py file, just copy that, and undo everything until the original message comes back up.
So now I can put in a return and paste in my render_template.
And then I can just cut this message, delete that return, and go back to my index.html file and paste it in.
We just remove the quotes as well to tidy things up.
So this is exactly the same welcome message as we were giving before.
Okay, so now I can run my application and check my index.html page.
And when I do, you can see that we have exactly the same message that we had before.
It used to be a string that was being output, but now it's coming from our index.html template.
I can still go to /aaron to create a new user.
And that's returning a string.
It's not coming from our template.
In future videos, we're going to improve our index.hmtl template.
As you can see, we're not taking our chat from a template.
There's no <title> tag, so it's just returning the address of our chat application.
So that completes creating our index.html template for now.
In our next video, we're going to see how to add more functionality to that and create and store users in a text file.

# Creating Users
 
## What is it?

Storing Users in a session variable

## What does it do?

Allows us to persist usernames in a browser session to automatically redirect users to their homepage

## How do you use it?

By initialising a session and a variable

LESSON:

In our previous video, we created our index.html template.
But now, we want to do much more with it .
In this video, we're going to introduce you to something called session variables.
We're going to use this to store our username so that when we go to our chat app, we will automatically be redirected to our personal homepage.
First though, let's have a little chat about what a session actually is.
Simply put, a web session is a way that we can store data for a short period of time in our application.
This is initiated by the server, and when it's been opened, we're given a unique and specific session ID.
Generally, we don't see the session ID because it's contained in the headers that are sent from the server.
But when we have this unique ID, we can use it to store variables.
Sometimes, data can be stored either in a temporary area on the server, or on our computer.
And we're going to store it in what's called a cookie.
A cookie is a small piece of data that's stored in our computer by a web browser.
Now, they're very small. They're only limited to file kilobytes in size.
But they're useful for storing things, like what we have in our shopping cart on a website, or what account we're logged in with.
They can be stored as text files, but we're going to use a session cookie, which will be deleted when we close the browser.
We're going to use Flask to create a cookie, which will store our username so that when we visit the website, it will redirect us to our personal homepage.
To do this, we need a couple of extra modules from our Flask library.
The request module, which will handle our username form, and the session module, which will handle the session variables.
To generate our session ID, we need to give our app what's called a secret key, which is a random list of letters, numbers, and characters.
Generally, in production, we'd have it set as an environment variable like we did with our IP address import.
But for now, we'll put it as a string.
Now we need to create our form in index.html.
So let's delete the paragraph and create a form where we ask for a username.
So we'll create a <form method= "POST".
Then a <label for="username">Username:</label>
Then we need to create our input box.
So that's going to be: <input type="text".
We'll give it id="username", in case we want to style it later.
And the name="username" so that we can refer to it in our run.py file.
Finally then, we'll create a <button>, which will have the text Go to chat!
And when this is clicked, our form will be posted.
Now let's just check to see that it's working.
We'll just go to our index.html page and refresh the page.
And there we see that we have our username form and our Go to chat! button.
Now at the moment, that won't work because we need to add both the GET and the request methods to our index route.
So let's do that.
On line 22 here, we'll add a comma in our route.
We'll say methods = ["GET", "POST"] so that it accepts both the GET and the POST methods.
Now, in our index view, we're going to add an if statement that says if request.method == "POST":, then we want to create a new variable in our session called username.
So we're going to create our session username variable; session["username"].
And we want that to be equal to request.form["username"], so the username that we typed and posted from our form.
Now that our username is set, we need to check to see that it's there so that if the username exists, we're going to redirect to our personal chat page.
So we're going to say if "username" in session, so if the username variable is set, then instead of returning our index.html template, we're going to redirect to the contents of the session username variable.
So our username here and our username in session are both the same.
And then we're going to redirect to session username, which will take us to this route here.
Let's see if that works.
We'll go back to our index page.
I'm just going to refresh it.
And I'll type in Aaron here as the username.
And now when I click on Go to chat!, then we're redirected to Aaron's personal homepage.
And this data will persist.
So if I close down the tab that we have here, reopen it, and go to the homepage, then we're automatically redirected to Aaron's homepage, instead of rendering index.html again.
If I right click and go to inspect, we can click on application, cookies, and then our chat app here.
And we can see that I have this cookie with the name of session set.
This cookie contains our username, and that's what we're checking each time.
This is a session cookie, so if we close the browser then this cookie will be erased.
So in this section, we've expanded our chat application by adding timestamps, an index.html page, a user form, and session variables to store our username.
In our next series of videos, we're going to add even more features to our chat app.
We'll refactor our code and then deploy the finished project to Heroku.

# Refactoring To Use Chat.Html Instead Of A Single String

## What is it?

An HTML file


## What does it do?

It will display our chat messages


## How do you use it?

By passing it the necessary chat messages

LESSON:

In our previous video, we changed how the messages are stored.
But this seemed to break how our messages are displayed.
To improve this, let's start displaying our messages in a template.
So back in our project, we're going to create a new HTML file in our templates directory.
And we're going to call that chat.html.
When that's created, we can open it for editing and then do ! and tab to put in the standard HTML boilerplate from Cloud9.
Now we want to display our welcome message and the chat messages like we were doing before.
So we'll put in <h1>.
We'll say Welcome.
And we're going to pass in the username variable from our view.
Underneath that, we're going to put in the chat_messages variable.
And these are both variables that we're going to pass through from our view to the template.
In fact, just to make things look a little bit nicer, in our title, we're going to change it so that it says Chat page for.
And then our username variable again.
And this will be another way we can make sure that our HTML template is working.
Okay, now that our template is made, we need to put in these two variables so that we can display it
To do that, we'll go back to our run.py file.
And in our user view, we can take out this return.
Now we want to do a return with render_template.
And it's the chat.html template that we want to render.
The arguments that we're passing through are username, as we said.
And that's going to be equal to the username that we're passing into this function.
And chat_messages is going to be equal to our messages list.
Now that that's done, we can save it, go back to our chat page, and refresh it.
And because our server has restarted, the list is now empty.
But we can see that it's there.
In fact, if I just pull down so that you can see the title of this page, you can see now that it says Chat page for aaron.
So our HTML template is being rendered correctly.
It might look like we're just back in the same place where we were at the start of this video.
But we're actually in a much better position.
Because now we're using actual HTML, we can start formatting our messages in a much nicer way and add more functionality.
We're going to do that in our next video by adding in some JavaScript.
  

