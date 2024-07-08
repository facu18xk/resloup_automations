from bs4 import BeautifulSoup
import webbrowser, os, pyperclip

TEMPLATE = "index.html"


"""opens the email's template"""


def open_template(template):
    try:
        with open("index.html", "r") as file:
            html_doc = file.read()
            return html_doc
    except FileNotFoundError:
        return None


"""get the email content from the clibpoard"""


def get_content():
    content = {"title": None, "paragraphs": []}
    clipboard_mail = pyperclip.paste()
    messages = clipboard_mail.split("\n")
    messages = [message for message in messages if message != ""]
    # delete subject
    del messages[0]
    content["title"] = messages[0]
    # delete the title, so there are only paragraphs
    del messages[0]
    content["paragraphs"] = messages
    return content


"""Append a paragraph to the beautifulsoup document"""


def append_paragraph(document, paragraph):
    container = document.find(id="paragraphs")
    p = document.new_tag("p")
    p.string = paragraph
    container.append(p)


"""Append the title to the bs4 doc"""


def append_title(document, title):
    title_html = document.find(id="title")
    title_html.string = title


"""Append all the content"""


def append_content(document):
    content = get_content()
    paragraph_container = document.find(id="paragraphs")
    paragraph_container.string = ""
    # append the content
    [
        append_paragraph(document, paragraph)
        for paragraph in content["paragraphs"]
        if paragraph != ""
    ]
    append_title(document, content["title"])
    return document.prettify()


def get_template():
    template = BeautifulSoup(open_template(TEMPLATE), "html.parser")
    append_content(template)
    # Open the HTML content in the default web browser
    with open("temp.html", "w") as f:
        f.write(str(template.prettify()))
    webbrowser.open("file://" + os.path.realpath("temp.html"))


get_template()
