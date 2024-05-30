from flask import Flask,render_template, url_for,flash,redirect
from form import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '206802a5986c7bb650d970ec7dbe308e'

posts=[{"author":"Aron Rop","title":"Blog Poss 1","content":"First Post content","date_posted":"May, 27 2024"},
{"author":"Dolly Chepng'etich","title":"Blog Poss 2","content":"Second Post content","date_posted":"May, 28 2024"},
{"author":"Naomy Chepkorir","title":"Blog Poss 3","content":"Third Post content","date_posted":"May, 29 2024"}]

@app.route("/")
def home():
    return render_template("home.html", posts= posts)

@app.route("/about")
def about():
    return render_template("about.html",title="about")

@app. route("/register", methods=["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
          flash(f'Account created for {form.username.data}!','success')
          return redirect(url_for('home'))
    return render_template("register.html",title="Register", form=form)
   
@app. route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="login", form=form)



if __name__=="__main__":
    app.run(debug=True, port=5005)