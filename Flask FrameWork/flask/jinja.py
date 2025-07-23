from flask import Flask,render_template,request,redirect,url_for

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

@app.route("/input_result",methods=["GET","POST"])
def result():
    if request.method=='POST':
        math_score = int(request.form.get("math"))
        science_score = int(request.form.get("science"))
        ds_score = int(request.form.get("datascience"))
        ml_score = int(request.form.get("ml"))
        oop_score = int(request.form.get("oop"))
        total_score=(math_score+science_score+ds_score+ml_score+oop_score)/5
    else:
        return render_template("resultinput.html")
    return redirect(url_for("get_score",total_mask=total_score))
    

@app.route("/get_score/<int:total_mask>")
def get_score(total_mask):
    result=""
    if(total_mask>=50):
        result='PASS'
    else:
        result="FAIL"
    exp={
        "marks":total_mask,
        "result":result
    }
    return render_template("showResult.html",exp=exp)

if __name__=="__main__":
    app.run(debug=True)