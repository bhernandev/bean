from flask import Blueprint, render_template

bean = Blueprint('bean', __name__,
                 template_folder='templates',
                 static_folder='static')

@bean.route('/')
def index():
    return render_template('bean.html')
