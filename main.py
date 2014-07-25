from misaka import HtmlRenderer, Markdown


import os
import webbrowser


class GitMarkdown():

    def __init__(self):

        self.renderer = HtmlRenderer()
        self.markdown = Markdown(self.renderer)

    def render_html(self, string):

        html_string = self.markdown.render(string)

        return html_string


class Main():

    def __init__(self):

        self.file_dir = str(os.getcwd) + '/files_to_convert/'

    def return_file_list(self):

        file_list = []

        for file in os.listdir(self.file_dir):

            file_list.append(file)

        return file_list