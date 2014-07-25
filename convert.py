import markdown
from flask import Flask
from flask import render_template
from flask import Markup
import os
import webbrowser

app = Flask(__name__)

print 'These files are in the directory: \n'

print '=================================='

file_count = 0

for file in os.listdir('/Users/kurtisjungersen/COS/'
                       'Markdown_Conversion/Files_to_convert'):
    if file.endswith(".txt") | file.endswith(".md") | file.endswith(".rst"):

        if file_count == 0:
            f_name = file

        print file + '\n'
        file_count += 1

print '=================================='

if file_count > 1:
    print '\nWhat would you like to view?'
    f_name = raw_input()

f_name = 'Files_to_convert/' + f_name

with open(f_name, 'r') as f:
    content = f.read()

content = Markup(markdown.markdown(content))

webbrowser.open('http://127.0.0.1:5001')

@app.route('/')
def index():

    return render_template('index.html', **locals())


app.run(debug=True, port=5001)