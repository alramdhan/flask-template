from flask import Flask, render_template, url_for
app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/<name>')
def hello(name):
    return render_template('home/index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)