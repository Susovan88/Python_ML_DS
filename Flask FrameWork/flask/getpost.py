from flask import Flask,render_template,request

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

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=='POST':
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        return f" hello {name}!!! \n Your email is {email}. also have a strong password {password}"
    return render_template("form.html")


if __name__=="__main__":
    app.run(debug=True)


""" 
🥀 What is Jinja2?
Flask uses Jinja2 as its template engine.

🔥 What is a template engine?
When you want to create HTML pages dynamically (e.g., show user data, render a table of products), you use a template engine.

Jinja2 lets you embed Python-like code in your HTML.
"""