from flask import Flask, render_template, url_for, redirect
import requests

app = Flask('__main__')


@app.route('/')
def index():
    res = requests.get('https://api.npoint.io/0474556ce29410042eca')
    res.raise_for_status
    data = res.json()
    return render_template('index.html', posts= data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')





    


if __name__ == '__main__':
    app.run(debug=True)
  