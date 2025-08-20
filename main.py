from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["DEBUG"] = True

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('auth/login/login.html');

@app.route('/register')
def register():
    return render_template('auth/register/register.html');

@app.route('/<name>')
def hello(name):
    return render_template('home/index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)