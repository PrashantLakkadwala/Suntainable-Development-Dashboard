from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard.html')
def dashboard():
    return render_template('dashboard.html')

@app.route('/story.html')
def story():
    return render_template('story.html')

@app.route('/report.html')
def report():
    return render_template('report.html')


if __name__ == '__main__':
    app.run(debug=True)