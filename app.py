from flask import render_template, Flask, Markup
from main import Main, GitMarkdown

app = Flask(__name__)

MAIN = Main()
git = GitMarkdown()

@app.route('/')
def index():

    message = 'These files are available: '

    return message
