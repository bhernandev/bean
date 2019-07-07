from bean import app, render_template

@app.route('/')
def index():
    return render_template('bean.html')
