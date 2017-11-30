from flask import Flask, request, redirect, render_template
import cgi, os, jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

#blank check
@app.route('/signup', methods = ['POST'])
def check_validate():
    user_name = request.form['user_name']
    pass_1 = request.form['pass_1']
    pass_2 =request.form['pass_2']
    e_mail= request.form['email']

    user_name_error = ''
    pass_1_error = ''
    pass_2_error = ''
    email_error = ''

    #username
    if len(user_name) < 3 or len(user_name) > 16:
        return render_template('signup_form.html', user_name_error = "That's not a valid username")
    elif ' ' in user_name:
        return render_template('signup_form.html', user_name_error = "That's not a valid username")
    #password
    elif len(pass_1) <= 3 or ' ' in pass_1:
        return render_template('signup_form.html', pass_1_error = "That's not a valid password",)
    elif len(pass_2) <= 3 or ' ' in pass_2:
        return render_template('signup_form.html', pass_2_error = "Passwords don't match")
    elif pass_1 != pass_2:
        return render_template('signup_form.html', pass_2_error = "Passwords don't match")

    #email
    elif ' ' in e_mail:
         return render_template('signup_form.html', email_error = "That's not a valid email")
    elif '@' not in e_mail or '.' not in e_mail:
         return render_template('signup_form.html', email_error = "That's not a valid email")

    else:
        return hello()

@app.route("/hello", methods = ['POST'])
def hello():
    user_name = request.form['user_name']
    return render_template('hello_form.html', name=user_name)

app.run()

#That's not a valid password
#Passwords don't match
#That's not a valid email
