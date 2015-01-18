from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
@app.route('/admin.html')
def admin():
    items = range(200)
    return render_template('admin.html',items=items)

@app.route('/edit.html')
def edit():
    return render_template('ace_edit.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
