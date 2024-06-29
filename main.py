from flask import Flask, render_template, request
import requests
import smtplib

MY_GMAIL = "adex.dbaba@gmail.com"
MY_PASSWORD = "fhgvciamnejldnvo"

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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_GMAIL, MY_PASSWORD)
        connection.sendmail(MY_GMAIL, MY_GMAIL, email_message)


@app.route('/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)





    


if __name__ == '__main__':
    app.run(debug=True, port=5001)
  