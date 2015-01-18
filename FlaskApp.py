from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/admin.html')
def admin():
    return render_template('admin.html')

@app.route('/ace_base.html')
def base():
    return render_template('ace_base.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/test.html')
def test():
    return render_template('ReadMe.txt')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
