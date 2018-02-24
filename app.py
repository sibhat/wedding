from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def mainPage():
    return render_template('index.html')
@app.route('/slideshow')
def slideshow():
    return render_template('slideshow.html')

if __name__ == '__main__':
    app.secret_key = 'super_secrect_key'
    app.debug = True
    app.run(host='0.0.0.0', port=3000)