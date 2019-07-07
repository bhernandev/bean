from flask import Flask
from flask import Blueprint, render_template
app = Flask(__name__, static_url_path='/static')

from .views import bean

app.register_blueprint(bean)
