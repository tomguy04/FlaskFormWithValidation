# Assignment: Dojo Survey
# Build a flask application that accepts a form submission, redirects, and presents the submitted data 
# on a results page.

# The goal is to help you get familiar with sending POST requests through a form 
# and displaying that information. 


from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
# our index route will handle rendering our form

#1
@app.route('/')
def index():
  return render_template("form.html")

# this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route
# WE ARE WAITING FOR A POST REQUEST
@app.route('/process', methods=['POST'])
def data():
   print "Got Post Info"
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   print "*" * 80, name
   print "*", location
   print "*", language
   print "*", comment
   print len(request.form['name'])
   print len(comment)
   if len(request.form['name']) < 1 and len(comment) < 1:
      flash("name cannot be blank!")
      flash("comment cannot be blank!")
      return redirect('/') 
   elif len(request.form['name']) < 1:
      flash("name cannot be blank!")
      return redirect('/') 
   elif len(comment) < 1:
      flash("comment cannot be blank!")
      return redirect('/') 
   elif len(comment) > 120:
      flash("comment cannot be longer than 120 characters!")
      return redirect('/')
   else:
      # flash("Success!")
      return render_template("data.html", myname = name, mylocation = location, mylanguage = language, mycomment = comment)


   
   
app.run(debug=True) # run our server

