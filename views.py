from bean import app, Blueprint, render_template

bean = Blueprint('bean', __name__,
                 template_folder='templates',
                 static_folder='static')

five = 5

@bean.route('/')
def index():
    return render_template('bean.html')
