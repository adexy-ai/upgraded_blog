from flask import Flask, render_template, url_for, redirect
import requests

app = Flask('__main__')

res = requests.get('https://api.npoint.io/0474556ce29410042eca')
res.raise_for_status
data = res.json()

@app.route('/')
def index():
    return render_template('index.html', posts= data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


    


if __name__ == '__main__':
    app.run(debug=True, port=5001)
  