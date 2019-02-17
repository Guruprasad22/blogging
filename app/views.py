from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'name' : "Guruprasad"}
    posts = [
            {
                'author' : {'name':'Shishya'},
                'body' : 'hello from the other side'
            },
            {
                'author' : {'name':'Praveen'},
                'body' : 'simply irresistable'
            }
        ]
    return render_template('index.html',user=user,posts=posts)
        