from flask import Flask
from flask import render_template
from flask import Markup
import os
import webbrowser

from misaka import Markdown, HtmlRenderer



app = Flask(__name__)

print 'These files are in the directory: \n'

print '=================================='

file_count = 0
file_dir = 'files_to_convert'
file_name = ''

for file in os.listdir(file_dir):
    if file.endswith(".txt") | file.endswith(".md") | file.endswith(".rst"):

        file_name = file

        print file + '\n'
        file_count += 1

print '=================================='

if file_count > 1:
    print '\nWhat would you like to view?'
    f_name = raw_input()

file_name = 'files_to_convert/' + file_name

with open(file_name, 'r') as f:
    content = f.read()

renderer = HtmlRenderer()
md = Markdown(renderer)

content = md.render(content)

webbrowser.open('http://127.0.0.1:5001')

@app.route('/')
def index():

    return render_template('index.html', content=content)


app.run(debug=True, port=5001)