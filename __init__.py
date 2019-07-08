from flask import Flask
app = Flask(__name__, static_folder='static')

from .views import bean

app.register_blueprint(bean)
