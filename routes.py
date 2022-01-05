

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_title="Jesse's Portfolio")    

@app.route('/contact')
def about():
    return render_template('contact.html')