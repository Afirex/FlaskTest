from flask import Flask,render_template
import os
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile/<name>')
def hello(name=None):
    return render_template('profile.html', name=name)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/SpuriousTool/')
def about1():
    os.system('PLAY.vbs')
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
