from flask import Flask,render_template

"""
it create an intance of flask class,which will be your WSGI
"""
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome Back our page...."

@app.route("/profile")
def get_profile():
    return "Welcome your profile page...."
@app.route("/about")
def get_about():
    names=["susovan","taniya"," mimi","ram"]
    return render_template("about.html",names=names)

if __name__=="__main__":
    app.run(debug=True)


""" 
🥀 What is Jinja2?
Flask uses Jinja2 as its template engine.

🔥 What is a template engine?
When you want to create HTML pages dynamically (e.g., show user data, render a table of products), you use a template engine.

Jinja2 lets you embed Python-like code in your HTML.
"""