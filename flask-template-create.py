import os
import argparse
import time

APP = """
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
"""
INDEX = """
{% extends 'base.html' %}

{% block title %}
{% endblock title %}

{% block custom_css %}
<!-- Custom CSS -->
<link rel="stylesheet" href="{{ url_for('static', filename='css/main.css') }}">
{% endblock custom_css %}

{% block body %}
<h1>Hello Flask</h1>
{% endblock body %}

{% block custom_js %}
<!-- Custom JS -->
<script src="{{ url_for('static', filename='script/index.js') }}"></script>
{% endblock custom_js %}

"""
BASE = """
<!doctype html>
<html lang="en">

<head>
  <!-- Required meta tags -->
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  {% block custom_css %}
  {% endblock custom_css %}

  <title>
    {% block title %}
    {% endblock title %}
  </title>
</head>

<body>
  {% block body %}
  {% endblock body %}

  <!-- Optional JavaScript -->
  <!-- jQuery first, then Popper.js, then Bootstrap JS -->
  <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js"
    integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n"
    crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
    integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
    crossorigin="anonymous"></script>

  <!-- jQuery google CDN-->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

  {% block custom_js %}
  {% endblock custom_js %}
</body>

</html>

"""


def file_maker(path, content):
    with open(path,"w") as f:
        f.writelines(content)


def make_dir_structure(root):
    path_for_placeholders = os.path.join(root, "templates", "placeholders")
    os.makedirs(path_for_placeholders, exist_ok=True)

    static_dirs = ['css', 'script', 'uploads']
    for static_dir in static_dirs:
        path = os.path.join(root, 'static', static_dir)
        os.makedirs(path, exist_ok=True)


def create_app_html_file(root):
    file_maker(path=os.path.join(root,"app.py"),content=APP)
    file_maker(path=os.path.join(root,"templates","index.html"),content=INDEX)
    file_maker(path=os.path.join(root,"templates","base.html"),content=BASE)
    

def touch_empty_files(root):
    static_dir_path=os.path.join(root,"static")
    files={
        'css/main.css': '/* main css comment */',
        'script/index.js': '// Index js file',
    }
    for file,content in files.items():
        dir_,file_ = file.split('/')
        path=os.path.join(static_dir_path,dir_,file_)
        file_maker(path, content)


def main(app_name):
    make_dir_structure(root=app_name)
    create_app_html_file(root=app_name)
    touch_empty_files(root=app_name)
    print(f'Your app {app_name} has been created')


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    ROOT = time.strftime("FlaskApp_%Y_%m_%d_%H_%M_%S")
    args.add_argument("--app-name", default=ROOT)
    parsed_args = args.parse_args()
    main(parsed_args.app_name)
