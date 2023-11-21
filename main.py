from flask import Flask,render_template
import requests
app = Flask(__name__)

response = requests.get('https://api.npoint.io/eb6cd8a5d783f501ee7d')
blog_all = response.json()

@app.route('/')
def main():
    return render_template("index.html",blog_all = blog_all )
@app.route('/About')
def about():
    return render_template('about.html')
@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/Post/<int:index>')
def show_post(index):
    for blog_post in blog_all:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

app.run()